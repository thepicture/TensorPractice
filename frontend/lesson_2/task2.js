/**
 * Maps the payment to year and month representation.
 * @returns {function(*): {month: *, year: *}} The payment object with year and month representation.
 */
function mapToYearAndMonth() {
    return function (val) {
        return {
            year: val.year,
            month: val.month,
        };
    };
}

/**
 * Returns first three payments with the biggest operations count in a month.
 * @param arr The input array with payments.
 * @returns {*} An array with first three months with the biggest payments.
 */
function task21(arr) {
    return arr
        .map(mapToYearAndMonth())
        .reduce(function (acc, val) {
            const payment = acc.find(function (el) {
                return el.month === val.month &&
                    el.year === val.year;
            });

            if (!payment) {
                val.totalOps = 1;
                acc.push(val);
            } else {
                payment.totalOps++;
            }

            return acc
                .sort(function (prev, next) {
                    return next.totalOps - prev.totalOps;
                });
        }, [])
        .slice(0, 3);
}

/**
 * Returns statistic in the end of a specified month.
 * @param year The year of payment.
 * @param month The month of payment.
 * @param arr The input array with payments.
 * @returns {*} Statistic in the end of a specified month.
 */
function task22(year, month, arr) {
    const resultArray = arr
        .filter(function (val) {
            return val.year === year &&
                val.month === month;
        })
        .sort(function (prev, next) {
            return next.amount - prev.amount;
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

            acc.withdrawalRate = (acc.monthWithdrawal /
                acc.monthReplenishment).toFixed(4);

            const futureDate = new Date(year, month) - 1;
            const lastDayOfMonthDate = new Date(futureDate);

            acc.date = lastDayOfMonthDate.toISOString().slice(0, 10);

            if (isNaN(acc.withdrawalRate)) {
                acc.withdrawalRate = 'Не определено';
            }

            if (acc.withdrawalRate < .15) {
                acc.rank = 'Золотой';
            } else if (acc.withdrawalRate < .3) {
                acc.rank = 'Серебряный';
            } else {
                acc.rank = 'Бронзовый';
            }

            return acc;
        }, {monthBalance: 0, monthWithdrawal: 0, monthReplenishment: 0});

    return {
        date: resultArray.date,
        monthBalance: resultArray.monthBalance,
        monthWithdrawal: resultArray.monthWithdrawal,
        withdrawalRate: resultArray.withdrawalRate,
        rank: resultArray.rank,
    };
}

/**
 * Returns statistic in the end of all months in an interval.
 * @param arr The input array with payments.
 * @returns {*} Statistic in the end of all months in an interval.
 */
function task23(arr) {
    return arr
        .sort(function (prev, next) {
            const prevDate = new Date(prev.year, prev.month, prev.day).toISOString();
            const nextDate = new Date(next.year, next.month, next.day).toISOString();

            if (prevDate <= nextDate) {
                return -1;
            } else {
                return 1;
            }
        })
        .map(mapToYearAndMonth())
        .reduce(function (acc, val) {
            const areYearAndMonthNotInArray = !acc.some(function (paymentOfArray) {
                const parsedDate = new Date(paymentOfArray.date);
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
                    const lastIndex = acc.length - 1;

                    currentPayment.totalBalance = acc[lastIndex].totalBalance;
                }
                currentPayment.totalBalance += currentPayment.monthBalance;

                acc.push(currentPayment);
            }

            return acc;
        }, []);
}