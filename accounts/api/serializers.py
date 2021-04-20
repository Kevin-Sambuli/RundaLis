from rest_framework import serializers
from accounts.models import Account


class RegistrationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = []