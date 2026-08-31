from django.http import JsonResponse
import json
from .models import Users

# Create your views here.

def PostManApi(req):
    if req.method == 'POST':
        data = json.loads(req.body)      # Store Full Data Of Json
        fn = data.get('firstname')
        em = data.get('email')
        password = data.get('password')
        mb = data.get('mobile')
        Ln = data.get('lastname')
        Users.objects.create(
            fullname=fn,
            email=em,
            password=password,
            mobile=mb,
            lastname=Ln
        )
        return JsonResponse({'message': 'Register SuccessFull'})
    else:
        return JsonResponse({'message': 'Register Failed'})


def LoginApi(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        Users.objects.get(
            email=data.get('ema'),
            password=data.get('pwd')
        )
        return JsonResponse({'message': 'Login Suceess'})
    else:
        return JsonResponse({'message': 'Login Fail'})


def GetApi(req):
    if req.method == 'GET':
        data = list(Users.objects.values(
            'id', 'fullname', 'lastname', 'email',
            'mobile'
        ))
        return JsonResponse(data, safe=False)


def DeleteApi(req, x_id):
    if req.method == 'DELETE':
        D = Users.objects.get(id=x_id)
        D.delete()
        return JsonResponse({'msg': 'delete successfull'})


def GetUsersApi(req, z_id):
    if req.method == 'GET':
        u = Users.objects.get(id=z_id)
        return JsonResponse({
            'fullname': u.fullname,
            'lastname': u.lastname,
            'email': u.email,
            'mobile': u.mobile
        })


def UpdateApi(req, user_id):
    D = Users.objects.get(id=user_id)
    if req.method == 'POST':
        data = json.loads(req.body)

        try:
            D.fullname = data.get('firstname')
            D.lastname = data.get('lastname')
            # D.email = data.get('email')
            D.mobile = data.get('mobile')
            D.save()
            return JsonResponse({'message': 'Update SuccessFully'})
        except:
            return JsonResponse({'message': 'Update failed'})