function task21(arr) {
    return arr
        .map(function (val) {
            return {
                year: val.year,
                month: val.month
            };
        })
        .reduce(function (acc, val) {
            const payment = acc.find(function (el) {
                return el.month === val.month;
            });

            if (!payment) {
                val.totalOps = 1
                acc.push(val);
            } else {
                payment.totalOps++;
            }

            return acc
                .sort(function (prev, next) {
                    return next.totalOps - prev.totalOps
                });
        }, [])
        .slice(0, 3);
}

function task22(year, month, arr) {
    return {
        date: '2019-01-31',
        monthBalance: 1234,
        monthWithdrawal: 33,
        withdrawalRate: 0.11,
        rank: 'Золотой'
    };
}

function task23(arr) {
    return arr;
}