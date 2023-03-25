from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ToDoListSerializer
from accounts.models import User
from ToDoList.models import Tasks
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins

# if we wanna use api_view:
"""@api_view(["GET","POST","PUT"])
def list_view(request):
    tasks = Tasks.objects.filter(email = request.user)
    if request.method == 'GET':
        serializer = ToDoListSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ToDoListSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ToDoListSerializer(tasks, data = request.data, many=True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)"""


"""@api_view(["GET","PUT","DELETE"])
def task_detail(request, pk):
    task = get_object_or_404(Tasks, email = request.user, id=pk)
    if request.method == 'GET':
        serializer = ToDoListSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ToDoListSerializer(task, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response("detail: task removed successfully.")"""


# if we wanna use APIView:
'''class TaskList(APIView):
    permissionn_classes = [IsAuthenticated]
    serializer_class = ToDoListSerializer

    def get(self, request):
        tasks = Tasks.objects.filter(email = request.user)
        serializer = ToDoListSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoListSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

class TaskDetail(APIView):
    permissionn_classes = [IsAuthenticated]
    serializer_class = ToDoListSerializer

    def get(self, request, pk):
        task = get_object_or_404(Tasks, email = request.user, id=pk)
        serializer = ToDoListSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = get_object_or_404(Tasks, email = request.user, id=pk)
        serializer = ToDoListSerializer(task, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        task = get_object_or_404(Tasks, email = request.user, id=pk)
        task.delete()
        return Response("detail: task removed successfully.")'''


# if we wanna use GenericAPIView
'''class TaskList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permissionn_classes = [IsAuthenticated]
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return Tasks.objects.filter(email = self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)'''


# لطفا کامنت بزارید و راهنمایی کنید که این اکشن های ای پی آی رو چطور به فرانت منتقل کنیم تا اکشن های حال حاضر  واقعا به بک اند ریکوئست بزنه و ای پی آی بگیره همن که به لینک ریکوئست بزنه کافیه
# if we wanna use ListAPIView & CreateAPIView
class TaskList(ListAPIView, CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return Tasks.objects.filter(email = self.request.user)


class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return Tasks.objects.filter(email = self.request.user)