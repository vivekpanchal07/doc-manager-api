from django.urls import path, include

urlpatterns = [
    path("auth/", include("accounts.urls")),
    # path("documents/", include("documents.urls")),  ← later
]
