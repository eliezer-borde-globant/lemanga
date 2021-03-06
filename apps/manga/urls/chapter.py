from django.conf.urls import include, url

from .. import views

CHAPTER = [
    url(r'^d/(?P<name>(\w|-)+)/(?P<chapter>\d+)/(?P<user>\d+)/(?P<number>\d+)/$',
        views.ChapterDetailView.as_view(),
        name="manga-chapter"),
    url(r'^d/(?P<name>(\w|-)+)/create/$', views.CreateChapterView.as_view(),
        name="create-chapter"),
]