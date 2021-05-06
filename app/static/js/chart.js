$(document).ready(function () {
    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "Air temperature (C°) near by device",
                backgroundColor: 'rgb(255,140,0)',
                borderColor: 'rgb(255,140,0)',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        labelString: 'Date (Y-M-D h:m:s)',
                        display: true
                    },
                    gridLines: {
                        color: "#ffffff",
                        display: false
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        labelString: 'Air temperature (C°)',
                        display: true
                    },
                    ticks: {
                        beginAtZero: true
                    },
                    gridLines: {
                        color: "#ffffff",
                        display: false
                    }
                }]
            }
        }
    };
    Chart.defaults.global.defaultFontColor = "#ffffff";
    Chart.defaults.global.defaultFontStyle = 'Bold';

    const context = document.getElementById('canvas').getContext('2d');
    const lineChart = new Chart(context, config);
    const source = new EventSource("/convert_chart_data");
    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (config.data.labels.length === 20) {
            config.data.labels.shift();
            config.data.datasets[0].data.shift();
        }
        config.data.labels.push(data.time);
        config.data.datasets[0].data.push(data.value);
        lineChart.update();
    }
});