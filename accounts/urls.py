from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile, new_page, premium, delete_account
from accounts import url_reset

urlpatterns = [
    url(r'^new_page/', new_page, name="new_page"),
    url(r'^premium/', premium, name="premium"),
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^delete_account/', delete_account, name="delete_account")
]