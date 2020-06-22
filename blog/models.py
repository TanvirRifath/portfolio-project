from django.db import models

# Create A Blog model
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#Add the blog app to the settings
    #copy the classname from apps.py and add that app to installed apps list in main settings.py file
#create a migration
    #go to command prompt and type "manage.py makemigrations". This makes the new model ready for migration
#Migrate
    #Go to command prompt and type "manage.py migrate"
#Add to the admin
    #paste the same lines we have written in admin.py in jobs model to this blog model's admin.py
