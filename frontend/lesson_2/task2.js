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
                return el.month === val.month &&
                    el.year === val.year;
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

    result.date = lastDayOfMonthDate.toISOString().slice(0, 10);

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
    return arr
        .map(function (val) {
            return {
                year: val.year,
                month: val.month,
            };
        })
        .reduce(function (acc, val) {
            let areYearAndMonthNotInArray = !acc.some(function (e) {
                const parsedDate = new Date(e.date);
                const currentPayment = {
                    year: parsedDate.getFullYear(),
                    month: parsedDate.getMonth() + 1,
                };
                return JSON.stringify(currentPayment) === JSON.stringify(val);
            });

            if (areYearAndMonthNotInArray) {
                const currentPayment = task22(val.year, val.month, arr);
                const isFirstPaymentInDateInterval = acc.length === 0;

                if (isFirstPaymentInDateInterval) {
                    currentPayment.totalBalance = 0;
                } else {
                    currentPayment.totalBalance = acc[acc.length - 1].totalBalance;
                }
                currentPayment.totalBalance += currentPayment.monthBalance;

                acc.push(currentPayment);
            }

            return acc;
        }, []);
}