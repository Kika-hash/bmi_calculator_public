function clearQuestion() {
    document.getElementById("weight").value = "";
    document.getElementById("height").value = "";
    window.location.href = "/";
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