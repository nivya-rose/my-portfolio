document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const responseMessage = document.getElementById('response-message');
    responseMessage.textContent = 'Thank you for your message!';
    responseMessage.style.color = 'green';
    this.reset();
});