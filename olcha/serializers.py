from rest_framework import serializers

from olcha.models import Category, Image, Group


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'is_primary']


class GroupModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'group_name', 'image']

    def get_image(self, instance):
        image = Image.objects.filter(group=instance, is_primary=True).first()

        if image:
            serializer = ImageSerializer(image)
            return serializer.data.get('image')
        return None


class CategoryModelSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many=True, read_only=True, source='category_images')
    category_image = serializers.SerializerMethodField(method_name='foo')
    groups = GroupModelSerializer(many=True, read_only=True)

    def foo(self, instance):
        image = Image.objects.filter(category=instance, is_primary=True).first()

        if image:
            serializer = ImageSerializer(image)
            return serializer.data.get('image')
        return None

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'slug', 'category_image', 'groups']

# class GroupSerializer(serializers.ModelSerializer):
#     category_name = serializers.CharField(source='category.category_name')
#     category_id = serializers.IntegerField(source='category.id')
#
#     image = serializers.SerializerMethodField()
#
#     def get_image(self, instance):
#         image = Image.objects.filter(group=instance, is_primary=True).first()
#
#         if image:
#             serializer = ImageSerializer(image)
#             return serializer.data.get('image')
#         return None
#
#     class Meta:
#         model = Group
#         fields = ['id', 'group_name', 'slug', 'category_name', 'category_id', 'image']
