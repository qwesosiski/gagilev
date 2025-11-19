// Отправка сообщений
document.querySelector('.send-btn').addEventListener('click', sendMessage);
document.querySelector('.message-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const input = document.querySelector('.message-input');
    const text = input.value.trim();
    
    if (text) {
        const messagesContainer = document.querySelector('.messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message my-message';
        messageDiv.innerHTML = `
            <div class="message-content">
                <div class="message-text">${text}</div>
                <div class="message-time">${new Date().toLocaleTimeString('ru-RU', {hour: '2-digit', minute:'2-digit'})}</div>
            </div>
        `;
        
        messagesContainer.appendChild(messageDiv);
        input.value = '';
        
        // Авто-ответ
        setTimeout(() => {
            const replies = [
                "Понял тебя!",
                "Интересно...",
                "Ага, понятно",
                "Хорошо, договорились!",
                "Угу, я слушаю"
            ];
            const reply = replies[Math.floor(Math.random() * replies.length)];
            
            const replyDiv = document.createElement('div');
            replyDiv.className = 'message other-message cloud';
            replyDiv.innerHTML = `
                <div class="message-avatar">
                    <img src="images/image1.png" alt="Влад">
                </div>
                <div class="message-content">
                    <div class="message-text">${reply}</div>
                    <div class="message-time">${new Date().toLocaleTimeString('ru-RU', {hour: '2-digit', minute:'2-digit'})}</div>
                </div>
            `;
            
            messagesContainer.appendChild(replyDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }, 1000);
        
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
}

// Переключение между чатами
document.querySelectorAll('.chat').forEach(chat => {
    chat.addEventListener('click', function() {
        document.querySelectorAll('.chat').forEach(c => c.classList.remove('active'));
        this.classList.add('active');
        
        // Обновляем заголовок чата
        const chatName = this.querySelector('.chat-name').textContent;
        document.querySelector('.partner-info h3').textContent = chatName;
        
        // Сбрасываем непрочитанные сообщения
        const unreadCount = this.querySelector('.unread-count');
        if (unreadCount) {
            unreadCount.remove();
        }
    });
});

// Создание нового чата
document.querySelector('.new-chat-btn').addEventListener('click', function() {
    alert('Функция создания нового чата будет реализована в будущем обновлении!');
});

// Поиск чатов
document.querySelector('.search-box input').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    const chats = document.querySelectorAll('.chat');
    
    chats.forEach(chat => {
        const chatName = chat.querySelector('.chat-name').textContent.toLowerCase();
        const lastMessage = chat.querySelector('.last-message').textContent.toLowerCase();
        
        if (chatName.includes(searchTerm) || lastMessage.includes(searchTerm)) {
            chat.style.display = 'flex';
        } else {
            chat.style.display = 'none';
        }
    });
});