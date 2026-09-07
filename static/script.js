const cur = document.getElementById('cursor');
const ring = document.getElementById('cursor-ring');
let mx = 0, my = 0, rx = 0, ry = 0;

document.addEventListener('mousemove', e => {
    mx = e.clientX; my = e.clientY;
    cur.style.left = mx + 'px';
    cur.style.top  = my + 'px';
});

(function animRing() {
    rx += (mx - rx) * 0.12;
    ry += (my - ry) * 0.12;
    ring.style.left = rx + 'px';
    ring.style.top  = ry + 'px';
    requestAnimationFrame(animRing);
})();

document.querySelectorAll('button, input, .chip').forEach(el => {
    el.addEventListener('mouseenter', () => {
        ring.style.transform   = 'translate(-50%,-50%) scale(1.6)';
        ring.style.borderColor = 'rgba(77,150,255,0.8)';
    });
    el.addEventListener('mouseleave', () => {
        ring.style.transform   = 'translate(-50%,-50%) scale(1)';
        ring.style.borderColor = 'rgba(255,255,255,0.5)';
    });
});

const COLORS = ['#c9844a','#7b8cbc','#7a9e7e','#bc9664','#b482b4','#82aac8'];
const pc = document.getElementById('particles');

for (let i = 0; i < 28; i++) {
    const p     = document.createElement('div');
    p.className = 'particle';
    const size  = Math.random() * 4 + 2;
    const left  = Math.random() * 100;
    const dur   = Math.random() * 18 + 12;
    const delay = Math.random() * -20;
    const color = COLORS[Math.floor(Math.random() * COLORS.length)];
    p.style.cssText = `
        width:${size}px; height:${size}px; left:${left}%;
        background:${color}; box-shadow:0 0 ${size*3}px ${color};
        animation-duration:${dur}s; animation-delay:${delay}s;
    `;
    pc.appendChild(p);
}

function fillChip(btn) {
    // Strip leading emoji + space from chip text
    const text = btn.textContent.replace(/^[\S]+\s/, '').trim();
    document.getElementById('question').value = text;
    sendQuestion();
}


function hideWelcome() {
    const w = document.getElementById('welcome');
    if (!w) return;
    w.style.transition = 'all 0.3s ease';
    w.style.opacity    = '0';
    w.style.transform  = 'scale(0.95) translateY(-10px)';
    setTimeout(() => w.remove(), 300);
}


function appendMessage(role, text) {
    const chatBox = document.getElementById('chat-box');
    const row     = document.createElement('div');
    row.className = `msg-row ${role}`;
    row.innerHTML = `
        <div class="av ${role}">${role === 'user' ? '🧑' : '🤖'}</div>
        <div class="bubble ${role}">${text}</div>
    `;
    chatBox.appendChild(row);
    scrollBottom();
}

function showTyping() {
    const chatBox   = document.getElementById('chat-box');
    const typingRow = document.createElement('div');
    typingRow.className = 'msg-row bot';
    typingRow.id        = 'typing';
    typingRow.innerHTML = `
        <div class="av bot">🤖</div>
        <div class="typing-bubble">
            <div class="td"></div>
            <div class="td"></div>
            <div class="td"></div>
        </div>
    `;
    chatBox.appendChild(typingRow);
    scrollBottom();
}

function removeTyping() {
    document.getElementById('typing')?.remove();
}

function scrollBottom() {
    document.getElementById('chat-body').scrollTop = 99999;
}

/* =====================
   SEND QUESTION
   ===================== */
async function sendQuestion() {
    const input    = document.getElementById('question');
    const sendBtn  = document.getElementById('send-btn');
    const question = input.value.trim();

    if (!question) return;

    hideWelcome();
    appendMessage('user', question);
    input.value       = '';
    sendBtn.disabled  = true;
    showTyping();

    try {
        const res = await fetch('/ask', {
            method:  'POST',
            headers: { 'Content-Type': 'application/json' },
            body:    JSON.stringify({ question })
        });

        if (!res.ok) throw new Error(`Server error: ${res.status}`);

        const data = await res.json();
        removeTyping();
        appendMessage('bot', data.answer);

    } catch (err) {
        removeTyping();
        appendMessage('bot', `⚠️ Something went wrong. Please try again.<br>
            <small style="opacity:0.5">${err.message}</small>`);
    }

    sendBtn.disabled = false;
    scrollBottom();
    input.focus();
}