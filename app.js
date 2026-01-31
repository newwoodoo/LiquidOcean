// Инициализация Telegram WebApp
const tg = window.Telegram.WebApp;

// Расширяем приложение на все доступное пространство
tg.expand();

// Настраиваем основную кнопку Telegram (внизу экрана)
tg.MainButton.text = "Закрыть приложение";
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#3b82f6";
tg.MainButton.show();

// Обработка нажатия на основную кнопку
tg.onEvent('mainButtonClicked', function() {
    tg.close();
});

// Функция для нашей кнопки внутри страницы
function checkSystem() {
    tg.HapticFeedback.impactOccurred('medium'); // Вибрация при нажатии
    alert('Связь с Telegram установлена!');
}
