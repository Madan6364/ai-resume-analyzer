async function uploadResume() {

    let file = document.getElementById("resume").files[0];

    let formData = new FormData();
    formData.append("file", file);

    let response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>ATS Score: ${data.ATS_score}</h3>
        <p><b>Skills Found:</b> ${data.skills_found}</p>
        <p><b>Missing Skills:</b> ${data.missing_skills}</p>
    `;
}