from io import BytesIO
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib
matplotlib.use('Agg')


def chart_data_process(data):
    rate_closes = [item['rate_close'] for item in data]
    time_closes = [item['time_close'].split('.')[0] for item in data]
    time_closes = [datetime.strptime(
        time_closes[i], '%Y-%m-%dT%H:%M:%S') for i in range(len(time_closes))]
    return rate_closes, time_closes


def plot_data(rate_closes, time_closes, currency_name, date):
    # Clean memory of past charts
    plt.clf()

    plt.plot(rate_closes)

    # Show x-lab for every 7 days
    interval = 7

    plt.xticks(range(0, len(time_closes), interval), [time_closes[i].strftime(
        '%Y-%m-%d') for i in range(0, len(time_closes), interval)], rotation=90)
    plt.xlabel('Period')
    plt.ylabel('Rate Close')
    plt.title(f'{currency_name} rate changes from {date}')

    # Save the chart to a memory buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    return buf


def draw(currency_name, date, data):
    rate_closes, time_closes = chart_data_process(data)
    if not rate_closes:
        raise ValueError('Invalid currency name entered.')
    buf = plot_data(rate_closes, time_closes,
                    currency_name, date)
    return buf
