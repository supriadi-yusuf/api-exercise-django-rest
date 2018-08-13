from rest_framework import serializers
from .models import Language

#class LanguageSerializer(serializers.ModelSerializer):
class LanguageListSerializer(serializers.HyperlinkedModelSerializer):

    # spd : we need to put this line of code if we want to display url when name space is used in apps
    # spd : format for view_name is namespace:xxxx-detail
    # spd : in this case, name space is languages_app
    url = serializers.HyperlinkedIdentityField(view_name='languages_app:language-detail')

    class Meta:
        model = Language # spd : model that we want to convert into JSON format with this serializer
        # fields = [ 'id', 'name', 'paradigm'] # spd : fields that we want to display
        fields = [ 'id', 'url', 'name'] # spd : fields that we want to display
        # fields = [ 'id', 'url', 'name', 'paradigm'] # spd : fields that we want to display

class LanguageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language # spd : model that we want to convert into JSON format with this serializer
        fields = [ 'id', 'name', 'paradigm'] # spd : fields that we want to display
