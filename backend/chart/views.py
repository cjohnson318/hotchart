from django.shortcuts import render

import random

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

def home(request):
    return render(request, 'home.html')

def draw_line_chart(request):
    data = bundle_data_for_chartjs(N, w)
    return render(request, 'line-chart.html', data)

def draw_histogram(request):
    data = bundle_data_for_chartjs(N, w)
    return render(request, 'histogram.html', data)

def draw_inline_line_chart(request):
    data = bundle_data_for_chartjs(N, w)
    return render(request, 'inline-line-chart.html', data)