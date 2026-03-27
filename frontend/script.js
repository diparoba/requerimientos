const API_URL = "http://localhost:8000";

async function fetchExercises() {
    try {
        const response = await fetch(`${API_URL}/exercises`);
        const exercises = await response.json();
        
        const container = document.getElementById('exercises-list');
        container.innerHTML = '';
        exercises.forEach(ex => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <h3>${ex.title}</h3>
                <p>${ex.description}</p>
                <a href="${ex.video_url}" target="_blank" class="card-link"><span>▶</span> Ver Guía de Ejercicios</a>
            `;
            container.appendChild(card);
        });
    } catch (error) {
        console.error("Error fetching exercises:", error);
    }
}

function setPain(level) {
    const buttons = document.querySelectorAll('.pain-scale button');
    buttons.forEach(btn => btn.classList.remove('active'));
    buttons[level - 1].classList.add('active');
    
    const status = document.getElementById('pain-status');
    let msg = "";
    if (level <= 3) msg = "Nivel bajo. ¡Buen momento para realizar tus estiramientos!";
    else if (level <= 7) msg = "Nivel moderado. Realiza los ejercicios con precaución.";
    else msg = "Nivel elevado. Por favor, descansa y consulta si el dolor persiste.";
    
    status.textContent = msg;
    
    // Auto-open chat and send info
    const chatWidget = document.getElementById('chat-widget');
    if (chatWidget.classList.contains('collapsed')) {
        toggleChat();
    }
    appendMessage('bot', `Nivel de dolor registrado: ${level}. ${msg}`);
}

function toggleChat() {
    const widget = document.getElementById('chat-widget');
    widget.classList.toggle('collapsed');
}

function appendMessage(sender, text) {
    const body = document.getElementById('chat-body');
    const bubble = document.createElement('div');
    bubble.className = `chat-bubble ${sender}`;
    bubble.textContent = text;
    body.appendChild(bubble);
    body.scrollTop = body.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById('chat-msg');
    const text = input.value.trim();
    if (text) {
        appendMessage('user', text);
        input.value = '';
        
        try {
            const response = await fetch(`${API_URL}/chat/send?message=${encodeURIComponent(text)}`, { 
                method: 'POST' 
            });
            const data = await response.json();
            
            setTimeout(() => {
                appendMessage('bot', data.reply);
            }, 600);
        } catch (error) {
            console.error("Error sending message:", error);
            setTimeout(() => {
                appendMessage('bot', "No pude procesar tu mensaje. ¿Lo intentamos de nuevo?");
            }, 600);
        }
    }
}

document.getElementById('chat-msg').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

document.addEventListener('DOMContentLoaded', () => {
    fetchExercises();
    setTimeout(() => {
        appendMessage('bot', "¡Hola! He reordenado la página según tus necesidades. Primero registremos tu nivel de dolor.");
    }, 1500);
});
