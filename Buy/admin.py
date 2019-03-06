from django.contrib import admin
from Buy.models import User, Stadium, Ticket, RemainingTickets,Match
# Register your models here.

#username- lukky
#password- lukky
admin.site.register(User)
admin.site.register(Stadium)
admin.site.register(Ticket)
admin.site.register(RemainingTickets)
admin.site.register(Match)
