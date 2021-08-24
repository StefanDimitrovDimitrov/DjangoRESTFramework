# what is Django REST framework


1. What is restful Apis - a way to transfer infomration between an interface and a database in a simple way

2. Difference between Put and Patch - Put change the whole row in a db and putch change only one value in the row for example age of a person

3. What is serializers - Serializers help us to convert JSON in ORM object and object in JSON type data. 
    
        * create new python file serializers

            ```
            class BookSerializer(serializers.ModelSerializer):
            class Meta:
            model = BookModel
            fields = "__all__"
            
            ```
        * in view files
            ```
            class BookListCreate(APIView):
                def get(self, request):
                    books = BookModel.objects.all()
                    serializer = BookSerializer(books, many=True)
                    return Response(serializer.data)
            ```

            - create method get
            - take all books(objects)
            - give as a param to the serializer wih option many=True if they are more then one
            - return serializer object .data

                def post(self.request)"

                - get data = BookSerializer(data=request.data)
                - check if it is valid()
                - save()
                - return Response(serializer.data, status)
                -if not valid return Response(serialize.error, status)

4. For additional validation we have to rewrite in the serializer the validator method example below

    
                