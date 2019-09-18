from django.core.urlresolvers import reverse
import functools
from hfu_cms.models import UserManagement, Stage
from django.http import HttpResponseRedirect
from models import NewsFeed
from django.db.models import Q
from django.contrib.auth.models import User


#############################################################
#  Decorator for News check                                 #
#                                                           #
#############################################################


def check_news_login(method):
    @functools.wraps(method)
    def wrapper(request, *args, **kwargs):
        if request.user.id and not request.user.is_superuser:
            user_access = UserManagement.objects.get(user_id=request.user.id)
            # where does user come from?!
            if user_access.is_news or user_access.is_news_reviewer:
                return method(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse("users-logout"))
        else:
            return method(request, *args, **kwargs)

    return wrapper

#############################################################
#  Decorator for News Publisher check                       #
#                                                           #
#############################################################


def publisher_permission(method):
    @functools.wraps(method)
    def wrapper(request, *args, **kwargs):
        if request.user.id and not request.user.is_superuser:
            user_access = UserManagement.objects.get(user_id=request.user.id)
            # Check user is publisher
            if user_access.is_publisher:
                return method(request,*args, **kwargs)
            else:
                return HttpResponseRedirect(reverse("users-logout"))
        else:
            return method(request, *args, **kwargs)
    return wrapper

#############################################################
#  Function for filter                                      #
#                                                           #
#############################################################


def filter_func(request, news_type):
    stage_filter = False
    news_caller_filter = False
    news_reviewer_filter = False
    publisher_filter = False
    try:
        stage_id_data = request.GET.get('stage_da')
        if stage_id_data:
            stage_filter = int(stage_id_data)
    except:
        stage_id_data = None
    try:
        news_caller_id = request.GET.get('user_da')
        if news_caller_id:
            news_caller_filter = int(news_caller_id)
    except:
        news_caller_id = None
    try:
        news_rev_id = request.GET.get('user_rev')
        if news_rev_id:
            news_reviewer_filter = int(news_rev_id)
    except:
        news_rev_id = None
    try:
        publish_id = request.GET.get('user_pub')
        if publish_id:
            publisher_filter = int(publish_id)
    except:
        publish_id = None

    if stage_id_data:
        if news_caller_id:
            objects = NewsFeed.objects.filter(
                Q(news_type=news_type) & Q(stage_id=stage_filter) & Q(current_user_id=news_caller_filter))
        elif news_rev_id:
            objects = NewsFeed.objects.filter(
                Q(news_type=news_type) & Q(stage_id=stage_filter) & Q(current_user_id=news_reviewer_filter))
        elif publish_id:
            objects = NewsFeed.objects.filter(
                Q(news_type=news_type) & Q(stage_id=stage_filter) & Q(current_user_id=publisher_filter))
        else:
            objects = NewsFeed.objects.filter(Q(news_type=news_type) & Q(stage_id=stage_filter))
        return objects, stage_filter, news_caller_filter, news_reviewer_filter, publisher_filter
    elif news_caller_id:
        objects = NewsFeed.objects.filter(Q(news_type=news_type) & Q(current_user_id=news_caller_filter))
        return objects, stage_filter, news_caller_filter, news_reviewer_filter, publisher_filter
    elif news_rev_id:
        objects = NewsFeed.objects.filter(Q(news_type=news_type) & Q(current_user_id=news_reviewer_filter))
        return objects, stage_filter, news_caller_filter, news_reviewer_filter, publisher_filter
    elif publish_id:
        objects = NewsFeed.objects.filter(Q(news_type=news_type) & Q(current_user_id=publisher_filter))
        return objects, stage_filter, news_caller_filter, news_reviewer_filter, publisher_filter
    else:
        objects = NewsFeed.objects.filter(Q(news_type=news_type))
    return objects, stage_filter, news_caller_filter, news_reviewer_filter, publisher_filter


#############################################################
#  Function for filter Checking Condition                   #
#                                                           #
#############################################################


def check_filter_only(request):
    try:
        stage_id_data = request.GET.get('stage_da')

    except:
        stage_id_data = None
    try:
        news_caller_id = request.GET.get('user_da')
    except:
        news_caller_id = None
    try:
        news_rev_id = request.GET.get('user_rev')
    except:
        news_rev_id = None
    try:
        publish_id = request.GET.get('user_pub')
    except:
        publish_id = None
    if stage_id_data and news_caller_id and news_rev_id and publish_id:
        return False
    elif news_caller_id and news_rev_id and publish_id:
        return False
    elif news_rev_id and publish_id:
        return False
    elif news_caller_id and publish_id:
        return False
    elif news_caller_id and news_rev_id:
        return False
    elif stage_id_data and news_caller_id and news_rev_id:
        return False
    elif stage_id_data and news_caller_id and publish_id:
        return False
    elif stage_id_data and news_rev_id and publish_id:
        return False
    else:
        return True


#############################################################
#  Function for checking  unblock and block condition       #
#                                                           #
#############################################################


def check_block_unblock(news_id):
    objects = NewsFeed.objects.filter(pk=news_id)
    if objects[0].blocked_news is False:
        return objects, False
    else:
        return objects, True

################################################################
# User data for news_caller, news_reviewer and publisher       #
#                                                              #
################################################################


def user_data_for_news():
    users_objects = User.objects.all()
    objects = UserManagement.objects.all()
    news_caller_data = objects.filter(is_news=True).values('user_id')
    news_caller_data = users_objects.filter(id__in=news_caller_data, is_active=True)
    news_reviewer_data = objects.filter(Q(is_news_reviewer=True) or Q(is_news=True)).values('user_id')
    news_reviewer_data = users_objects.filter(id__in=news_reviewer_data, is_active=True)
    publisher_data = objects.filter(is_publisher=True).values('user_id')
    publisher_data = users_objects.filter(id__in=publisher_data, is_active=True)
    return news_caller_data,news_reviewer_data, publisher_data

################################################################
# Getting news data for Publisher                              #
#                                                              #
################################################################


def getting_news_publisher_data(request, news_type):
    objects = NewsFeed.objects.filter(Q(current_user_id=request.user.id) & Q(news_type_id=news_type) & Q(blocked_news=False) & Q(activation_status=True)).order_by('topic_title')

    return objects, Stage.objects.all()[3:]

""" Providers Decorator """
#############################################################
#  Decorator for provider Publisher check                   #
#                                                           #
#############################################################


def providers_permission(method):
    @functools.wraps(method)
    def wrapper(request, *args, **kwargs):
        if request.user.id and not request.user.is_superuser:
            user_access = UserManagement.objects.get(user_id=request.user.id)
            # Check user is publisher
            if user_access.is_service_plan or user_access.is_service_reviewer:
                return method(request,*args, **kwargs)
            else:
                return HttpResponseRedirect(reverse("users-logout"))
        else:
            return method(request, *args, **kwargs)
    return wrapper

""" End """