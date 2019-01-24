from rest_framework import serializers


class CoreSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(CoreSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CoreModelSerializer(CoreSerializer):
    """
    Serializer defining the nesting for the created_by and modified_by users. Additionally
    allowing to specify fields to be defined when serializer is instantiated.
    """

    created_by = serializers.ReadOnlyField()
    modified_by = serializers.ReadOnlyField()
