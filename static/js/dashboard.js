var day = ["Monday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        var month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"
        ];
        setInterval(() => {
            let date = new Date();
            let full =
                `${day[date.getDay()]}, ${date.getDate()} ${month[date.getMonth()]} ${date.getFullYear()}`;
            document.getElementById("dashboard_date").innerHTML = full;
            document.getElementById("dashboard_clock").innerHTML = date.toTimeString().substr(0, 8);
        }, 1000);
        const skipped = (ctx, value) => ctx.p0.skip || ctx.p1.skip ? value : undefined;
        const ctx = document.getElementById('itemSoldChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                datasets: [{
                        label: 'Sold ',
                        data: [10, 15, 13, NaN, 52, 73, 14, 45, 12, 35, 92, 51],
                        backgroundColor: '#bbf7d0',
                        borderColor: '#16a34a',
                        borderWidth: 1,
                        tension: 0.1,
                        pointStyle: 'circle',
                        pointRadius: 5,
                        pointHoverRadius: 7,
                        segment: {
                            borderColor: ctx => skipped(ctx, '#bbf7d0'),
                            borderDash: ctx => skipped(ctx, [5, 5]),
                        },
                        spanGaps: true,
                    },
                    {
                        label: 'Purchase ',
                        data: [32, 39, 33, 55, 72, 53, 64, 85, 92, 65, 100, 61],
                        backgroundColor: '#fecaca',
                        borderColor: '#dc2626',
                        borderWidth: 1,
                        tension: 0.1,
                        pointStyle: 'circle',
                        pointRadius: 5,
                        pointHoverRadius: 7,
                        segment: {
                            borderColor: ctx => skipped(ctx, '#fecaca'),
                            borderDash: ctx => skipped(ctx, [5, 5]),
                        },
                        spanGaps: true,
                    },
                ]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    title: {
                        display: false,
                        text: 'Item Sold Chart',
                        font: {
                            size: 28,
                            family: "'Acme', sans-serif",
                            color: "#111827"
                        },
                        padding: {
                            top: 0,
                            bottom: 15,
                        },
                        align: 'start',
                    },
                },
            }
        });