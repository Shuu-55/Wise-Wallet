const chart= document.querySelector("#chart").getContext('2d');

// create a new chart instance

new Chart(chart, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb','Mar','Apr','May','Jun'],

        datasets: [
            {
                label:'Balance Status',
                data: [ 27400, 26700, 25600, 22500, 27500, 26000],
                borderColor: 'red', 
                borderWidth: 2
            },
            {
                label:'Expense Overview',
                data: [ 35000, 34700, 32900, 38000, 33500, 38000],
                borderColor: 'blue',
                borderWidth: 2
            },
            {
                label:'Savings',
                data: [ 17600, 18600, 21500, 18500, 14600, 16000],
                borderColor: 'green',
                borderWidth: 2
            },
        ]
    },
    options: {
        responsive: true
    }
})

const mylist = ()=>{
    Map()
}