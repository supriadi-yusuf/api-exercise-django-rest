from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language # spd : model that we want to convert into JSON format with this serializer
        fields = [ 'id', 'name', 'paradigm'] # spd : fields that we want to display
