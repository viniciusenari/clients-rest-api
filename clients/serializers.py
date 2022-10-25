from rest_framework import serializers
from clients.models import Client
from clients.validators import valid_name, valid_phone_number, valid_ssn

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    
    def validate(self, data):
        if not valid_ssn(data['ssn']):
            raise serializers.ValidationError({'ssn':'SSN must be 9 digits'})
        if not valid_name(data['name']):
            raise serializers.ValidationError({'name':'Name must be letters only'})
        if not valid_phone_number(data['phone']):
            raise serializers.ValidationError({'phone':'Invalid phone number, must be in format 123-456-7890'})
        return data