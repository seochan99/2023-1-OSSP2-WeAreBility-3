from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Users
from .serializer import userSerializer # 이부분 수정
from .walking_course_recommender import tokenizer # 이부분 수정


@csrf_exempt
def user_list(request):
    if request.method != 'POST': # GET 방식일 때
        query_set = Users.objects.all() # ORM으로 Users의 모든 객체 받아옴
        serializer = userSerializer(query_set, many=True) # JSON으로 변환
        return HttpResponse(serializer.data) # JSON타입의 데이터로 응답

    elif request.method == 'POST': # POST방식일 때
        query_set = Users.objects.all() # ORM으로 Users의 모든 객체 받아옴
        query_set.delete() # 모든 데이터 삭제
        data = JSONParser().parse(request) # 요청들어온 데이터를 JSON 타입으로 파싱

        # parsing 부분
        userId_data = data["data"]["userId"]
        locations_data = data["data"]["locations"] # 내부 for 문 추가요망
        points = ""
        for i in locations_data :
            points += str(i["latitude"]) + " "
            points += str(i["longitude"]) + " "
    
        serializer = userSerializer(data=data) # Serializer를 사용해 전송받은 데이터를 변환하기 위함
        if serializer.is_valid():
            serializer.save() # 데이터 저장
            user = Users.objects.all()
            user = user.last()
            """checker = similarity_Checker(user.user_id, user.userid, user.title, user.createdDateTime,
                                         user.introduction, user.coursekeyword, user.segmentId,
                                         user.startPoint, user.endPoint, user.points)
            return JsonResponse(checker.calculate_Similarity(user.points), safe=False)""" # 이 부분 recommender로 수정
        return JsonResponse(serializer.errors, status=400)
        
        "checker.calculate_Similarity(user.points)"
        """if serializer.is_valid(): # 생성한 모델과 일치하면
            serializer.save() # 데이터 저장
            return JsonResponse(serializer.data, status=201) # 정상 응답 201
        return JsonResponse(serializer.errors, status=400) # 모델에 일치하지 않는 데이터일 경우"""