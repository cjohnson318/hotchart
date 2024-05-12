from django.shortcuts import render
from turbo_helper import turbo_stream

import random

# ----- General Functions ----- #

N = 40
w = 0.95

def generate_data(N: int, w: float) -> tuple[list[str], list[float]]:
    labels = [""] * N
    values = [random.uniform(-0.1, 0.1)]
    for _ in range(1, N):
        prev = values[-1]
        val = prev * w + random.uniform(-0.1, 0.1) * (1.0 - w)
        values.append(val)
    return labels, values

def bundle_data_for_chartjs(N: int, w: float) -> dict[str, list]:
    labels, values = generate_data(N, w)
    data = {
        "labels": labels,
        "values": values,
    }
    return data

# ----- Home View ----- #

def home(request):
    return render(request, 'home.html')

# ----- Turbo Drive Functionality ----- #

def draw_line_chart(request):
    '''Draw a line chart with Chart.js.

    Used for Turbo Drive demo.
    '''
    data = bundle_data_for_chartjs(N, w)
    return render(request, 'line-chart.html', data)

def draw_histogram(request):
    '''Draw a histogram with Chart.js.
    
    Used for Turbo Drive demo.
    '''
    data = bundle_data_for_chartjs(N, w)
    return render(request, 'histogram.html', data)

# ----- Turbo Frame Functionality ----- #

def draw_inline_line_chart(request):
    '''Draw an inline line chart with Chart.js.

    Used for Turbo Frame demo.
    '''
    data = bundle_data_for_chartjs(N, w)
    return render(request, 'inline-line-chart.html', data)

# ----- Turbo Stream Functionality ----- #

def helper_stream(request):
    '''Used for django-turbo-helper endpoint.

    Used for Turbo Stream demo.
    '''
    data = bundle_data_for_chartjs(N, w)
    response = turbo_stream.response([
        turbo_stream.update(
            target="stream-chart",
            template="streamed-line-chart.html",
            context=data,
            request=request,
        ),
        turbo_stream.update(
            target="stream-data",
            template="streamed-data.html",
            context=data,
            request=request,
        )
    ])

    return response