document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    if (!userInput.trim()) return;

    let chatbox = document.getElementById("messages");
    chatbox.innerHTML += `<div class="user-message">${userInput}</div>`;

    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ message: userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        let reply = data.reply || "Sorry, I couldn't understand.";
        chatbox.innerHTML += `<div class="bot-message">${reply}</div>`;
    })
    .catch(error => console.error("Error:", error));

    document.getElementById("userInput").value = "";
}
