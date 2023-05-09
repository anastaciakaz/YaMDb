from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryViewSet,
    CommentsViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitlesViewSet,
    TokenView,
    UserSignUpView,
    UsersViewSet,
)


class NoPutRouter(routers.DefaultRouter):
    """
    Класс роутер, отключающий PUT запросы
    """

    def get_method_map(self, viewset, method_map):

        bound_methods = super().get_method_map(viewset, method_map)

        if 'put' in bound_methods.keys():
            del bound_methods['put']

        return bound_methods


router_v1 = NoPutRouter()
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitlesViewSet)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments',
)
router_v1.register('users', UsersViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include([
        path('signup/', UserSignUpView.as_view()),
        path('token/', TokenView.as_view())
    ])),
]
