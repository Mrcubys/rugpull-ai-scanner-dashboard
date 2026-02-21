let chart;

async function scan(){
  const chain = document.getElementById("chain").value;
  const token = document.getElementById("token").value;

  const res = await fetch("http://127.0.0.1:8000/scan", {
    method:"POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({chain, address: token})
  });

  const data = await res.json();
  const risk = (data.rug_risk*100).toFixed(2);
  document.getElementById("risk").innerText = "Risk: "+risk+"%";

  if(chart) chart.destroy();
  const ctx = document.getElementById('riskChart').getContext('2d');
  chart = new Chart(ctx,{
    type:'bar',
    data:{
      labels:Object.keys(data.features),
      datasets:[{
        label:'Feature Values',
        data:Object.values(data.features),
        backgroundColor:'rgba(255,99,132,0.5)'
      }]
    }
  });
}
