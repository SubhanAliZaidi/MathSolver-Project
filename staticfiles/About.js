
const data = {

    labels: ['HTML', 'CSS', 'JAVASCRIPT', 'PYTHON', 'DJANGO'],

    datasets: [{
        data: [5426, 5455, 1346, 2497, 206],
        backgroundColor: [
            'rgb(227, 76, 38)',
            'rgb(32, 98, 175)',
            'rgb(244, 129, 49)',
            'rgb(21, 214, 118)',
            'rgb(153, 102, 255)',
        ],
        borderColor: [
            'rgb(227, 76, 38)',
            'rgb(32, 98, 175)',
            'rgb(244, 129, 49)',
            'rgb(21, 214, 118)',
            'rgb(153, 102, 255)',
        ],
        borderWidth: 1
    }],
};

const options = {
    plugins:{
        legend:{
            display:false
        }
    }
};

const config = {
    type: 'pie',
    data,
    options,
};

const myChart = new Chart(
    document.getElementById('myChart'),
    config
);
