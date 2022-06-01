from django.http import JsonResponse
from .models import Framework
from .serializers import FrameworkSerializer

# Create your views here.
def framework_list(request):
    frameworks = Framework.objects.all()
    selializer = FrameworkSerializer(frameworks, many=True)
    return JsonResponse(selializer.data, safe=False)