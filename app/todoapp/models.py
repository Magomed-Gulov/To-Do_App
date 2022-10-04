from email.policy import default
from django.utils import timezone
from django.db import models

import datetime


class TodoListItem( models.Model ):
    content = models.TextField(  )
    pub_data = models.DateTimeField( auto_now=False, default=timezone.now )
    # print( timezone.now( ) )
    status = models.BooleanField( default=False )

    # def was_published_recently( self ):
    #     now = timezone.now(  )
    #     return now - datetime.timedelta( days=1 ) <= self.pub_date <= now