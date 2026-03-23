async function fetchExercises() {
    // Simulando fetch de la API de FastAPI
    const sampleExercises = [
        { title: "Estiramiento Lumbar", description: "Estiramiento suave para la zona baja de la espalda.", video: "🎥" },
        { title: "Movilidad Cervical", description: "Ejercicios para reducir la tensión en el cuello.", video: "🎥" }
    ];
    
    const container = document.getElementById('exercises-list');
    sampleExercises.forEach(ex => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `<h3>${ex.title}</h3><p>${ex.description}</p><span>${ex.video} Ver video</span>`;
        container.appendChild(card);
    });
}

function sendMessage() {
    const input = document.getElementById('chat-msg');
    const body = document.getElementById('chat-body');
    if (input.value.trim()) {
        const msg = document.createElement('p');
        msg.textContent = `Tú: ${input.value}`;
        body.appendChild(msg);
        input.value = '';
        
        setTimeout(() => {
            const reply = document.createElement('p');
            reply.textContent = `Fisio: Hola, ¿en qué podemos ayudarte oggi?`;
            reply.style.color = '#4f46e5';
            body.appendChild(reply);
        }, 1000);
    }
}

document.addEventListener('DOMContentLoaded', fetchExercises);
