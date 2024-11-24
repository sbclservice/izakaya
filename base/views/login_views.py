from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from base.models import User


class Login1(LoginView):

    template_name = 'pages/login1.html'

    def form_valid(self, form):
        # ユーザーがログインしている場合、ログアウトを実行
        if self.request.user.is_authenticated:
            logout(self.request)

            user = User.objects.get(id=2)
            user.is_active = True
            user.save()

            # ログアウト後にログインの処理
            response = super().form_valid(form)
            return response
        
        else:
            # ログインが成功した場合の処理
            user = User.objects.get(id=2)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
    

class Login2(LoginView):

    template_name = 'pages/login2.html'

    def form_valid(self, form):
        # ユーザーがログインしている場合、ログアウトを実行
        if self.request.user.is_authenticated:
            logout(self.request)
            # ログアウト後にログインの処理

            user = User.objects.get(id=3)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
        else:
            # ログインが成功した場合の処理
            user = User.objects.get(id=3)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
    

class Login3(LoginView):

    template_name = 'pages/login3.html'

    def form_valid(self, form):
        # ユーザーがログインしている場合、ログアウトを実行
        if self.request.user.is_authenticated:
            logout(self.request)
            # ログアウト後にログインの処理

            user = User.objects.get(id=4)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
        else:
            # ログインが成功した場合の処理

            user = User.objects.get(id=4)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
    

class Login4(LoginView):

    template_name = 'pages/login4.html'

    def form_valid(self, form):
        # ユーザーがログインしている場合、ログアウトを実行
        if self.request.user.is_authenticated:
            logout(self.request)
            # ログアウト後にログインの処理

            user = User.objects.get(id=5)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
        else:
            # ログインが成功した場合の処理

            user = User.objects.get(id=5)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
    

class Login5(LoginView):

    template_name = 'pages/login5.html'

    def form_valid(self, form):
        # ユーザーがログインしている場合、ログアウトを実行
        if self.request.user.is_authenticated:
            logout(self.request)
            # ログアウト後にログインの処理

            user = User.objects.get(id=6)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
        else:
            # ログインが成功した場合の処理

            user = User.objects.get(id=6)
            user.is_active = True
            user.save()

            response = super().form_valid(form)
            return response
        
    
