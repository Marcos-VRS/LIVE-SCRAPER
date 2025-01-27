import plotly.express as px
from django.http import JsonResponse


def live_chart(request):
    # Dados de exemplo
    data = [
        {"timestamp": "2025-01-26 12:00", "likes": 100, "comments": 5},
        {"timestamp": "2025-01-26 12:01", "likes": 150, "comments": 10},
    ]
    fig = px.line(data, x="timestamp", y=["likes", "comments"], title="Live Metrics")
    return JsonResponse(fig.to_json(), safe=False)
