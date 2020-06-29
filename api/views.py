from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Employee, Student
from api.serializers import EmployeeSerializer, EmployeeDeSerializer, StudentSerializer, StudentDeSerializer


class EmployeeAPIView(APIView):

    def get(self, request, *args, **kwargs):

        user_id = kwargs.get('pk')

        if user_id:
            emp_obj = Employee.objects.get(pk=user_id)
            many = False
        else:
            emp_obj = Employee.objects.all()
            many = True

        emp_ser = EmployeeSerializer(emp_obj, many=many)

        return Response({
            'status': 200,
            'msg': '查询成功',
            'result': emp_ser.data
        })



    def post(self, request, *args, **kwargs):
        emp_data = request.data
        if not isinstance(emp_data, dict) or emp_data == {}:
            return Response({
                'status': 500,
                'msg': '数据有误'
            })

        emp_des = EmployeeDeSerializer(data=emp_data)
        if emp_des.is_valid():
            new_emp = emp_des.save()
            return Response({
                'status': 200,
                'msg': '添加单个成功',
                'result': EmployeeSerializer(new_emp).data
            })
        else:
            return Response({
                'status': 500,
                'msg': '添加单个失败',
                'result': emp_des.errors
            })


class StudentAPIView(APIView):
    def get(self, request, *args, **kwargs):

        stu_id = kwargs.get('pk')

        if stu_id:
            stu_obj = Student.objects.get(pk=stu_id)
            many = False
        else:
            stu_obj = Student.objects.all()
            many = True

        stu_ser = StudentSerializer(stu_obj, many=many)

        return Response({
            'status': 200,
            'messages': '查询成功',
            'result': stu_ser.data
        })

    def post(self, request, *args, **kwargs):
        stu_data = request.data

        if not isinstance(stu_data, dict) or stu_data == {}:
            return Response({
                'status': 500,
                'msg': '数据有误'
            })

        stu_des = StudentDeSerializer(data=stu_data)
        if stu_des.is_valid():
            new_stu = stu_des.save()
            return Response({
                'status': 200,
                'msg': '添加成功',
                'result': StudentSerializer(new_stu).data
            })
        else:
            return Response({
                'status': 500,
                'msg': '添加失败',
                'detail': stu_des.errors
            })
