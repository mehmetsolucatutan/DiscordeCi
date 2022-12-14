from django.urls import path
from UserApp.api import views as api_views


urlpatterns = [
    path('DiscordAcc/<int:pk>', api_views.UyeDiscordAccListCreateAPIView.as_view(), name="DiscordLog"),
    path('User/<int:pk>', api_views.UyeAPIView.as_view(), name="uye"),
    path('DeadUser/<int:pk>', api_views.UyeAccisDeadAPIView.as_view(), name="Deaduye"),
    path('UyeAccPerm/<int:pk>', api_views.UyeAccPermissionsControl.as_view(), name="UyeAccPerm"),
    path('UyeAcc/<int:discordid>/', api_views.UyeAccAPIView.as_view(), name="UyeAccPerm"),
    path('UyeAccControl/<int:discordid>/', api_views.UyeDiscordControlAPIView.as_view(), name="UyeAccControl"),
    path('logs/', api_views.UyeWalletAndAlisverisLogAPIView.as_view(), name="logs"),
]