const tg = window.Telegram.WebApp;

tg.expand();

// Получаем имя пользователя из Telegram
const userName = tg.initDataUnsafe?.user?.first_name || "Пользователь";

// Выводим имя на экран, когда страница загрузится
window.onload = function() {
    document.getElementById("user-name").innerText = `Привет, ${userName}!`;
};

tg.MainButton.text = "Закрыть Ocean";
tg.MainButton.show();

tg.onEvent('mainButtonClicked', function() {
    tg.close();
});

function checkSystem() {
    tg.HapticFeedback.notificationOccurred('success');
    alert(`Связь в норме, ${userName}!`);
}
