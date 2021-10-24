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
    const result = arr
        .filter(function (val) {
            return val.year === year &&
                val.month === month;
        })
        .sort(function (prev, next) {
            return next.amount - prev.amount;
        })
        .map(function (val) {
            return {
                type: val.type,
                amount: val.amount,
            };
        })
        .reduce(function (acc, val) {
            if (val.type === 'replenishment') {
                acc.monthBalance += val.amount;
                acc.monthReplenishment += val.amount;
            } else if (val.type === 'withdrawal') {
                acc.monthBalance -= val.amount;
                acc.monthWithdrawal += val.amount
            } else {
                acc.monthBalance -= val.amount
            }

            return acc;
        }, {monthBalance: 0, monthWithdrawal: 0, monthReplenishment: 0});

    result.withdrawalRate = (result.monthWithdrawal /
        result.monthReplenishment).toFixed(4);
    const futureDate = new Date(year, month) - 1;
    const lastDayOfMonthDate = new Date(futureDate);

    let lastDayMonth = lastDayOfMonthDate.getMonth() + 1;

    if (lastDayMonth < 10) {
        lastDayMonth = `0${lastDayMonth}`;
    }

    result.date = `${lastDayOfMonthDate.getFullYear()}`
        + `.${lastDayMonth}`
        + `.${lastDayOfMonthDate.getDate()}`;

    if (result.withdrawalRate < .15) {
        result.rank = 'Золотой';
    } else if (result.withdrawalRate < .3) {
        result.rank = 'Серебряный';
    } else {
        result.rank = 'Бронзовый';
    }
    delete result.monthReplenishment;

    return result;
}

function task23(arr) {
    const yearAndMonths = arr
        .map(function (val) {
            return {
                year: val.year,
                month: val.month
            };
        })
        .reduce(function (acc, val) {
            let isYearAndMonthAreInArray = !acc.some(function (e) {
                return JSON.stringify(e) === JSON.stringify(val);
            });

            if (isYearAndMonthAreInArray) {
                acc.push(val);
            }

            return acc;
        }, []);

    const result = [];

    for (const yearAndMonth of yearAndMonths) {
        result.push(task22(yearAndMonth.year, yearAndMonth.month, arr));
    }
    return result;
}