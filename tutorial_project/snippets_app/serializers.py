from rest_framework import serializers
from snippets_app.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


"""
    A serializer class is very similar to a Django Form class, and includes similar 
    validation flags on the various fields, such as required, max_length and default.
    The field flags can also control how the serializer should be displayed in certain 
    circumstances, such as when rendering to HTML. The {'base_template': 'textarea.html'} 
    flag above is equivalent to using widget=widgets.Textarea on a Django Form class. 
    This is particularly useful for controlling how the browsable API should be displayed.

    We can also serialize querysets instead of model instances. To do so we simply add a 
    many=True flag to the serializer arguments.

    When using modelSerializers, we can print a representation of them in the shell using
    print(repr(serializer))
"""

# class SnippetSerializer(serializers.Serializer):
#     """
#         Defines the fields to be serialized and/or deserialized
#     """
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


#     def create(self, validated_data):
#         """
#             Create and return a new `Snippet` instance, given the validated data
#         """

#         return Snippet.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         """
#             Update and return existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


# Class Based Serializer saves rewriting out the model data again

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        
