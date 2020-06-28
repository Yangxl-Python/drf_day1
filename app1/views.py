from django.db import transaction
from django.http import HttpResponse, JsonResponse, QueryDict
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import User


@csrf_exempt
def users(request):

    if request.method == 'GET':
        print('get success')
        return HttpResponse('get success')

    elif request.method == 'POST':
        print('post success')
        return HttpResponse('post success')

    elif request.method == 'PUT':
        print('put success')
        return HttpResponse('put success')

    elif request.method == 'DELETE':
        print('delete success')
        return HttpResponse('delete success')

    return HttpResponse('fail')


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request, *args, **kwargs):

        user_id = kwargs.get('pk')
        if user_id:
            user = User.objects.filter(pk=user_id).values('pk', 'username', 'password', 'gender').first()
            print(user)
            if user:
                return JsonResponse({
                    'status': 200,
                    'message': '查询单个用户成功',
                    'result': user
                })
        else:
            all_users = User.objects.all().values('pk', 'username', 'password', 'gender')
            if all_users:
                return JsonResponse({
                    'status': 200,
                    'message': '查询所有用户成功',
                    'result': list(all_users)
                })

        return JsonResponse({
            'status': 500,
            'message': '查询失败'
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        gender = request.POST.get('gender')

        try:
            new_user = User.objects.create(username=username, password=pwd, gender=gender)
            if new_user:
                return JsonResponse({
                    'status': 201,
                    'message': '创建用户成功',
                    'result': {
                        'username': new_user.username,
                        'gender': new_user.gender
                    }
                })
        except Exception as e:
            return JsonResponse({
                'status': 501,
                'message': f'创建用户失败：{e}',
            })

    def put(self, request, *args, **kwargs):
        print('put success')
        return HttpResponse('put success')

    def delete(self, request, *args, **kwargs):
        print('delete success')
        return HttpResponse('delete success')


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        if user_id:
            user_obj = User.objects.filter(pk=user_id).values('username', 'password', 'gender').first()
            return Response({
                'status': 200,
                'message': '查询单个成功',
                'result': user_obj
            })
        else:
            all_users = User.objects.all().values('id', 'username', 'password', 'gender')
            return Response({
                'status': 200,
                'message': '查询所有成功',
                'result': list(all_users)
            })

    def post(self, request, *args, **kwargs):
        user_data = request.data
        if isinstance(user_data, QueryDict):
            user_data = user_data.dict()
        if isinstance(user_data, dict):
            try:
                new_user = User.objects.create(**user_data)
                if new_user:
                    return Response({
                        'status': 200,
                        'message': '创建成功',
                        'result': {
                            'username': new_user.username,
                            'gender': new_user.gender
                        }
                    })
            except Exception as e:
                return Response({
                    'status': 500,
                    'message': f'创建失败：{e}'
                })

        return Response({
            'status': 500,
            'message': '创建失败'
        })

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        if user_id:
            user_data = request.data
            try:
                with transaction.atomic():
                    user_obj = User.objects.filter(pk=user_id).first()
                    user_obj.username = user_data.get('username')
                    user_obj.password = user_data.get('password')
                    user_obj.gender = user_data.get('gender')
                    user_obj.save()
                    return Response({
                        'status': 200,
                        'message': '修改成功',
                        'result': {
                            'username': user_obj.username,
                            'gender': user_obj.gender
                        }
                    })
            except Exception as e:
                return Response({
                    'status': 500,
                    'message': f'修改失败：{e}'
                })
        return Response({
            'status': 500,
            'message': '修改失败'
        })

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        if user_id:
            try:
                user_obj = User.objects.filter(pk=user_id).first()
                user_obj.delete()
                return Response({
                    'status': 200,
                    'message': '删除成功'
                })
            except Exception as e:
                return Response({
                    'status': 500,
                    'message': f'删除失败：{e}'
                })
        return Response({
            'status': 500,
            'message': '删除失败'
        })
