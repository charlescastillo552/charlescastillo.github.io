// script.js

const ctx = document.getElementById('participantsChart').getContext('2d');

const participantsData = {
  labels: ['Intro to Baking', 'Pastry Skills', 'Cake Decoration', 'Advanced Baking', 'Final Exam'],
  datasets: [{
    label: 'Participants Enrolled',
    data: [50, 60, 40, 30, 20], // Example data for participants in each section
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderColor: 'rgba(75, 192, 192, 1)',
    borderWidth: 1
  }]
};

const config = {
  type: 'bar',
  data: participantsData,
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
};

const participantsChart = new Chart(ctx, config);