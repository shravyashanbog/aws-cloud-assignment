async function loadData() {

try {

const response = await fetch("/api/files");
const data = await response.json();

document.getElementById("totalFiles").innerText = data.length;
document.getElementById("lastUpdate").innerText = new Date().toLocaleTimeString();

const tableBody = document.getElementById("tableBody");
tableBody.innerHTML = "";

data.forEach(item => {

tableBody.innerHTML += `
<tr>
<td>${item.fileName}</td>
<td>${item.bucket}</td>
<td>${item.status}</td>
</tr>
`;

});

} catch (error) {

console.error(error);

}

}

loadData();
