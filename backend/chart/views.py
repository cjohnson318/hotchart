from django.shortcuts import render

import random

def generate_data(N: int, w: float) -> tuple[list[str], list[float]]:
    labels = [""] * N
    values = [random.uniform(-0.1, 0.1)]
    for _ in range(1, N):
        prev = values[-1]
        val = prev * (1 - w) + random.uniform(-0.1, 0.1) * w
        values.append(val)
    return labels, values

def draw_line_chart(request):
    N = 40
    w = 0.05
    labels, values = generate_data(N, w)
    data = {
        "labels": labels,
        "values": values,
    }
    return render(request, 'line-chart.html', data)

def draw_histogram(request):
    N = 40
    w = 0.05
    labels, values = generate_data(N, w)
    data = {
        "labels": labels,
        "values": values,
    }
    return render(request, 'histogram.html', data)

def home(request):
    return render(request, 'home.html')