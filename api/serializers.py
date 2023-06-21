import re

from rest_framework import serializers

from .models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    search_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Dictionary
        fields = ("id","label","description","search_count")

    # Custom Validations
    def validate(self, data):
        label = data.get("label","")
        if (len(label) <= 0) or (label=="") or (len(label) < 3):
            raise serializers.ValidationError("Please enter a valid label name")  
        
        pattern = "^[A-Za-z]+$"
        if not re.match(pattern, label):
            raise serializers.ValidationError("Label name should not contain characters other then alphabets")  
        
        return data