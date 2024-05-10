function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatMessages = document.getElementById("chat-messages");
    var userMessage = '<div class="user-message">' + userInput + '</div>';
    chatMessages.innerHTML += userMessage;
    document.getElementById("user-input").value = "";

    // Send user input to server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/send-message/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var botResponse = '<div class="bot-message">Bot: ' + JSON.parse(xhr.responseText).reply + '</div>';
            chatMessages.innerHTML += botResponse;
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    };
    xhr.send("message=" + userInput);
}
