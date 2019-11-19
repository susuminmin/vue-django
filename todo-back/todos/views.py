from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


@api_view(['POST'])
def todo_create(request):
    # request.dats 는 axios 의 body 로 전달한 data
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # 사용자가 새롭게 작성한 데이터를 응답
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_id):
    # 수정하거나 삭제할 todo instance 호출
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'PUT':
        # instance todo 를 request.data 로 넘어온 값으로 수정하겠다
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=204)  # 삭제했습니다 status 코드
