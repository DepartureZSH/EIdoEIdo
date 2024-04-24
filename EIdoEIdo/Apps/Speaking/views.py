from . import models
from . import Serializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class Practice_getTopic1(APIView):
    def get(self, pk):
        if pk == 0:
            # 无条件|随机获取3个Topics（3[Topic1]）
            return
        else:
            # 通过用户.id|获取自定义IELTS1语料Topic列表（all[user_Topic1]）
            # 在自定义列表中随机获取3个Topics（3[Topic1]）
            return

class Practice_getCorpus1(APIView):
    def get(self, pk):
        # 通过Topic_id|获取该id下所有语料信息（n[IELTS1]）
        return

class Practice_getTopic23(APIView):
    def get(self, pk):
        if pk == 0:
            # 无条件|随机获取1个Topics（3[Topic2&3]）
            return
        else:
            # 通过用户.id|获取自定义IELTS2&3语料Topic列表（all[user_Topic2&3]）
            # 在自定义列表中随机获取1个Topics（[Topic2&3]）
            return

class Practice_getCorpus2(APIView):
    def get(self, pk):
        # 通过Topic_id|获取该id下所有语料信息（[IELTS2]）
        return

class Practice_getCorpus3(APIView):
    def get(self, pk):
        # 通过Topic_id|获取该id下所有语料信息（n[IELTS3]）
        return

class Practice_getTopic(APIView):
    def get(self, pk):
        if pk == 0:
            # 无条件|随机获取1个Topics（[Topic]）
            return
        else:
            # 通过用户.id|获取自定义QuickTest语料Topic列表（all[user_Topic]）
            # 在自定义列表中随机获取1个Topics（[Topic]）
            return

class Practice_getCorpus(APIView):
    def get(self, pk):
        # 通过Topic_id|获取该id下所有语料信息（n[QuickTest]）
        return

class Corpus_getTopic1(APIView):
    def get(self, pk):
        if pk == 0:
            # 返回未登录禁止访问
            return
        else:
            # 通过用户.id|获取自定义IELTS1语料Topic列表（all[user_Topic1]），
            # 无条件| 获取所有IELTS1语料Topic列表（all[Topic1]）
            return

    def post(self, pk):
        # 通过用户.id|上传自定义IELTS1语料Topic列表
        return

class Corpus_getTopic23(APIView):
    def get(self, pk):
        if pk == 0:
            # 返回未登录禁止访问
            return
        else:
            # 通过用户.id|获取自定义IELTS2&3语料Topic列表（all[user_Topic2&3]），
            # 无条件| 获取所有IELTS2&3语料Topic列表（all[Topic2&3]）
            return

    def post(self, pk):
        # 通过用户.id|上传自定义IELTS2&3语料Topic列表
        return

class Corpus_getTopic(APIView):
    def get(self, pk):
        if pk == 0:
            # 返回未登录禁止访问
            return
        else:
            # 通过用户.id|获取自定义QuickTest语料Topic列表（all[user_Topic]）
            # 无条件| 获取所有QuickTest语料Topic列表（all[Topic]）
            return

    def post(self, pk):
        # 通过用户.id|上传自定义QuickTest语料Topic列表
        return

