from rest_framework import viewsets

from tests.testapp.models import Book, Course, Student
from tests.testapp.serializers import (
	BookSerializer, CourseSerializer, StudentSerializer,
	CourseWithFieldsKwargSerializer, CourseWithExcludeKwargSerializer,
	CourseWithReturnPkkwargSerializer, ReplaceableStudentSerializer,
	WritableStudentSerializer, WritableCourseSerializer,
	ReplaceableCourseSerializer, CourseWithAliasedBooksSerializer,
	CourseWithDynamicSerializerMethodField, StudentWithAliasSerializer
)
from django_restql.mixins import EagerLoadingMixin


#### ViewSets for Data Querying And Mutations Testing ####
class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
	serializer_class = CourseSerializer
	queryset = Course.objects.all()


############# ViewSets For Data Querying Testing #############
class CourseWithReturnPkkwargViewSet(viewsets.ModelViewSet):
	serializer_class = CourseWithReturnPkkwargSerializer
	queryset = Course.objects.all()


class CourseWithFieldsKwargViewSet(viewsets.ModelViewSet):
	serializer_class = CourseWithFieldsKwargSerializer
	queryset = Course.objects.all()


class CourseWithExcludeKwargViewSet(viewsets.ModelViewSet):
	serializer_class = CourseWithExcludeKwargSerializer
	queryset = Course.objects.all()


class CourseWithAliasedBooksViewSet(viewsets.ModelViewSet):
	serializer_class = CourseWithAliasedBooksSerializer
	queryset = Course.objects.all()


class CourseWithDynamicSerializerMethodFieldViewSet(viewsets.ModelViewSet):
	serializer_class = CourseWithDynamicSerializerMethodField
	queryset = Course.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()


class StudentEagerLoadingViewSet(EagerLoadingMixin, viewsets.ModelViewSet):
	serializer_class = StudentWithAliasSerializer
	queryset = Student.objects.all()
	select_related = {
		"program": "course"
	}
	prefetch_related = {
		"phone_numbers": "phone_numbers",
		"program.books": "course__books"
	}


######### ViewSets For Data Mutations Testing ##########
class WritableCourseViewSet(viewsets.ModelViewSet):
	serializer_class = WritableCourseSerializer
	queryset = Course.objects.all()


class ReplaceableCourseViewSet(viewsets.ModelViewSet):
	serializer_class = ReplaceableCourseSerializer
	queryset = Course.objects.all()


class ReplaceableStudentViewSet(viewsets.ModelViewSet):
	serializer_class = ReplaceableStudentSerializer
	queryset = Student.objects.all()


class WritableStudentViewSet(viewsets.ModelViewSet):
	serializer_class = WritableStudentSerializer
	queryset = Student.objects.all()
