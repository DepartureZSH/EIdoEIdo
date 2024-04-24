# from . import models
# from .serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse
import json

class Practice_CorpusList(APIView):
    def get(self, pk):
        if pk == 0:
            # 无条件|获取所有听力语料列表和语言文件路径
            return
        else:
            # 通过用户id|在User.model获取用户听力语料列表，
            # 在Listening.model获取语言文件路径（user_id[Name、Src_file]）
            return

class Practice_WordFile(APIView):
    def get(self, pk):
        # 通过语料.id|获取语料对应单词文件路径
        return

class Practice_reload(APIView):
    def get(self, pk):
        # 通过用户.id|获取上次的听写本、当前语料、播放断点
        return

    def post(self, pk):
        # 上传至User.Record和User.Listening，包括听写本、当前语料、播放断点，和时间戳
        return

class Corpus_CorpusList(APIView):
    def get(self, pk):
        if pk == 0:
            # 返回未登录禁止访问
            return
        else:
            # 通过用户id|获取所有的听力语料列表和用户的听力语料列表
            return

    def post(self, pk):
        # 上传至User.model，包括用户听力语料列表
        return

class IELTSWangAPI(APIView):
    # 定义 GET 请求的方法，内部实现相同 @api_view
    # def delete(self, request):
    #     try:
    #         models.IELTS1Topics.objects.all().delete()
    #         return Response(data={"message": ["IELTS1 delete ok!"], "code": "200"}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response(data={"message": [f"IELTS1 delete not ok! Because {str(e)}"], "code": "200"},
    #                         status=status.HTTP_200_OK)
    def get(self, request, pk):
        try:
            data = [
                {'title': 'Chapter3 预测试'},
                {'title': 'Chapter3 Test 1'},
                {'title': 'Chapter3 Test 2'},
                {'title': 'Chapter3 Test 3'},
                {'title': 'Chapter3 Test 4'},
                {'title': 'Chapter3 Test 5'},
                {'title': 'Chapter3 Test 6'},
                {'title': 'Chapter3 Test 7'},
                {'title': 'Chapter3 Test 8'},
                {'title': 'Chapter3 Test 9'},
                {'title': 'Chapter4 Test 1'},
                {'title': 'Chapter4 Test 2'},
                {'title': 'Chapter4 Test 3&4'},
                {'title': 'Chapter5 预测试'},
                {'title': 'Chapter5 Test 1'},
                {'title': 'Chapter5 Test 2'},
                {'title': 'Chapter5 Test 3'},
                {'title': 'Chapter5 Test 4'},
                {'title': 'Chapter5 Test 5'},
                {'title': 'Chapter5 Test 6'},
                {'title': 'Chapter5 Test 7'},
                {'title': 'Chapter5 Test 8'},
                {'title': 'Chapter5 Test 9'},
                {'title': 'Chapter5 Test 10'},
                {'title': 'Chapter5 Test 11'},
                {'title': 'Chapter5 Test 12'},
                {'title': 'Chapter11 Section 1'},
                {'title': 'Chapter11 Section 2'},
                {'title': 'Chapter11 Section 3'},
                {'title': 'Chapter11 Section 4'},
                {'title': 'Chapter11 剑15版新增部分'},
            ]
            if pk == 0:
                return Response(data={"message": data, "code": "200"}, status=status.HTTP_200_OK)
            elif pk == 1:
                return Response(data={"message": data[:5], "code": "200"}, status=status.HTTP_200_OK)
        except:
            data = [
                {'title': 'Chapter3 预测试'},
                {'title': 'Chapter3 Test 1'},
                {'title': 'Chapter3 Test 2'},
                {'title': 'Chapter3 Test 3'},
                {'title': 'Chapter3 Test 4'},
                {'title': 'Chapter3 Test 5'},
                {'title': 'Chapter3 Test 6'},
                {'title': 'Chapter3 Test 7'},
                {'title': 'Chapter3 Test 8'},
                {'title': 'Chapter3 Test 9'},
                {'title': 'Chapter4 Test 1'},
                {'title': 'Chapter4 Test 2'},
                {'title': 'Chapter4 Test 3&4'},
                {'title': 'Chapter5 预测试'},
                {'title': 'Chapter5 Test 1'},
                {'title': 'Chapter5 Test 2'},
                {'title': 'Chapter5 Test 3'},
                {'title': 'Chapter5 Test 4'},
                {'title': 'Chapter5 Test 5'},
                {'title': 'Chapter5 Test 6'},
                {'title': 'Chapter5 Test 7'},
                {'title': 'Chapter5 Test 8'},
                {'title': 'Chapter5 Test 9'},
                {'title': 'Chapter5 Test 10'},
                {'title': 'Chapter5 Test 11'},
                {'title': 'Chapter5 Test 12'},
                {'title': 'Chapter11 Section 1'},
                {'title': 'Chapter11 Section 2'},
                {'title': 'Chapter11 Section 3'},
                {'title': 'Chapter11 Section 4'},
                {'title': 'Chapter11 剑15版新增部分'},
            ]
            return Response(data={"message": data, "code": "404"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        ############################################
        # 业务逻辑
        ############################################
        try:
            f1 = open("E:\python_project\EIdoEIdoWeb\Backup\\topics_new.txt", "r")
            topics_new = f1.readlines()
            topics_new = [each.strip('\n') for each in topics_new]

            f2 = open("E:\python_project\EIdoEIdoWeb\Backup\\topics_old.txt", "r")
            topics_old = f2.readlines()
            topics_old = [each.strip('\n') for each in topics_old]

            f3 = open("E:\python_project\EIdoEIdoWeb\Backup\\questions_new.txt", "r")
            questions_new = f3.readlines()
            questions_new = [each.strip('\n') for each in questions_new]

            f4 = open("E:\python_project\EIdoEIdoWeb\Backup\\questions_old.txt", "r")
            questions_old = f4.readlines()
            questions_old = [each.strip('\n') for each in questions_old]

            i = 0
            IELTS1Topics = models.IELTS1Topics(Topic=topics_new[i], IsOld=False)
            IELTS1Topics.save()
            for each in questions_new:
                if each == '':
                    i += 1
                    IELTS1Topics = models.IELTS1Topics(Topic=topics_new[i], IsOld=False)
                    IELTS1Topics.save()
                else:
                    question = models.IELTS1(Question=each)
                    question.Topic = IELTS1Topics
                    question.save()
            i = 0
            IELTS1Topics = models.IELTS1Topics(Topic=topics_old[i], IsOld=True)
            IELTS1Topics.save()
            for each in questions_old:
                if each == '':
                    i += 1
                    IELTS1Topics = models.IELTS1Topics(Topic=topics_old[i], IsOld=True)
                    IELTS1Topics.save()
                else:
                    question = models.IELTS1(Question=each)
                    question.Topic = IELTS1Topics
                    question.save()
            return Response(data={"message": ["IELTS1 Create ok!"], "code": "200"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"message": [f"IELTS1 Create not ok! Because {str(e)}"], "code": "200"},
                            status=status.HTTP_200_OK)

class IELTSMyCorpusAPI(APIView):
    def get(self, request, pk):
        try:
            mockData = []
            originTargetKeys = ["2", "5", "8"]
            for i in range(0, 20):
                mockData.append({
                    'key': str(i),
                    'title': f'content{i + 1}',
                    'description': f'description of content{i + 1}',
                    'disabled': False,
                })
            if pk == 0:
                return Response(data={"mockData": json.dumps(mockData), "originTargetKeys": originTargetKeys, "code": "200"}, status=status.HTTP_200_OK)
            elif pk == 1:
                return Response(data={"mockData": json.dumps(mockData), "originTargetKeys": originTargetKeys, "code": "200"}, status=status.HTTP_200_OK)
        except:
            mockData = []
            originTargetKeys = ["2", "5", "8"]
            for i in range(0, 20):
                mockData.append({
                    'key': str(i),
                    'title': f'content{i + 1}',
                    'description': f'description of content{i + 1}',
                    'disabled': False,
                })
            return Response(data={"mockData": json.dumps(mockData), "originTargetKeys": originTargetKeys, "code": "400"}, status=status.HTTP_400_OK)