# class IELTS1CreateAPI(APIView):
#     # 定义 GET 请求的方法，内部实现相同 @api_view
#     def delete(self, request):
#         try:
#             models.IELTS1Topics.objects.all().delete()
#             return Response(data={"message": ["IELTS1 delete ok!"], "code": "200"}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(data={"message": [f"IELTS1 delete not ok! Because {str(e)}"], "code": "200"},
#                             status=status.HTTP_200_OK)
#
#     def post(self, request):
#         ############################################
#         # 业务逻辑
#         ############################################
#         try:
#             f1 = open("E:\python_project\EIdoEIdoWeb\Backup\\topics_new.txt", "r")
#             topics_new = f1.readlines()
#             topics_new = [each.strip('\n') for each in topics_new]
#
#             f2 = open("E:\python_project\EIdoEIdoWeb\Backup\\topics_old.txt", "r")
#             topics_old = f2.readlines()
#             topics_old = [each.strip('\n') for each in topics_old]
#
#             f3 = open("E:\python_project\EIdoEIdoWeb\Backup\\questions_new.txt", "r")
#             questions_new = f3.readlines()
#             questions_new = [each.strip('\n') for each in questions_new]
#
#             f4 = open("E:\python_project\EIdoEIdoWeb\Backup\\questions_old.txt", "r")
#             questions_old = f4.readlines()
#             questions_old = [each.strip('\n') for each in questions_old]
#
#             i = 0
#             IELTS1Topics = models.IELTS1Topics(Topic=topics_new[i], IsOld=False)
#             IELTS1Topics.save()
#             for each in questions_new:
#                 if each == '':
#                     i += 1
#                     IELTS1Topics = models.IELTS1Topics(Topic=topics_new[i], IsOld=False)
#                     IELTS1Topics.save()
#                 else:
#                     question = models.IELTS1(Question=each)
#                     question.Topic = IELTS1Topics
#                     question.save()
#             i = 0
#             IELTS1Topics = models.IELTS1Topics(Topic=topics_old[i], IsOld=True)
#             IELTS1Topics.save()
#             for each in questions_old:
#                 if each == '':
#                     i += 1
#                     IELTS1Topics = models.IELTS1Topics(Topic=topics_old[i], IsOld=True)
#                     IELTS1Topics.save()
#                 else:
#                     question = models.IELTS1(Question=each)
#                     question.Topic = IELTS1Topics
#                     question.save()
#             return Response(data={"message": ["IELTS1 Create ok!"], "code": "200"}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(data={"message": [f"IELTS1 Create not ok! Because {str(e)}"], "code": "200"}, status=status.HTTP_200_OK)
#
# class IELTS2_3CreateAPI(APIView):
#     # 定义 GET 请求的方法，内部实现相同 @api_view
#     def delete(self, request):
#         try:
#             models.IELTS23Topics.objects.all().delete()
#             return Response(data={"message": ["IELTS1 delete ok!"], "code": "200"}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(data={"message": [f"IELTS1 delete not ok! Because {str(e)}"], "code": "200"},
#                             status=status.HTTP_200_OK)
#
#     def post(self, request):
#         ############################################
#         # 业务逻辑
#         ############################################
#         try:
#             f = open("E:\python_project\EIdoEIdoWeb\Backup\\topics23_new.txt", "r", encoding='utf-8', errors='ignore')
#             topics_new = f.readlines()
#             topics_new = [each.strip('\n') for each in topics_new]
#             f.close()
#
#             f = open("E:\python_project\EIdoEIdoWeb\Backup\\topics23_old.txt", "r", encoding='utf-8', errors='ignore')
#             topics_old = f.readlines()
#             topics_old = [each.strip('\n') for each in topics_old]
#             f.close()
#
#             f = open("E:\python_project\EIdoEIdoWeb\Backup\\questions2_new.txt", "r", encoding='utf-8', errors='ignore')
#             questions2_new = f.readlines()
#             questions2_new = [each.strip('\n') for each in questions2_new]
#             f.close()
#
#             f = open("E:\python_project\EIdoEIdoWeb\Backup\\questions2_old.txt", "r", encoding='utf-8', errors='ignore')
#             questions2_old = f.readlines()
#             questions2_old = [each.strip('\n') for each in questions2_old]
#             f.close()
#
#             f = open("E:\python_project\EIdoEIdoWeb\Backup\\questions3_new.txt", "r", encoding='utf-8', errors='ignore')
#             questions3_new = f.readlines()
#             questions3_new = [each.strip('\n') for each in questions3_new]
#             f.close()
#
#             f = open("E:\python_project\EIdoEIdoWeb\Backup\\questions3_old.txt", "r", encoding='utf-8', errors='ignore')
#             questions3_old = f.readlines()
#             questions3_old = [each.strip('\n') for each in questions3_old]
#             f.close()
#
#             i = 0
#             j = 0
#             k = 0
#             while i < len(topics_new):
#                 question = questions2_new[j]
#                 print(f"topic:{topics_new[i]}\tquestion2:\t", question)
#                 IELTS23Topics = models.IELTS23Topics(Topic=topics_new[i], IsOld=False)
#                 IELTS23Topics.save()
#                 j += 1
#                 requirement = ""
#                 while j < len(questions2_new) and questions2_new[j] != '':
#                     requirement += questions2_new[j] + '\n'
#                     j += 1
#                 print("requirement:\n", requirement)
#                 question = models.IELTS2(Question=question, Requirement=requirement)
#                 question.Topic = IELTS23Topics
#                 question.save()
#                 while k < len(questions3_new) and questions3_new[k] != '':
#                     question = questions3_new[k]
#                     print(f"topic:{topics_new[i]}\tquestion3:\t", question)
#                     question = models.IELTS3(Question=question)
#                     question.Topic = IELTS23Topics
#                     question.save()
#                     k += 1
#                 i += 1
#                 j += 1
#                 k += 1
#                 print()
#
#             i = 0
#             j = 0
#             k = 0
#             while i < len(topics_old):
#                 question = questions2_old[j]
#                 print(f"topic:{topics_old[i]}\tquestion2:\t", question)
#                 IELTS23Topics = models.IELTS23Topics(Topic=topics_old[i], IsOld=True)
#                 IELTS23Topics.save()
#                 j += 1
#                 requirement = ""
#                 while j < len(questions2_old) and questions2_old[j] != '':
#                     requirement += questions2_old[j] + '\n'
#                     j += 1
#                 print("requirement:\n", requirement)
#                 question = models.IELTS2(Question=question, Requirement=requirement)
#                 question.Topic = IELTS23Topics
#                 question.save()
#                 while k < len(questions3_old) and questions3_old[k] != '':
#                     question = questions3_old[k]
#                     print(f"topic:{topics_old[i]}\tquestion3:\t", question)
#                     question = models.IELTS3(Question=question)
#                     question.Topic = IELTS23Topics
#                     question.save()
#                     k += 1
#                 i += 1
#                 j += 1
#                 k += 1
#                 print()
#             # for each in questions2_new:
#             #     if each == '':
#             #         i += 1
#             #         print(topics_new[i], " IsOld=False")
#             #     else:
#             #         print(each, " Topic={}".format(topics_new[i]))
#             #
#             # i = 0
#             # print(topics_new[i], " IsOld=False")
#             # for each in questions3_new:
#             #     if each == '':
#             #         i += 1
#             #         print(topics_new[i], " IsOld=False")
#             #     else:
#             #         print(each, " Topic={}".format(topics_new[i]))
#         #     i = 0
#         #     IELTS23Topics = models.IELTS23Topics(Topic=topics_new[i], IsOld=False)
#         #     IELTS23Topics.save()
#         #     for each in questions2_new:
#         #         if each == '':
#         #             i += 1
#         #             IELTS1Topics = models.IELTS1Topics(Topic=topics_new[i], IsOld=False)
#         #             IELTS1Topics.save()
#         #         else:
#         #             question = models.IELTS1(Question=each)
#         #             question.Topic = IELTS1Topics
#         #             question.save()
#         #     i = 0
#         #     IELTS1Topics = models.IELTS1Topics(Topic=topics_old[i], IsOld=True)
#         #     IELTS1Topics.save()
#         #     for each in questions_old:
#         #         if each == '':
#         #             i += 1
#         #             IELTS1Topics = models.IELTS1Topics(Topic=topics_old[i], IsOld=True)
#         #             IELTS1Topics.save()
#         #         else:
#         #             question = models.IELTS1(Question=each)
#         #             question.Topic = IELTS1Topics
#         #             question.save()
#             return Response(data={"message": ["IELTS2 Create ok!"], "code": "200"}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(data={"message": [f"IELTS2 Create not ok! Because {str(e)}"], "code": "200"}, status=status.HTTP_200_OK)
#
# class IELTS3CreateAPI(APIView):
#     # 定义 GET 请求的方法，内部实现相同 @api_view
#     def post(self, request):
#         ############################################
#         # 业务逻辑
#         ############################################
#
#         return Response(data={"message": ["IELTS3 Create ok!"], "code": "200"}, status=status.HTTP_200_OK)
#
# class IELTS1TopicsAPI(APIView):
#
#     # 定义 GET 请求的方法，内部实现相同 @api_view
#     def get(self, request, pk):
#         ############################################
#         # 业务逻辑
#         ############################################
#         # permission_classes = [IsAuthenticatedOrReadOnly]
#         IELTS1NewTopics = models.IELTS1Topics.objects.filter(IsOld=False).order_by('?')[:2]
#         IELTS1OldTopics = models.IELTS1Topics.objects.filter(IsOld=True).order_by('?')[:1]
#         IELTS1Topics = IELTS1NewTopics.union(IELTS1OldTopics)
#         serializer = Serializer.IELTS1TopicsSerializer(IELTS1Topics, many=True)
#         # IELTS1 = models.IELTS1.objects.all()
#         # serializer = Serializer.IELTS1Serializer(IELTS1, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class IELTS1API(APIView):
#     # 定义 GET 请求的方法，内部实现相同 @api_view
#     def get(self, request, pk):
#         ############################################
#         # 业务逻辑
#         ############################################
#         # permission_classes = [IsAuthenticatedOrReadOnly]
#         IELTS1 = models.IELTS1.objects.filter(Topic=pk)
#         serializer = Serializer.IELTS1Serializer(IELTS1, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class IELTS23API(APIView):
#     # 定义 GET 请求的方法，内部实现相同 @api_view
#     def get(self, request, pk):
#         ############################################
#         # 业务逻辑
#         ############################################
#         # permission_classes = [IsAuthenticatedOrReadOnly]
#         IELTS23Topics = models.IELTS23Topics.objects.all().order_by('?')[:1]
#         serializer = Serializer.IELTS23TopicsSerializer(IELTS23Topics, many=True)
#         # IELTS1 = models.IELTS1.objects.all()
#         # serializer = Serializer.IELTS1Serializer(IELTS1, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class IELTS2API(APIView):
#
#     # 定义 GET 请求的方法，内部实现相同 @api_view
#     def get(self, request, pk):
#         ############################################
#         # 业务逻辑
#         ############################################
#         # permission_classes = [IsAuthenticatedOrReadOnly]
#         IELTS2 = models.IELTS2.objects.filter(Topic=pk)
#         serializer = Serializer.IELTS2Serializer(IELTS2, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class IELTS3API(APIView):
#
#     # 定义 GET 请求的方法，内部实现相同 @api_view
#     def get(self, request, pk):
#         ############################################
#         # 业务逻辑
#         ############################################
#         # permission_classes = [IsAuthenticatedOrReadOnly]
#         IELTS3 = models.IELTS3.objects.filter(Topic=pk)
#         serializer = Serializer.IELTS3Serializer(IELTS3, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
