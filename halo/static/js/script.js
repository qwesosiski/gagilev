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
                    <img src="../static/images/image1.png" alt="Влад">
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

// Данные для чатов (аватарки и история сообщений)
const chatData = {
    'Влад': {
        avatar: '../static/images/image1.png',
        messages: [
            { type: 'other', text: 'Привет! Как дела?', time: '10:30' },
            { type: 'my', text: 'Привет! Всё отлично, спасибо!', time: '10:32' },
            { type: 'other', text: 'Отлично! Что нового?', time: '10:33' }
        ]
    },
    'Костя': {
        avatar: '../static/images/kot.webp',
        messages: [
            { type: 'other', text: 'Добрый день!', time: '09:15' },
            { type: 'my', text: 'Привет! Как твои успехи?', time: '09:20' },
            { type: 'other', text: 'Всё хорошо, работаю над проектом', time: '09:22' }
        ]
    },
    'Вадя': {
        avatar: '../static/images/rebenok.jpg',
        messages: [
            { type: 'other', text: 'Привет! Готов к встрече?', time: '14:10' },
            { type: 'my', text: 'Да, готов! Во сколько?', time: '14:12' },
            { type: 'other', text: 'Давай в 15:00', time: '14:13' }
        ]
    },
    'Дота2Пати': {
        avatar: '../static/images/tigrulla.jpg',
        messages: [
            { type: 'other', text: 'Здравствуйте!', time: '11:05' },
            { type: 'my', text: 'Привет! Как проходит день?', time: '11:10' },
            { type: 'other', text: 'Отлично, спасибо!', time: '11:12' }
        ]
    },
    'Мама': {
        avatar: '../static/images/mama.jpg',
        messages: [
            { type: 'other', text: 'Привет!', time: '11:05' },
            { type: 'my', text: 'Привет! Как проходит день?', time: '11:10' },
            { type: 'other', text: 'Отлично, спасибо!', time: '11:12' }
        ]
    }
};

// Функция для загрузки истории чата
function loadChatHistory(chatName) {
    const messagesContainer = document.querySelector('.messages');
    messagesContainer.innerHTML = ''; // Очищаем контейнер
    
    const chat = chatData[chatName];
    if (chat) {
        // Обновляем аватарку в заголовке
        document.querySelector('.partner-avatar img').src = chat.avatar;
        document.querySelector('.partner-avatar img').alt = chatName;
        
        // Загружаем историю сообщений
        chat.messages.forEach(message => {
            const messageDiv = document.createElement('div');
            
            if (message.type === 'my') {
                messageDiv.className = 'message my-message';
                messageDiv.innerHTML = `
                    <div class="message-content">
                        <div class="message-text">${message.text}</div>
                        <div class="message-time">${message.time}</div>
                    </div>
                `;
            } else {
                messageDiv.className = 'message other-message cloud';
                messageDiv.innerHTML = `
                    <div class="message-avatar">
                        <img src="${chat.avatar}" alt="${chatName}">
                    </div>
                    <div class="message-content">
                        <div class="message-text">${message.text}</div>
                        <div class="message-time">${message.time}</div>
                    </div>
                `;
            }
            
            messagesContainer.appendChild(messageDiv);
        });
        
        // Прокручиваем вниз
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
        
        // Загружаем историю чата и меняем аватарку
        loadChatHistory(chatName);
        
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

// Загружаем первый чат по умолчанию при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    const firstChat = document.querySelector('.chat.active');
    if (firstChat) {
        const chatName = firstChat.querySelector('.chat-name').textContent;
        loadChatHistory(chatName);
    }
});

// // Отправка сообщений
// document.querySelector('.send-btn').addEventListener('click', sendMessage);
// document.querySelector('.message-input').addEventListener('keypress', function(e) {
//     if (e.key === 'Enter') {
//         sendMessage();
//     }
// });

// function sendMessage() {
//     const input = document.querySelector('.message-input');
//     const text = input.value.trim();
    
//     if (text) {
//         const messagesContainer = document.querySelector('.messages');
//         const messageDiv = document.createElement('div');
//         messageDiv.className = 'message my-message';
//         messageDiv.innerHTML = `
//             <div class="message-content">
//                 <div class="message-text">${text}</div>
//                 <div class="message-time">${new Date().toLocaleTimeString('ru-RU', {hour: '2-digit', minute:'2-digit'})}</div>
//             </div>
//         `;
        
//         messagesContainer.appendChild(messageDiv);
//         input.value = '';
        
//         // Авто-ответ
//         setTimeout(() => {
//             const replies = [
//                 "Понял тебя!",
//                 "Интересно...",
//                 "Ага, понятно",
//                 "Хорошо, договорились!",
//                 "Угу, я слушаю"
//             ];
//             const reply = replies[Math.floor(Math.random() * replies.length)];
            
//             const replyDiv = document.createElement('div');
//             replyDiv.className = 'message other-message cloud';
//             replyDiv.innerHTML = `
//                 <div class="message-avatar">
//                     <img src="../static/images/image1.png" alt="Влад">
//                 </div>
//                 <div class="message-content">
//                     <div class="message-text">${reply}</div>
//                     <div class="message-time">${new Date().toLocaleTimeString('ru-RU', {hour: '2-digit', minute:'2-digit'})}</div>
//                 </div>
//             `;
            
//             messagesContainer.appendChild(replyDiv);
//             messagesContainer.scrollTop = messagesContainer.scrollHeight;
//         }, 1000);
        
//         messagesContainer.scrollTop = messagesContainer.scrollHeight;
//     }
// }

// // Переключение между чатами
// document.querySelectorAll('.chat').forEach(chat => {
//     chat.addEventListener('click', function() {
//         document.querySelectorAll('.chat').forEach(c => c.classList.remove('active'));
//         this.classList.add('active');
        
//         // Обновляем заголовок чата
//         const chatName = this.querySelector('.chat-name').textContent;
//         document.querySelector('.partner-info h3').textContent = chatName;
        
//         // Сбрасываем непрочитанные сообщения
//         const unreadCount = this.querySelector('.unread-count');
//         if (unreadCount) {
//             unreadCount.remove();
//         }
//     });
// });

// // Создание нового чата
// document.querySelector('.new-chat-btn').addEventListener('click', function() {
//     alert('Функция создания нового чата будет реализована в будущем обновлении!');
// });

// // Поиск чатов
// document.querySelector('.search-box input').addEventListener('input', function(e) {
//     const searchTerm = e.target.value.toLowerCase();
//     const chats = document.querySelectorAll('.chat');
    
//     chats.forEach(chat => {
//         const chatName = chat.querySelector('.chat-name').textContent.toLowerCase();
//         const lastMessage = chat.querySelector('.last-message').textContent.toLowerCase();
        
//         if (chatName.includes(searchTerm) || lastMessage.includes(searchTerm)) {
//             chat.style.display = 'flex';
//         } else {
//             chat.style.display = 'none';
//         }
//     });
// });