var dragon = new VanillaDragon({onopen: onOpen, onchannelmessage: onChannelMessage});
var notificationsList = document.getElementById("notifications");

function onChannelMessage(channels, message) {
    addNotification((message.data));
    }

function onOpen() {
    dragon.subscribe('notification', 'notifications');
}

function addNotification(notification) {

    new Notification(notification.content);

    var li = document.createElement("li");
    notificationsList.insertBefore(li, notificationsList.firstChild);
    li.innerHTML = notification.content;

    while (notificationsList.getElementsByTagName("li").length > 5) {
    notificationsList.getElementsByTagName("li")[5].remove();
    }
}