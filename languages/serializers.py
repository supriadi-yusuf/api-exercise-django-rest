from rest_framework import serializers
from .models import Language, Paradigm, Programmer

#class LanguageSerializer(serializers.ModelSerializer):
class LanguageListSerializer(serializers.HyperlinkedModelSerializer):

    # spd : we need to put this line of code if we want to display url when name space is used in apps
    # spd : format for view_name is namespace:xxxx-detail
    # spd : in this case, name space is languages_app
    url = serializers.HyperlinkedIdentityField(view_name='languages_app:language-detail')

    class Meta:
        model = Language # spd : model that we want to convert into JSON format with this serializer
        # fields = [ 'id', 'name', 'paradigm'] # spd : fields that we want to display
        #fields = [ 'id', 'url', 'name'] # spd : fields that we want to display
        fields = [ 'id', 'url', 'name'] # spd : fields that we want to display

#class LanguageDetailSerializer(serializers.ModelSerializer):
class LanguageDetailSerializer(serializers.HyperlinkedModelSerializer):

    # spd : we need to put this line of code if we want to display paradigm link when name space is used in apps
    # spd : since paradigm is foreign key with one to many ( not many to many) relationship so parameter many=False
    # spd : in case of many to many relationship, parameter many=True
    #paradigm = serializers.HyperlinkedRelatedField( many=False, read_only=True, view_name='languages_app:paradigm-detail')
    paradigm = serializers.HyperlinkedRelatedField( many=False, queryset=Paradigm.objects.all(),
     view_name='languages_app:paradigm-detail')

    class Meta:
        model = Language # spd : model that we want to convert into JSON format with this serializer
        fields = [ 'id', 'name', 'paradigm'] # spd : fields that we want to display

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField( view_name='languages_app:paradigm-detail')

    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')


#class ProgrammerSerializer(serializers.ModelSerializer):
class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField( view_name='languages_app:programmer-detail')
    #languages = serializers.HyperlinkedRelatedField( many=True, read_only=True, view_name='languages_app:language-detail')
    languages = serializers.HyperlinkedRelatedField( many=True, queryset=Language.objects.all(),
     view_name='languages_app:language-detail')
    #languages = serializers.StringRelatedField( many=True)
    #languages = serializers.PrimaryKeyRelatedField( many=True, read_only=True)
    #languages = serializers.PrimaryKeyRelatedField( many=True, queryset=Language.objects.all())
    #languages = LanguageDetailSerializer( many=True, read_only=True)

    class Meta:
        model = Programmer
        fields = ( 'id', 'url', 'name', 'languages')


'''
class ProgrammerSerializer(serializers.ModelSerializer):
#class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField( view_name='languages_app:programmer-detail')
    languages = LanguageDetailSerializer( many=True)

    class Meta:
        model = Programmer
        fields = ( 'id', 'url', 'name', 'languages')

    def create(self, validated_data):
        languages_data = validated_data.pop('languages')
        programmer = Programmer.objects.create(**validated_data)
        for language_data in languages_data:
            Language.objects.create(programmer=programmer, **language_data)

        return programmer
'''
