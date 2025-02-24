document.addEventListener("DOMContentLoaded", function () {
    const changingText = document.getElementById("changing-text");
    const words = ["Django", "HTML", "CSS","MySQL","MSSQL","Python"];
    let index = 0;
  
    function changeText() {
      changingText.textContent = `Proficient In: ${words[index]}`;
      index = (index + 1) % words.length;
    }
  
    setInterval(changeText, 1500);
  });
  