from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from api import models

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"

class CourseDetailSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source='course.title')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')

    recommends = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        # fields = "__all__"
        # depth = 2
        fields = ['course', 'title', 'img', 'slogon', 'why', 'level', 'recommends', 'chapter']

    def get_recommends(self, obj):
        # 获取推荐的所有课程
        queryset = obj.recommand_courses.all()
        return [{'id': row.id, 'title': row.title} for row in queryset]

    def get_chapter(self, obj):
        # 获取章节
        queryset = obj.course.chapter_set.all()
        return [{'id': row.id, 'name': row.name} for row in queryset]
# class Course(APIView):
#
#     def get(self, request, *args, **kwargs):
#
#         ret = {
#             'code': 1000,
#             'data': None,
#         }
#         pk = kwargs.get('pk')
#
#         try:
#             if pk:
#                 course_detail = models.Course.objects.filter(id=pk).first()
#                 ser = CourseSerializers(instance=course_detail, many=False)
#             else:
#                 courses = models.Course.objects.all()
#                 ser = CourseSerializers(instance=courses, many=True)
#             ret['data'] = ser.data
#         except Exception as e:
#             ret['code'] = 1001
#             ret['error'] = '获取数据失败'
#
#         return Response(ret)

from rest_framework import viewsets
class CourseView(viewsets.ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            courses = models.Course.objects.all()
            ser = CourseSerializers(instance=courses, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程列表失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            course_detail = models.CourseDetail.objects.filter(course_id=pk).first()
            ser = CourseDetailSerializers(instance=course_detail, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)