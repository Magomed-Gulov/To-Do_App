from django.utils import timezone
from django.db import models

import datetime


class TodoListItem( models.Model ):
    content = models.TextField(  )
    pub_data = models.DateTimeField( auto_now=False, default=timezone.now )
    
    status = models.BooleanField( default=False )
    email = models.EmailField( max_length=30 )

    # def was_published_recently( self ):
    #     now = timezone.now(  )
    #     return now - datetime.timedelta( days=1 ) <= self.pub_date <= now