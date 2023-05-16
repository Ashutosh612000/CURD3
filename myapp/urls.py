from django.urls import path
from myapp.views import index,delete_data,update_data,Buyer,Seller,Add_data,handleSignup,handleLogin,handleLogout

urlpatterns = [
path('',index,name='myapp'),
path('buyer',Buyer,name='buyer'),
path('delete/<int:id>/',delete_data,name="deletedata"),
path('<int:id>/',update_data,name='updatedata'),
path('seller',Seller,name='seller'),
path('adddata',Add_data,name= 'adddata'),
# path('signup',Signup,name='signup'),
path('signup',handleSignup,name='handlesignup'),
path('login',handleLogin,name='handlelogin'),
path('logout',handleLogout,name='handlelogout'),

]