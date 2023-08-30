const faceTempt = document.getElementById('face-tempt');
const forheadTempt = document.getElementById("forhead-tempt")

// get root style
const r = document.querySelector(':root');
const css = getComputedStyle(r)


// plugins
const plugin = {
  id: 'customCanvasBackgroundColor',
  beforeDraw: (chart, args, options) => {
    const {ctx} = chart;
    ctx.save();
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle = options.color || '#99ffff';
    ctx.fillRect(0, 0, chart.width, chart.height);
    ctx.restore();
  }
};


//  face temeperature update
let face_highest =[29,30]
let face_average = [29,30]
let face_lowest = [29,30]

lbls= []
for(let i = 0;i <= 17;i++){
  lbls.push(i)
}

const dataFaceTempt = {
  labels: lbls,
  datasets: [
    {
      label: 'Highest',
      data: face_highest,
      borderColor: "red",
    },
    {
      label: 'Average',
      data: face_average,
      borderColor: "green",
    },
    {
      label: 'Lowest',
      data: face_lowest,
      borderColor: "blue",
    }
  ]
};

const configFaceTempt = {
    type: 'line',
    data: dataFaceTempt,
    options: {
      responsive: true, 
      elements:{
        point:{
          pointStyle:'star'
        }
      },
      plugins: {
        legend: {
          position: 'top',

        },
        title: {
          display: true,
          text: 'Face temperature'
        }
      }
    },
  };

Chart.defaults.borderColor = css.getPropertyValue("--secondaryDark2")

Chart.defaults.color = css.getPropertyValue("--secondary")
faceChart = new Chart(faceTempt,configFaceTempt);


function rand(){
  return Math.random() * (30 - 28) + 29
}

setInterval(()=>{
    face_highest.push(rand())
    face_average.push(rand())
    face_lowest.push(rand())

    if(face_highest.length > 16 )face_highest.shift()
    if(face_average.length > 16 )face_average.shift()
    if(face_lowest.length > 16) face_lowest.shift()

    
    faceChart.update('none')
},500)

// new Chart(forheadTempt,configForheadTempt);
