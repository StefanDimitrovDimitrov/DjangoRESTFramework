Content:
    * Media Files - Basics settings 
    * Upload picture
    * Upload file
    * Privet/Public files
    * Download link
________________________________________________________________
#MEDIA FILES

    - What are media files?

        * pictures : JPEG, GIF, TIFF, BMP
        * music: AAC, MP3, WAV, WMA, DOLBY DIGITAL, DTS
        * audios
        * videos: MPEG-1, MPEG-2, MPEG-4, AVI, MOV, AVCHD, H.264, H.265, Hvid
        * documents
            


    - The pillow library (Python Imaging Library)
        * free library
        * support opening, manipulating, saving many different image file formats
        * file formats: PPM, PNG, JPEG, GIF, TIFF, BMP
        
        * PIL is older version of pillow
        * inatstalation: pip install pillow( if we have PIL install we have to uninstall it)

    - Static Files
        * STATIC_URL = '/static/'
        * STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static'),
        ]
    - Media Files in Django

        * Uploading images
            - {% load static %}
            
            - {% static './css/style.css' %}

            - in the form in the html we have to add enctype="multipart/form-data"

            - urlpatterns - 'resources/<path:path_tofile>'
        
        * Uploading documents
__________________________________________________________________________
#Configuration Steps

    [] in Settings file add:
        MEDIA_URL = '/media/'
        MEDIA_ROOT = join(BASE_DIR, 'media/')
    
    [] urlPatterns
        * +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    [] in Models

        * image = models.ImageField(upload_to='pythons',)

    [] Pillow
        * pip install pillow

    [] add to the form:
        * enctype="multipart/form-data"

    [] update form:
        forms.FileInput

    [] in the videw def:
        form = PythonCreateForm(request.POST,request.FILES)

______________________________________________________________________
1. Settings: MEDIA_URL, MEDIA_ROOT
2. UrlPatterns: +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
3. Models: image = models.ImageField(upload_to='pythons',)
4. Install Pillow
5. html/form: enctype="multipart/form-data"
6. Form: forms.FileInput
7. Views: form = PythonCreateForm(request.POST,request.FILES)
