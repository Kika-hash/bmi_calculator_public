function clearQuestion() {
    document.getElementById("weight").value = "";
    document.getElementById("height").value = "";
    window.location.href = "/";
}

function needle() {
    const needle = document.getElementById('needle');
    needle.style.transform = `rotate(${needle}deg)`;
}


function moveNeedle(degrees) {
    const needle = document.getElementById('needle');
    needle.style.transform = `rotate(${degrees}deg)`;
}

window.addEventListener('DOMContentLoaded', function() {
    const needleDegree = document.getElementById('degreeValue').textContent;

    if (needleDegree) {
        moveNeedle(needleDegree);
    }
});

function clearFields() {
    weightInput.value = '';
    heightInput.value = '';
    messageDiv.textContent = '';
    needle.style.transform = 'rotate(0deg)';
    clearButton.disabled = true;
}