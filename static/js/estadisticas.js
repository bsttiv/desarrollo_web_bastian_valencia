async function cargarGrafico1(){
    const chart = Highcharts.chart('grafico1', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Avisos de adopcion por dia (ultimo mes)'
        },
        xAxis: {
            type: "datetime",
            dateTimeLabelFormats: {
                month: "%b-%e-%Y",
            },
            title: {
                text: "Fecha",
            },
        },
        yAxis: {
            title: {
                text: 'Numero de avisos'
            }
        },
        legend: {
            align: "left",
            verticalAlign: "top",
            borderWidth: 0,
        },

        tooltip: {
            shared: true,
            crosshairs: true,
        },

        series: [{
            name: "Avisos",
            data: [],
            lineWidth: 1,
            marker: {
                enabled: true,
                radius: 4,
            },
            color: "#4f28fcff",
        }]
    });
    try {
        const resp = await fetch(`${window.origin}/estadisticas/avisos_por_dia`, { method: "GET", cache: "no-cache" })
        if (!resp.ok) {
            throw new Error(`Error cargando avisos por dia: Status ${resp.status}`)
        }
        const data = await resp.json()
        if (data.error) {
            throw new Error(`Error de respuesta del endpoint: ${data.error}`)
        }
        let parsedData = data.avisos.map((aviso) => {
            const [dia, mes, año] = aviso.fecha
                .split("-")
                .map((part) => parseInt(part, 10));
            return [
                Date.UTC(año, mes - 1, dia), // javascript month indices start from 0 !
                aviso.num,
            ];
        });
        chart.update({
            series: [
                {
                    data: parsedData,
                },
            ],
        })
    } catch (error) {
        console.error(error)
    }
}

async function cargarGrafico2(){
    const chart = Highcharts.chart('grafico2', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Avisos de adopcion totales por tipo de mascota'
        },
        legend: {
            align: "left",
            verticalAlign: "top",
            borderWidth: 0,
        },

        tooltip: {
            shared: true,
            crosshairs: true,
        },
        series: [
        {
            name: 'Total',
            colorByPoint: true,
            data: [
                
            ]
        }
    ]
    });
    try {
        const resp = await fetch(`${window.origin}/estadisticas/avisos_por_tipo`, { method: "GET", cache: "no-cache" })
        if (!resp.ok) {
            throw new Error(`Error cargando avisos por tipo: Status ${resp.status}`)
        }
        const data = await resp.json()
        if (data.error) {
            throw new Error(`Error de respuesta del endpoint: ${data.error}`)
        }
        chart.update({
            series: [
                {
                    data: [
                        {name: "Perro", y:data.perro},
                        {name: "Gato", y:data.gato},
                    ],
                },
            ],
        })
    } catch (error) {
        console.error(error)
    }
}

async function cargarGrafico3(){
    const chart = Highcharts.chart('grafico3', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Avisos de adopcion por mes (separado por tipo)'
        },
        xAxis: {
            categories: ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
            title: "Mes"
        },
        yAxis: {
            title: {
                text: 'Numero de avisos'
            }
        },

        series: [
        {
            name: "Perro",
            data: [],
            color: "#4f28fcff"
        },
        {
            name: "Gato",
            data: [],
            color: "#ff5733"
        }
    ]
    });
    try {
        const resp = await fetch(`${window.origin}/estadisticas/avisos_por_meses/`, { method: "GET", cache: "no-cache" })
        if (!resp.ok) {
            throw new Error(`Error cargando avisos por dia: Status ${resp.status}`)
        }
        const data = await resp.json()
        if (data.error) {
            throw new Error(`Error de respuesta del endpoint: ${data.error}`)
        }
        let avisosPerro = data.avisos.map(aviso => aviso.perro)
        let avisosGato = data.avisos.map(aviso => aviso.gato)
        chart.update({
            series: [
                {
                    name: "Perro",
                    data: avisosPerro
                },
                {
                    name: "Gato",
                    data: avisosGato
                }
            ],
        })
    } catch (error) {
        console.error(error)
    }
}

document.addEventListener('DOMContentLoaded', async function () {
    await cargarGrafico1()
    await cargarGrafico2()
    await cargarGrafico3()
});