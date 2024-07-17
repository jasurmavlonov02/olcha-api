from rest_framework import serializers

from olcha.models import Category, Image, Group, Product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'is_primary', 'product', 'group', 'category']


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
        request = self.context.get('request')
        if image:
            image_url = image.image.url
            return request.build_absolute_uri(image_url)

        return None

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'slug', 'category_image', 'groups']


class ProductSerializer(serializers.ModelSerializer):
    group = GroupModelSerializer(many=False, read_only=True)
    # group_name = serializers.CharField(source='group.group_name', read_only=True)
    category_name = serializers.CharField(source='group.category.category_name', read_only=True)
    primary_image = serializers.SerializerMethodField()
    all_images = serializers.SerializerMethodField()

    def get_all_images(self, instance):
        images = Image.objects.all().filter(product=instance)
        all_images = []
        request = self.context.get('request')

        for image in images:
            all_images.append(request.build_absolute_uri(image.image.url))

        return all_images

    def get_primary_image(self, instance):
        image = Image.objects.filter(product=instance, is_primary=True).first()
        request = self.context.get('request')
        if image:
            image_url = image.image.url
            return request.build_absolute_uri(image_url)

    class Meta:
        model = Product
        fields = '__all__'

        extra_fields = ['category_name', 'primary_image', 'group', 'all_images']
