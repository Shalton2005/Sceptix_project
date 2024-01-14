let medicine_inputs = [];
let water_inputs = [];
let sleep_inputs = [];

function medicineTracking() {
  const medicineName = prompt("Enter the name of the medicine:");
  const medicineDosage = prompt("Enter the dosage (in mg):");

  medicine_inputs.push({ name: medicineName, dosage: medicineDosage });
  document.getElementById("output").innerText = `Medicine tracked successfully!\nName: ${medicineName}, Dosage: ${medicineDosage} mg`;
}

function waterTracking() {
  const waterAmount = prompt("Enter the amount of water consumed (in ltr):");

  water_inputs.push({ amount: waterAmount });
  document.getElementById("output").innerText = `Water intake tracked successfully!\nAmount: ${waterAmount} litre`;
}

function sleepTracking() {
  const sleepDuration = prompt("Enter the duration of sleep (in hrs):");

  sleep_inputs.push({ duration: sleepDuration });
  document.getElementById("output").innerText = `Sleep tracked successfully!\nDuration: ${sleepDuration} hours`;
}

function viewPreviousData() {
  const previousData = document.getElementById("previousData");
  previousData.style.display = "block";

  document.getElementById("medicineData").innerHTML = `<h3>Medicine Tracker</h3>${formatData(medicine_inputs)}`;
  document.getElementById("waterData").innerHTML = `<h3>Water Tracker</h3>${formatData(water_inputs)}`;
  document.getElementById("sleepData").innerHTML = `<h3>Sleep Tracker</h3>${formatData(sleep_inputs)}`;

  document.getElementById("output").innerText = "";
}

function formatData(dataArray) {
  if (dataArray.length === 0) return "<p>No data available</p>";
  let formatted = "<ul>";
  dataArray.forEach(item => {
    formatted += "<li>";
    for (const key in item) {
      formatted += `${key}: ${item[key]}, `;
    }
    formatted = formatted.slice(0, -2);
    formatted += "</li>";
  });
  formatted += "</ul>";
  return formatted;
}

function exitSite() {
  alert("Exited");
  window.close();
}
