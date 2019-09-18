from django.core.paginator import PageNotAnInteger, EmptyPage

from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_GET, require_POST
from hfu_cms.elasticsearch_client import *
from hfu_cms.data_publisher import *
from django.template.loader import render_to_string

""" Import from deco file """
from deco import check_news_login, check_filter_only, filter_func, check_block_unblock, user_data_for_news, \
    publisher_permission, getting_news_publisher_data

""" END deco file import """

""" Import from hfu_cms app """

from hfu_cms.check_point import edit_rights
from hfu_cms.views import paginate
from hfu_cms.models import UserManagement

""" END """
import uuid
import json
import os
from models import *
from underscore import *

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.conf import settings
import mammoth
import base64
import os
image_iterator = 0
image_file_name = ''
image_src = ''
image_alt_g=''

# Create your views here.
@check_news_login
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def news_home(request):
    return render(request, 'news/news_feed_dashboard.html', {'tab': 'news_data'})


@check_news_login
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser, login_url='/')
@require_GET
def news_management(request, type_data=None):
    if type_data is not None:
        return render(request, 'news/news_feed_2.html', {'type_data': type_data, 'tab': 'news_data'})
    else:
        messages.error(request, 'You are trying wrong data to access')
        return render(request, 'news/news_feed_dashboard.html', {'tab': 'news_data'})


##################################################################################
# Assign Start Here                                                              #
##################################################################################

####################################################################
# Name - get_assign_data                                           #
# Owner - Visnu Badal                                              #
####################################################################
@check_news_login
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def get_assign_data(request, news_type=None):
    stage_filter = False
    news_caller_filter = False
    news_reviewer_filter = False
    publisher_filter = False
    stage_data = Stage.objects.filter(id__lte=4)
    user_data_all = UserManagement.objects.all()
    news_caller = user_data_all.filter(is_news=True)
    news_reviewer = user_data_all.filter(is_news_reviewer=True)
    publisher_data = user_data_all.filter(is_publisher=True,user__is_active=True)

    search_data=None
    search_data = request.GET.get('search_data')
    if search_data :

        if news_type != None :
            admin_news_data = NewsFeed.objects.filter(topic_title__icontains=search_data,news_type=news_type).order_by('topic_title')
        else:
            messages.error(request, 'Invalid Feed Type Data')
            return render(request, 'news/news_feed_dashboard.html', {'tab': 'news_data','search_data':search_data})

        paginator = Paginator(admin_news_data, 100)
        page = request.GET.get('page')
        try:
            admin_news_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            admin_news_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            admin_news_data = paginator.page(paginator.num_pages)

        if news_type == 1:
            return render(request, 'news/assign/global_assign.html',
                      {'tab': 'news_data', 'admin_news_data': admin_news_data, 'stage_data': stage_data,
                       'news_caller': news_caller, 'news_reviewer': news_reviewer, 'publisher_data': publisher_data,
                       'stage_filter': stage_filter, 'news_caller_filter': news_caller_filter,
                       'news_reviewer_filter': news_reviewer_filter,
                       'publisher_filter': publisher_filter,'search_data':search_data})
        elif news_type == 2:
            return render(request, 'news/assign/wellness_assign.html',
                      {'tab': 'news_data', 'admin_news_data': admin_news_data, 'stage_data': stage_data,
                       'news_caller': news_caller, 'news_reviewer': news_reviewer, 'publisher_data': publisher_data,
                       'stage_filter': stage_filter, 'news_caller_filter': news_caller_filter,
                       'news_reviewer_filter': news_reviewer_filter,
                       'publisher_filter': publisher_filter,'search_data':search_data})
        elif news_type == 3:
            return render(request, 'news/assign/health_assign.html',
                      {'tab': 'news_data', 'admin_news_data': admin_news_data, 'stage_data': stage_data,
                       'news_caller': news_caller, 'news_reviewer': news_reviewer, 'publisher_data': publisher_data,
                       'stage_filter': stage_filter, 'news_caller_filter': news_caller_filter,
                       'news_reviewer_filter': news_reviewer_filter,
                       'publisher_filter': publisher_filter,'search_data':search_data})
        else:
            messages.error(request, '11111You are trying to access non existing data')
            return render(request, 'news/news_feed_dashboard.html', {'tab': 'news_data','search_data':search_data})

    try:
        x = request.GET.get('x')
    except:
        x = None
    if x == 'filter':
        if_ok = check_filter_only(request)
        if if_ok is True:
            admin_news_data, stage_filter, news_caller_filter, news_reviewer_filter, publisher_filter = filter_func(
                request, news_type)
        else:
            messages.error(request, "Please select any one kind of user at a time")
            admin_news_data = NewsFeed.objects.filter(news_type=news_type).order_by('topic_title')
            paginator = Paginator(admin_news_data, 100)
            page = request.GET.get('page')
            try:
                admin_news_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                admin_news_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                admin_news_data = paginator.page(paginator.num_pages)
    else:
        admin_news_data = NewsFeed.objects.filter(news_type=news_type).order_by('topic_title')
    paginator = Paginator(admin_news_data, 100)
    page = request.GET.get('page')
    try:
        admin_news_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        admin_news_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        admin_news_data = paginator.page(paginator.num_pages)
    if news_type == 1:
        return render(request, 'news/assign/global_assign.html',
                      {'tab': 'news_data', 'admin_news_data': admin_news_data, 'stage_data': stage_data,
                       'news_caller': news_caller, 'news_reviewer': news_reviewer, 'publisher_data': publisher_data,
                       'stage_filter': stage_filter, 'news_caller_filter': news_caller_filter,
                       'news_reviewer_filter': news_reviewer_filter,
                       'publisher_filter': publisher_filter})
    elif news_type == 2:
        return render(request, 'news/assign/wellness_assign.html',
                      {'tab': 'news_data', 'admin_news_data': admin_news_data, 'stage_data': stage_data,
                       'news_caller': news_caller, 'news_reviewer': news_reviewer, 'publisher_data': publisher_data,
                       'stage_filter': stage_filter, 'news_caller_filter': news_caller_filter,
                       'news_reviewer_filter': news_reviewer_filter,
                       'publisher_filter': publisher_filter})
    elif news_type == 3:
        return render(request, 'news/assign/health_assign.html',
                      {'tab': 'news_data', 'admin_news_data': admin_news_data, 'stage_data': stage_data,
                       'news_caller': news_caller, 'news_reviewer': news_reviewer, 'publisher_data': publisher_data,
                       'stage_filter': stage_filter, 'news_caller_filter': news_caller_filter,
                       'news_reviewer_filter': news_reviewer_filter,
                       'publisher_filter': publisher_filter})
    else:
        messages.error(request, '####You are trying to access non exist data')
        return render(request, 'news/news_feed_dashboard.html', {'tab': 'news_data'})

####################################################################
# Name - set_assign_data                                           #
# Owner - Visnu Badal                                              #
####################################################################
@check_news_login
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
@require_POST
def set_assign_data(request, news_type=None):
    if news_type is not None:
        response1 = {}
        try:
            assign_user = int(request.POST['telecaller'].strip())
        except:
            assign_user = 0
        try:
            change_stage = int(request.POST['stage'].strip())
        except:
            change_stage = 0
        checkedValues = request.POST.getlist('checkedValues[]')
        if assign_user and change_stage and checkedValues:
            if checkedValues[0] == 'on':
                try:
                    checkedValues = checkedValues[1:]
                except:
                    response1['Message'] = "Something Bad happened"
            nbslist = []
            nbflist = []
            for i in range(0, len(checkedValues)):
                try:
                    NewsFeed.objects.filter(id=checkedValues[i]).update(current_user_id=assign_user,
                                                                    stage_id=change_stage)
                    nbslist.append(checkedValues[i])
                except:
                    nbflist.append(checkedValues[i])
                    continue

            # if news_type == 1:
            #     ttype =
            # elif news_type == 2:
            #     response1['RedirectUrl'] = '/news-feed/assign/get/wellness/'
            # elif news_type == 3:
            #     response1['RedirectUrl'] = '/news-feed/assign/get/health/'
            # my_send_mail(request, 'lab', nbslist, nbflist, 'Lab Assignment', 'Assigned')

            response1['Redirect'] = True
            if news_type == 1:
                response1['RedirectUrl'] = '/news-feed/assign/get/global/'
            elif news_type == 2:
                response1['RedirectUrl'] = '/news-feed/assign/get/wellness/'
            elif news_type == 3:
                response1['RedirectUrl'] = '/news-feed/assign/get/health/'
            else:
                response1['RedirectUrl'] = '/news-feed/home/'
            response1['Message'] = "Assignment Completed"
        else:
            response1['Message'] = "Please select Stage and User "
        response = json.dumps(response1)
        return HttpResponse(response)
    else:
        raise Http404
""" End Assignment Function Here """
""" Start Block And Unblock Function Here """
####################################################################
# Name - blocking_news                                             #
# Owner - Visnu Badal                                              #
####################################################################
@check_news_login
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def blocking_news(request, news_id=None):
    try:
        if news_id is not None:
            news_object, block_unblock = check_block_unblock(news_id)
            if block_unblock is False:
                news_object.update(blocked_news=True)
            else:
                news_object.update(blocked_news=False)
            messages.success(request, 'Updated Successfully')
        else:
            messages.error(request, 'Something Bad Happened')
    except Exception as e:
        messages.error(request, 'Something Bad Happened')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

""" End Block and Unblock Function Here """
##################################################################################
# Global News Start Here                                                         #
##################################################################################

####################################################################
# Name - global_listing                                            #
# Owner - Visnu Badal                                              #
####################################################################
@check_news_login
@login_required(login_url='/')
@require_GET
def global_listing(request):
    """Nishank commented 5 lines inside the try block and the  @check_news_login decorator because now all types of users
    need to see news and not only admin and news and service tyoes becayse caller and reviewer and pulisher
    will also review these"""
    try:
        # Nishank added  current_user = request.user as we need to pass feeds to and fro review and publish users as well
        # and need to dis[play only related feeds
        global_news = NewsFeed.objects.filter(news_type=1,current_user = request.user,blocked_news=False,activation_status=True).order_by('topic_title')
        paginator = Paginator(global_news,50)
        page = request.GET.get('page')
        try:
            global_news = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            global_news = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            global_news = paginator.page(paginator.num_pages)
        #if not request.user.is_superuser:
        #    global_news = NewsFeed.objects.filter(
        #        Q(news_type=1) & Q(current_user_id=request.user.id) & Q(blocked_news=False))
        #else:
        #    global_news = NewsFeed.objects.filter(news_type=1)
    except Exception as e:
        global_news = []
        messages.error(request, "Something Bad happened")
    return render(request, 'news/global_listing.html',
                  {'tab_listing': 'global_listing', 'global_news': global_news, 'tab': 'news_data'})

####################################################################
# Name - adding_news                                               #
# Owner - Nishank                                                 #
####################################################################
@check_news_login
@login_required(login_url='/')
@csrf_exempt
def adding_news(request):
    if request.user.is_superuser:
        global_news_articles = NewsFeed.objects.filter(news_type_id=1)
    else:
        global_news_articles = NewsFeed.objects.filter(news_type_id=1, activation_status=True,blocked_news=False).order_by('topic_title')
    try:
        if request.method == 'GET':
            category_obj = Category.objects.filter(delete=False).order_by('name')
            return render(request, 'news/add_news.html', {'tab_listing': 'global_listing',
                                                          'global_news_articles': global_news_articles,
                                                          'category_obj': category_obj})
        elif request.method == "POST":
            page_title = request.POST['page_title']
            page_keywords = request.POST['page_keywords']
            page_description = request.POST['page_description']
            try:
                small_description = request.POST['small_description'].strip()
            except:
                small_description = ''
            try:
                publish_date = request.POST['publish_date'].strip()
                import datetime
                #publish_date = datetime.strptime('02/11/2010', '%d/%m/%Y').strftime('%d-%m-%Y')
                month, day, year = publish_date.split('/')
                publish_date = datetime.date(int(year),int(month),int(day) )
            except Exception as e:
                #print e
                publish_date = None
            global image_iterator
            image_iterator = 0
            related_topics = request.POST.getlist('related_topics')
            tag_string = request.POST['tag_string'].strip()
            topic_title = request.POST['topic_title'].strip()
            #doctors_category = request.POST['doctors_category'].strip()
            doctors_category = request.POST.getlist('category')
            tmpstr1 = ''
            counter = 0
            if doctors_category and doctors_category != []:
                counter += 1
                for i in doctors_category:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                doctors_category = tmpstr1
            else:
                doctors_category = ''
            # type = request.POST.getlist('type')
            tmpstr1 = ''
            counter = 0
            if related_topics and related_topics != []:
                counter += 1
                for i in related_topics:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                related_topics = tmpstr1
            else:
                related_topics = ''
            if len(request.FILES) == 1:
                file_name = request.FILES['myfile'].name
                tstr = ''
                for i in file_name:
                    if i == ' ' or i == '-' or i == '(' or i == ')':
                        #print 'space'
                        tstr = tstr + '_'
                    else:
                        #print i
                        tstr = tstr + i
                file_name = tstr.lower()
                global image_file_name
                global image_alt_g
                image_file_name = file_name
                file_type = file_name[-5:-1] + file_name[-1]
                if file_type.lower() == '.docx':
                    def convert_image(image):
                        with image.open() as image_bytes:
                            encoded_src = base64.b64encode(image_bytes.read()).decode("ascii")
                        imgData = encoded_src
                        global image_iterator
                        global image_file_name
                        image_iterator = image_iterator + 1
                        image = image_file_name[:-5] + "_" + str(image_iterator) + ".png"
                        global image_src
                        #image_src = "/media/articles/docx/newsfeed/" + image
                        image_src = "https://image2.healthforu.com/media/articles/docx/newsfeed/" + image
                        found = "---"
                        filepath = settings.DOCX_PATH_NEWSFEED + '/' + image
                        while True:
                            found = "yes"
                            if os.path.isfile(filepath) == True:
                                image_iterator = image_iterator + 1
                                image = image_file_name[:-5] + "_" + str(image_iterator) + ".png"
                                filepath = settings.DOCX_PATH_NEWSFEED + '/' + image
                            else:
                                found = "no"
                                break
                            #image_src = "/media/articles/docx/newsfeed/" + image
                            image_src = "https://image2.healthforu.com/media/articles/docx/newsfeed/" + image
                        global newsfeed_image_file_name
                        newsfeed_image_file_name = image
                        fh = open(filepath, "wb")
                        fh.write(imgData.decode('base64'))
                        fh.close()

                        """Uploading via ftplib """  # ~~~~New code Below Uploading block
                        import ftplib
                        from ftplib import FTP
                        try:
                            ftp = FTP("45.114.117.14")
                            ftp.login('www-data', 'qwwe34456ttggnhh666')
                            file = open(filepath, "rb")
                            ftp.cwd('/html/media/articles/docx/newsfeed/')
                            ftp.storbinary('STOR ' + newsfeed_image_file_name, file)
                            ftp.sendcmd('SITE CHMOD 664 ' + newsfeed_image_file_name)
                            #print "STORing File now..."
                            ftp.quit()
                            file.close()
                            #print "File transfered"
                        except Exception as e:
                            print e
                            #print e

                        """Uploading end"""

                        return {
                            # "src": "data:{0};base64,{1}".format(image.content_type, encoded_src)
                            "src": image_src,
                            "alt_text": image_alt_g
                        }

                    for f in request.FILES.getlist('myfile'):
                        # result = mammoth.convert_to_html(f)
                        result = mammoth.convert_to_html(f, convert_image=mammoth.images.img_element(convert_image))
                        global image_alt_g
                        global newsfeed_image_file_name
                        # tstr = ''
                        # for i in newsfeed_image_file_name:
                        #     if i == ' ':
                        #         print 'space'
                        #         tstr = tstr + '-'
                        #     else:
                        #         print i
                        #         tstr = tstr + i
                        # newsfeed_image_file_name = tstr
                        image_alt_g = ''
                        html = result.value  # The generated HTML
                        new_newsfeed = NewsFeed(newsfeed_docx_file=f, newsfeed_html_raw=html,
                                                newsfeed_html_refined=html, tag_string=tag_string,
                                                current_user_id=request.user.id, stage_id=2, topic_title=topic_title,
                                                doctors_category=doctors_category, related_topics=related_topics,
                                                newsfeed_image_file_name=newsfeed_image_file_name, news_type_id=1,
                                                free_text='',small_description=small_description,
                                                 publish_date=publish_date,page_title=page_title,
                                                page_keywords=page_keywords,page_description=page_description)
                        new_newsfeed.save()
                        newsfeed_image_file_name = ''
                    image_file_name = ''
                    image_iterator = 0
                    messages.success(request, "Successfully added Global News Feed")
                    return redirect(reverse('edit-global-news', args=[new_newsfeed.id]))
                else:
                    messages.error(request, "Uploaded file is not a docx file")
                    return render(request, 'news/add_news.html', {'tab_listing': 'global_listing',
                                                                  'global_news_articles': global_news_articles})
            else:
                messages.error("No file uploaded")
                return render(request, 'news/add_news.html', {'tab_listing': 'global_listing',
                                                              'global_news_articles': global_news_articles})
    except Exception as e:
        #print e
        messages.error(request, e)
        #return HttpResponseRedirect(reverse('add-global-news'))
        return HttpResponse(e)

####################################################################
# Name - edit_news                                                 #
# Owner - Nishank Gupta                                            #
####################################################################
#@check_news_login
@login_required(login_url='/')
@csrf_exempt
def edit_news(request, news_id=None):
    try:
        if request.user.is_superuser:
            global_news_articles = NewsFeed.objects.filter(~Q(id=news_id)).filter(news_type_id=1)
        else:
            global_news_articles = NewsFeed.objects.filter(~Q(id=news_id)).filter(news_type_id=1, activation_status=True,blocked_news=False).order_by('topic_title')

        if request.method == 'GET' and news_id is not None:
            if request.user.is_superuser:
                global_news = NewsFeed.objects.get(id=news_id, news_type=1)
            else:
                global_news = NewsFeed.objects.get(id=news_id, current_user_id=request.user.id, news_type=1)
            news_caller_data, news_reviewer_data, publisher_data = user_data_for_news()
            news_caller_data, news_reviewer_data, publisher_data = user_data_for_news()
            if global_news:
                list_empty =[]
                if global_news.related_topics and global_news.related_topics != '' and global_news.related_topics != []:
                    links = global_news.related_topics.split(",")
                    current_article_list = links
                else:
                    current_article_list = list_empty
                user_is_publisher = None
                is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                if len(is_publisher):
                    user_is_publisher = True
                try:
                    pub_date = global_news.publish_date.strftime('%d-%m-%Y')
                except:
                    pub_date = None
                category_obj = Category.objects.filter(delete=False).order_by('name')
                current_cats = global_news.doctors_category
                if current_cats and current_cats != '' or current_cats != ' ':
                    current_cats = current_cats.strip()
                    current_cats = current_cats.split(',')
                else:
                    current_cats = []
                return render(request, 'news/global_edit.html',
                              {'tab_listing': 'global_listing','global_news': global_news, 'tab': 'news_data', 'news_caller': news_caller_data,
                               'news_reviewer': news_reviewer_data, 'publisher_data': publisher_data,
                               'user_is_publisher': user_is_publisher,'global_news_articles':global_news_articles,
                               'pub_date':pub_date,'current_article_list':current_article_list,'current_cats':current_cats,
                               'category_obj':category_obj})
            else:
                messages.error(request, 'You have not rights to edit this document')
        elif request.method == 'POST' and news_id is not None :
            page_title = request.POST['page_title']
            page_keywords = request.POST['page_keywords']
            page_description = request.POST['page_description']
            try:
                small_description = request.POST['small_description'].strip()
            except:
                small_description = ''
            try:
                publish_date = request.POST['publish_date'].strip()
                import datetime
                #publish_date = datetime.strptime('02/11/2010', '%d/%m/%Y').strftime('%d-%m-%Y')
                day, month, year = publish_date.split('-')
                publish_date = datetime.date(int(year),int(month),int(day) )
            except Exception as e:
                #print e
                publish_date = None
            related_topics = request.POST.getlist('related_topics')
            tag_string = request.POST['tag_string'].strip()
            newsfeed_html_refined = request.POST['newsfeed_html_refined'].strip()
            topic_title = request.POST['topic_title'].strip()
            #doctors_category = request.POST['doctors_category'].strip()
            doctors_category = request.POST.getlist('category')

            tmpstr1 = ''
            counter = 0
            if doctors_category and doctors_category != []:
                counter += 1
                for i in doctors_category:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                doctors_category = tmpstr1
            else:
                doctors_category = ''

            tmpstr1 = ''
            counter = 0
            if related_topics and related_topics != []:
                counter += 1
                for i in related_topics:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                related_topics = tmpstr1
            else:
                related_topics = ''
            newsfeed_obj = NewsFeed.objects.get(pk=news_id)
            if newsfeed_obj:
                newsfeed_obj.topic_title = topic_title
                newsfeed_obj.doctors_category = doctors_category
                newsfeed_obj.tag_string = tag_string
                newsfeed_obj.related_topics = related_topics
                newsfeed_obj.newsfeed_html_refined = newsfeed_html_refined
                newsfeed_obj.publish_date = publish_date
                newsfeed_obj.small_description = small_description
                newsfeed_obj.page_title = page_title
                newsfeed_obj.page_keywords = page_keywords
                newsfeed_obj.page_description = page_description
                newsfeed_obj.save()
                messages.success(request, 'GLobal NewsFeed Data Successfully Updated')
                return redirect(reverse('edit-global-news', args=[news_id]))
    except Exception as e:
        messages.error(request, 'Something Bad Happened')
        is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
        if len(is_publisher):
            return HttpResponseRedirect(reverse('global-listing'))
        return HttpResponseRedirect(reverse('global-listing'))

####################################################################
# Name - update_global_news                                        #
# Owner - Visnu Badal                                              #
####################################################################
#@check_news_login
@login_required(login_url='/')
@csrf_exempt
@require_POST
def update_global_news(request, news_id=None):
    try:
        news_header = request.POST["news_header"]
        tag_string = request.POST['tag_string']
        article_intro = request.POST['article_intro']
        small_description = request.POST['small_description']
        conclusion = request.POST['conclusion']
        image_data = request.FILES.get('image_data')
        bullet_header = request.POST.getlist('bullet_header')
        bullet_body = request.POST.getlist('bullet_body')
        """Added by Nishank to make uploading the image again  > non compulsory  """
        if (not image_data):
            image_data = NewsFeed.objects.get(id=news_id).image
        if image_data and bullet_header and bullet_body and news_header and tag_string and small_description and conclusion and article_intro and news_id:
            data_obj = edit_rights(news_id, request, 1)
            if data_obj is not False:
                article_body = [{'bullet_header': bullet_header[bh], 'bullet_body': bullet_body[bh]} for bh in
                                range(0, len(bullet_header))]
                news_update_data = NewsFeed.objects.get(id=news_id)
                news_update_data.image = image_data
                news_update_data.save()
                data_obj.update(tag_string=tag_string, small_desc=small_description, article_body=article_body,
                                article_intro=article_intro, article_conclusion=conclusion)
                messages.success(request, "Successfully Updated")
            is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)
            if len(is_publisher):
                return HttpResponseRedirect(reverse('get-publish-global-feed'))
            elif request.user.is_superuser :
                return HttpResponseRedirect(reverse('get-assign-global-feed'))
            return HttpResponseRedirect(reverse('global-listing'))
        else:
            messages.error(request, "Please enter all fields")
            return HttpResponseRedirect('/news-feed/edit/global/' + news_id + '/')
    except Exception as e:
        messages.error(request, "Something Bad happened, Please Try Again")
        return HttpResponseRedirect('/news-feed/edit/global/' + news_id + '/')

"""Here End of Global News """
##################################################################################
# Wellness News Start Here                                                       #
##################################################################################

####################################################################
# Name - wellness_listing                                          #
# Owner - Visnu Badal                                              #
# Review by - ?                                                    #
#                                                                  #
####################################################################
@check_news_login
@login_required(login_url='/')
@require_GET
def wellness_listing(request):
    """Nishank commented 5 lines inside the try block and the  @check_news_login decorator because now all types of users
        need to see news and not only admin and news and service tyoes becayse caller and reviewer and pulisher
        will also review these"""
    try:
        #Nishank added  current_user = request.user as we need to pass feeds to and fro review and publish users as well
        #and need to dis[play only related feeds
        if (request.user.is_superuser ) :
            wellness_news = NewsFeed.objects.filter(news_type=2).order_by().order_by('topic_title')
        else:
            wellness_news = NewsFeed.objects.filter(news_type=2, current_user = request.user,blocked_news=False,activation_status=True).order_by('topic_title')
        paginator = Paginator(wellness_news,50)
        page = request.GET.get('page')
        try:
            wellness_news = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            wellness_news = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            wellness_news = paginator.page(paginator.num_pages)
        #if not request.user.is_superuser:
        #    wellness_news = NewsFeed.objects.filter(
        #        Q(news_type=2) & Q(current_user_id=request.user.id) & Q(blocked_news=False))
        #else:
        #    wellness_news = NewsFeed.objects.filter(news_type=2)
    except Exception as e:
        wellness_news = []
        messages.error(request, "Something Bad happened")
    return render(request, 'news/wellness_listing.html',
                  {'tab_listing': 'wellness_listing', 'wellness_news': wellness_news})

####################################################################
# Name - search_health_by stage and user                           #
# By-  Nishank Gupta                                               #
####################################################################
@check_news_login
@login_required(login_url='/')
@require_GET
def health_listing(request):
    """Nishank commented 5 lines inside the try block and the  @check_news_login decorator because now all types of users
    need to see news and not only admin and news and service tyoes becayse caller and reviewer and pulisher
    will also review these"""
    try:
        # Nishank added  current_user = request.user as we need to pass feeds to and fro review and publish users as well
        # and need to dis[play only related feeds
        health_news = NewsFeed.objects.filter(news_type=3, current_user=request.user,blocked_news=False,activation_status=True).order_by(
            'topic_title')

        paginator = Paginator(health_news, 50)
        page = request.GET.get('page')
        try:
            health_news = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            health_news = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            health_news = paginator.page(paginator.num_pages)
    except Exception as e:
        wellness_news = []
        messages.error(request, "Something Bad happened")
    return render(request, 'news/health_listing.html',
                  {'tab_listing': 'health_listing', 'health_news': health_news})

####################################################################
# Name - adding_wellness(request)                                  #
# Owner - Nishank                                                  #
####################################################################
@check_news_login
@login_required(login_url='/')
@csrf_exempt
def adding_wellness(request):
    if request.user.is_superuser:
        wellness_news_articles = NewsFeed.objects.filter(news_type_id=2)
    else:
        wellness_news_articles = NewsFeed.objects.filter(news_type_id=2, activation_status=True,blocked_news=False).order_by('topic_title')
    try:
        if request.method == 'GET':
            category_obj = Category.objects.filter(delete=False).order_by('name')
            return render(request, 'news/add_wellness.html', {'tab_listing': 'wellness_listing',
                                                          'wellness_news_articles': wellness_news_articles,
                                                              'category_obj': category_obj})
        elif request.method == "POST":
            page_title = request.POST['page_title']
            page_keywords = request.POST['page_keywords']
            page_description = request.POST['page_description']
            try:
                small_description = request.POST['small_description'].strip()
            except:
                small_description = ''
            try:
                publish_date = request.POST['publish_date'].strip()
                import datetime
                #publish_date = datetime.strptime('02/11/2010', '%d/%m/%Y').strftime('%d-%m-%Y')
                month, day, year = publish_date.split('/')
                publish_date = datetime.date(int(year),int(month),int(day) )
            except Exception as e:
                #print e
                publish_date = None
            global image_iterator
            image_iterator = 0
            related_topics = request.POST.getlist('related_topics')
            tag_string = request.POST['tag_string'].strip()
            topic_title = request.POST['topic_title'].strip()
            #doctors_category = request.POST['doctors_category'].strip()
            doctors_category = request.POST.getlist('category')
            tmpstr1 = ''
            counter = 0
            if doctors_category and doctors_category != []:
                counter += 1
                for i in doctors_category:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                doctors_category = tmpstr1
            else:
                doctors_category = ''
            # type = request.POST.getlist('type')
            tmpstr1 = ''
            counter = 0
            if related_topics and related_topics != []:
                counter += 1
                for i in related_topics:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                related_topics = tmpstr1
            else:
                related_topics = ''

            if len(request.FILES) == 1:
                file_name = request.FILES['myfile'].name
                tstr = ''
                for i in file_name:
                    if i == ' ' or i == '-' or i == '(' or i == ')':
                        #print 'space'
                        tstr = tstr + '_'
                    else:
                        #print i
                        tstr = tstr + i
                file_name = tstr.lower()
                global image_file_name
                global image_alt_g
                image_file_name = file_name
                file_type = file_name[-5:-1] + file_name[-1]
                if file_type.lower() == '.docx':
                    def convert_image(image):
                        with image.open() as image_bytes:
                            encoded_src = base64.b64encode(image_bytes.read()).decode("ascii")
                        imgData = encoded_src
                        global image_iterator
                        global image_file_name
                        image_iterator = image_iterator + 1
                        image = image_file_name[:-5] + "_" + str(image_iterator) + ".png"
                        global image_src
                        #image_src = "/media/articles/docx/newsfeed/" + image
                        image_src = "https://image2.healthforu.com/media/articles/docx/newsfeed/" + image
                        found = "---"
                        filepath = settings.DOCX_PATH_NEWSFEED + '/' + image
                        while True:
                            found = "yes"
                            if os.path.isfile(filepath) == True:
                                image_iterator = image_iterator + 1
                                image = image_file_name[:-5] + "_" + str(image_iterator) + ".png"
                                filepath = settings.DOCX_PATH_NEWSFEED + '/' + image
                            else:
                                found = "no"
                                break
                            #image_src = "/media/articles/docx/newsfeed/" + image
                            image_src = "https://image2.healthforu.com/media/articles/docx/newsfeed/" + image
                        global newsfeed_image_file_name
                        newsfeed_image_file_name = image
                        fh = open(filepath, "wb")
                        fh.write(imgData.decode('base64'))
                        fh.close()

                        """Uploading via ftplib """  # ~~~~New code Below Uploading block
                        import ftplib
                        from ftplib import FTP
                        try:
                            ftp = FTP("45.114.117.14")
                            ftp.login('www-data', 'qwwe34456ttggnhh666')
                            file = open(filepath, "rb")
                            ftp.cwd('/html/media/articles/docx/newsfeed/')
                            ftp.storbinary('STOR ' + newsfeed_image_file_name, file)
                            ftp.sendcmd('SITE CHMOD 664 ' + newsfeed_image_file_name)
                            #print "STORing File now..."
                            ftp.quit()
                            file.close()
                            #print "File transfered"
                        except Exception as e:
                            print e
                            #print e

                        return {
                            # "src": "data:{0};base64,{1}".format(image.content_type, encoded_src)
                            "src": image_src,
                            "alt_text": image_alt_g
                        }

                    for f in request.FILES.getlist('myfile'):
                        # result = mammoth.convert_to_html(f)
                        result = mammoth.convert_to_html(f, convert_image=mammoth.images.img_element(convert_image))
                        global image_alt_g
                        global newsfeed_image_file_name
                        # tstr = ''
                        # for i in newsfeed_image_file_name:
                        #     if i == ' ':
                        #         print 'space'
                        #         tstr = tstr + '-'
                        #     else:
                        #         print i
                        #         tstr = tstr + i
                        # newsfeed_image_file_name = tstr
                        image_alt_g = ''
                        html = result.value  # The generated HTML
                        new_newsfeed = NewsFeed(newsfeed_docx_file=f, newsfeed_html_raw=html,
                                                newsfeed_html_refined=html, tag_string=tag_string,
                                                current_user_id=request.user.id, stage_id=2, topic_title=topic_title,
                                                doctors_category=doctors_category, related_topics=related_topics,
                                                newsfeed_image_file_name=newsfeed_image_file_name, news_type_id=2,
                                                free_text='',small_description=small_description,
                                                publish_date=publish_date,page_title=page_title,
                                                page_keywords=page_keywords,page_description=page_description)
                        new_newsfeed.save()
                        newsfeed_image_file_name = ''
                    image_file_name = ''
                    image_iterator = 0
                    messages.success(request, "Successfully added Wellness News Feed")
                    return redirect(reverse('edit-wellness-news', args=[new_newsfeed.id]))
                else:
                    messages.error(request, "Uploaded file is not a docx file")
                    return render(request, 'news/add_wellness.html', {'tab_listing': 'wellness_listing',
                                                                  'wellness_news_articles': wellness_news_articles})
            else:
                messages.error("No file uploaded")
                return render(request, 'news/add_wellness.html', {'tab_listing': 'wellness_listing',
                                                              'wellness_news_articles': wellness_news_articles})
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('add-wellness-news'))

####################################################################
# Name - edit_wellness                                             #
# Owner - Nishank Gupta                                            #
####################################################################
#@check_news_login
@login_required(login_url='/')
@csrf_exempt
def edit_wellness(request, news_id=None):
    try:
        if request.user.is_superuser:
            wellness_news_articles = NewsFeed.objects.filter(~Q(id=news_id)).filter(news_type_id=2)
        else:
            wellness_news_articles = NewsFeed.objects.filter(~Q(id=news_id)).filter(news_type_id=2, activation_status=True,blocked_news=False).order_by('topic_title')
        if request.method == 'GET' and news_id is not None:
            if request.user.is_superuser:
                wellness_news = NewsFeed.objects.get(id=news_id, news_type=2)
            else:
                wellness_news = NewsFeed.objects.get(id=news_id, current_user_id=request.user.id, news_type=2)
            news_caller_data, news_reviewer_data, publisher_data = user_data_for_news()
            if wellness_news:
                list_empty = []
                if wellness_news.related_topics and wellness_news.related_topics != '' and wellness_news.related_topics != []:
                    links = wellness_news.related_topics.split(",")
                    current_article_list = links
                else:
                    current_article_list = list_empty
                user_is_publisher = None
                is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                if len(is_publisher):
                    user_is_publisher = True
                try:
                    pub_date = wellness_news.publish_date.strftime('%d-%m-%Y')
                except:
                    pub_date = None
                category_obj = Category.objects.filter(delete=False).order_by('name')
                current_cats = wellness_news.doctors_category
                if current_cats and current_cats != '' or current_cats != ' ':
                    current_cats = current_cats.strip()
                    current_cats = current_cats.split(',')
                else:
                    current_cats = []
                return render(request, 'news/wellness_edit.html',
                              {'tab_listing': 'wellness_listing','wellness_news': wellness_news, 'tab': 'news_data', 'news_caller': news_caller_data,
                               'news_reviewer': news_reviewer_data, 'publisher_data': publisher_data,
                               'user_is_publisher': user_is_publisher,'wellness_news_articles':wellness_news_articles,
                               'pub_date':pub_date,'current_article_list':current_article_list,
                               'current_cats': current_cats, 'category_obj': category_obj})
            else:
                messages.error(request, 'You have not rights to edit this document')
        elif request.method == 'POST' and news_id is not None :
            page_title = request.POST['page_title']
            page_keywords = request.POST['page_keywords']
            page_description = request.POST['page_description']
            try:
                small_description = request.POST['small_description'].strip()
            except:
                small_description = ''
            try:
                publish_date = request.POST['publish_date'].strip()
                import datetime
                #publish_date = datetime.strptime('02/11/2010', '%d/%m/%Y').strftime('%d-%m-%Y')
                day, month, year = publish_date.split('-')
                publish_date = datetime.date(int(year),int(month),int(day) )
            except Exception as e:
                #print e
                publish_date = None
            related_topics = request.POST.getlist('related_topics')
            tag_string = request.POST['tag_string'].strip()
            newsfeed_html_refined = request.POST['newsfeed_html_refined'].strip()
            topic_title = request.POST['topic_title'].strip()
            #doctors_category = request.POST['doctors_category'].strip()
            doctors_category = request.POST.getlist('category')
            tmpstr1 = ''
            counter = 0
            if doctors_category and doctors_category != []:
                counter += 1
                for i in doctors_category:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                doctors_category = tmpstr1
            else:
                doctors_category = ''

            tmpstr1 = ''
            counter = 0
            if related_topics and related_topics != []:
                counter += 1
                for i in related_topics:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                related_topics = tmpstr1
            else:
                related_topics = ''
            newsfeed_obj = NewsFeed.objects.get(pk=news_id)
            if newsfeed_obj:
                newsfeed_obj.topic_title = topic_title
                newsfeed_obj.doctors_category = doctors_category
                newsfeed_obj.tag_string = tag_string
                newsfeed_obj.related_topics = related_topics
                newsfeed_obj.newsfeed_html_refined = newsfeed_html_refined
                newsfeed_obj.publish_date = publish_date
                newsfeed_obj.small_description = small_description
                newsfeed_obj.page_title = page_title
                newsfeed_obj.page_keywords = page_keywords
                newsfeed_obj.page_description = page_description
                newsfeed_obj.save()
                messages.success(request, 'GLobal NewsFeed Data Successfully Updated')
                return redirect(reverse('edit-wellness-news', args=[news_id]))

    except Exception as e:
        messages.error(request, 'Something Bad Happened')
        is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
        if len(is_publisher):
            return HttpResponseRedirect(reverse('wellness-listing'))
        return HttpResponseRedirect(reverse('wellness-listing'))

####################################################################
# Name - update_wellness_news                                      #
# Owner - Visnu Badal                                              #
####################################################################
#@check_news_login
@login_required(login_url='/')
@csrf_exempt
@require_POST
def update_wellness_news(request, news_id=None):
    try:
        news_header = request.POST["news_header"]
        tag_string = request.POST['tag_string']
        article_intro = request.POST['article_intro']
        small_description = request.POST['small_description']
        conclusion = request.POST['conclusion']
        image_data = request.FILES.get('image_data')
        bullet_header = request.POST.getlist('bullet_header')
        bullet_body = request.POST.getlist('bullet_body')
        """Added by Nishank to make uploading the image again  > non compulsory  """
        if (not image_data):
            image_data = NewsFeed.objects.get(id=news_id).image
        if image_data and bullet_header and bullet_body and news_header and tag_string and small_description and conclusion and article_intro and news_id:
            data_obj = edit_rights(news_id, request, 2)
            if data_obj is not False:
                article_body = [{'bullet_header': bullet_header[bh], 'bullet_body': bullet_body[bh]} for bh in
                                range(0, len(bullet_header))]
                news_update_data = NewsFeed.objects.get(id=news_id)
                news_update_data.image = image_data
                news_update_data.save()
                data_obj.update(tag_string=tag_string, small_desc=small_description, article_body=article_body,
                                article_intro=article_intro, article_conclusion=conclusion)
                messages.success(request, "Successfully Updated")
            is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)
            if len(is_publisher):
                return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
            elif request.user.is_superuser :
                return HttpResponseRedirect(reverse('get-assign-wellness-feed'))
            return HttpResponseRedirect(reverse('wellness-listing'))
        else:
            messages.error(request, "Please enter all fields")
            return HttpResponseRedirect('/news-feed/edit/wellness/' + news_id + '/')
    except Exception as e:
        messages.error(request, "Something Bad happened, Please Try Again")
        return HttpResponseRedirect('/news-feed/edit/wellness/' + news_id + '/')

""" End Wellness Function Here"""

####################################################################
# Name - adding_health(request)                                    #
# Owner - Nishank                                                  #
####################################################################
@check_news_login
@login_required(login_url='/')
@csrf_exempt
def adding_health(request):
    if request.user.is_superuser:
        health_news_articles = NewsFeed.objects.filter(news_type_id=3)
    else:
        health_news_articles = NewsFeed.objects.filter(news_type_id=3, activation_status=True,blocked_news=False).order_by('topic_title')
    try:
        if request.method == 'GET':
            category_obj = Category.objects.filter(delete=False).order_by('name')
            return render(request, 'news/add_health.html', {'tab_listing': 'health_listing',
                                                          'health_news_articles': health_news_articles,
                                                            'category_obj': category_obj})
        elif request.method == "POST":
            page_title = request.POST['page_title']
            page_keywords = request.POST['page_keywords']
            page_description = request.POST['page_description']
            try:
                small_description = request.POST['small_description'].strip()
            except:
                small_description = ''
            try:
                publish_date = request.POST['publish_date'].strip()
                import datetime
                #publish_date = datetime.strptime('02/11/2010', '%d/%m/%Y').strftime('%d-%m-%Y')
                month, day, year = publish_date.split('/')
                publish_date = datetime.date(int(year),int(month),int(day) )
            except Exception as e:
                #print e
                publish_date = None
            global image_iterator
            image_iterator = 0
            related_topics = request.POST.getlist('related_topics')
            tag_string = request.POST['tag_string'].strip()
            topic_title = request.POST['topic_title'].strip()
            #doctors_category = request.POST['doctors_category'].strip()
            doctors_category = request.POST.getlist('category')
            tmpstr1 = ''
            counter = 0
            if doctors_category and doctors_category != []:
                counter += 1
                for i in doctors_category:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                doctors_category = tmpstr1
            else:
                doctors_category = ''
            # type = request.POST.getlist('type')
            tmpstr1 = ''
            counter = 0
            if related_topics and related_topics != []:
                counter += 1
                for i in related_topics:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                related_topics = tmpstr1
            else:
                related_topics = ''
            if len(request.FILES) == 1:
                file_name = request.FILES['myfile'].name
                tstr = ''
                for i in file_name:
                    if i == ' ' or i == '-' or i == '(' or i == ')':
                        #print 'space'
                        tstr = tstr + '_'
                    else:
                        #print i
                        tstr = tstr + i
                file_name = tstr.lower()
                global image_file_name
                global image_alt_g
                image_file_name = file_name
                file_type = file_name[-5:-1] + file_name[-1]
                if file_type.lower() == '.docx':
                    def convert_image(image):
                        with image.open() as image_bytes:
                            encoded_src = base64.b64encode(image_bytes.read()).decode("ascii")
                        imgData = encoded_src
                        global image_iterator
                        global image_file_name
                        image_iterator = image_iterator + 1
                        image = image_file_name[:-5] + "_" + str(image_iterator) + ".png"
                        global image_src
                        #image_src = "/media/articles/docx/newsfeed/" + image
                        image_src = "https://image2.healthforu.com/media/articles/docx/newsfeed/" + image
                        found = "---"
                        filepath = settings.DOCX_PATH_NEWSFEED + '/' + image
                        while True:
                            found = "yes"
                            if os.path.isfile(filepath) == True:
                                image_iterator = image_iterator + 1
                                image = image_file_name[:-5] + "_" + str(image_iterator) + ".png"
                                filepath = settings.DOCX_PATH_NEWSFEED + '/' + image
                            else:
                                found = "no"
                                break
                            #image_src = "/media/articles/docx/newsfeed/" + image
                            image_src = "https://image2.healthforu.com/media/articles/docx/newsfeed/" + image
                        global newsfeed_image_file_name
                        newsfeed_image_file_name = image
                        fh = open(filepath, "wb")
                        fh.write(imgData.decode('base64'))
                        fh.close()

                        """Uploading via ftplib """  # ~~~~New code Below Uploading block
                        import ftplib
                        from ftplib import FTP
                        try:
                            ftp = FTP("45.114.117.14")
                            ftp.login('www-data', 'qwwe34456ttggnhh666')
                            file = open(filepath, "rb")
                            ftp.cwd('/html/media/articles/docx/newsfeed/')
                            ftp.storbinary('STOR ' + newsfeed_image_file_name, file)
                            ftp.sendcmd('SITE CHMOD 664 ' + newsfeed_image_file_name)
                            #print "STORing File now..."
                            ftp.quit()
                            file.close()
                            #print "File transfered"
                        except Exception as e:
                            print e
                            #print e

                        return {
                            # "src": "data:{0};base64,{1}".format(image.content_type, encoded_src)
                            "src": image_src,
                            "alt_text": image_alt_g
                        }
                    for f in request.FILES.getlist('myfile'):
                        # result = mammoth.convert_to_html(f)
                        result = mammoth.convert_to_html(f, convert_image=mammoth.images.img_element(convert_image))
                        global image_alt_g
                        global newsfeed_image_file_name
                        # tstr = ''
                        # for i in newsfeed_image_file_name:
                        #     if i == ' ':
                        #         print 'space'
                        #         tstr = tstr + '-'
                        #     else:
                        #         print i
                        #         tstr = tstr + i
                        # newsfeed_image_file_name = tstr
                        image_alt_g = ''
                        html = result.value  # The generated HTML
                        new_newsfeed = NewsFeed(newsfeed_docx_file=f, newsfeed_html_raw=html,
                                                newsfeed_html_refined=html, tag_string=tag_string,
                                                current_user_id=request.user.id, stage_id=2, topic_title=topic_title,
                                                doctors_category=doctors_category, related_topics=related_topics,
                                                newsfeed_image_file_name=newsfeed_image_file_name, news_type_id=3,
                                                free_text='',small_description=small_description,
                                                publish_date=publish_date,page_title=page_title,
                                                page_keywords=page_keywords,page_description=page_description)
                        new_newsfeed.save()
                        newsfeed_image_file_name = ''
                    image_file_name = ''
                    image_iterator = 0
                    messages.success(request, "Successfully added Health News Feed")
                    return redirect(reverse('edit-health-news', args=[new_newsfeed.id]))
                else:
                    messages.error(request, "Uploaded file is not a docx file")
                    return render(request, 'news/add_health.html', {'tab_listing': 'health_listing',
                                                                  'health_news_articles': health_news_articles})
            else:
                messages.error("No file uploaded")
                return render(request, 'news/add_health.html', {'tab_listing': 'health_listing',
                                                              'health_news_articles': health_news_articles})
    except Exception as e:
        #print e
        messages.error(request, e)
        return HttpResponseRedirect(reverse('add-health-news'))

####################################################################
# Name - edit_health                                               #
# By Nishank                                                       #
####################################################################
#@check_news_login commented to allow access to all types of users
@login_required(login_url='/')
@csrf_exempt
def edit_health(request, news_id=None):
    try:
        if request.method == 'GET' and news_id is not None:
            #Nishank made edits to edit_rights  from hfu.cms.check-point
            data_obj = edit_rights(news_id, request, 3)
            news_caller_data, news_reviewer_data, publisher_data = user_data_for_news()
            if data_obj is not False:
                article_data = data_obj[0].article_body
                if type(article_data) is str:
                    article_data = json.loads(article_data)
                return render(request, 'news/health_edit.html',
                              {'health_data_edit': data_obj, 'tab_listing': 'health_listing',
                               'article_data': article_data, 'tab': 'news_data', 'news_caller': news_caller_data,
                               'news_reviewer': news_reviewer_data, 'publisher_data': publisher_data})
            else:
                messages.error(request, 'You have not rights to edit this document')
    except Exception as e:
        messages.error(request, 'Something Bad Happened')
    return HttpResponseRedirect(reverse('health-listing'))

####################################################################
# Name - edit_health                                               #
# Owner - Nishank Gupta                                            #
####################################################################
#@check_news_login
@login_required(login_url='/')
@csrf_exempt
def edit_health(request, news_id=None):
    try:
        if request.user.is_superuser:
            health_news_articles = NewsFeed.objects.filter(~Q(id=news_id)).filter(news_type_id=3)
        else:
            health_news_articles = NewsFeed.objects.filter(~Q(id=news_id)).filter(news_type_id=3, activation_status=True,blocked_news=False).order_by('topic_title')
        if request.method == 'GET' and news_id is not None:
            if request.user.is_superuser:
                health_news = NewsFeed.objects.get(id=news_id, news_type=3)
            else:
                health_news = NewsFeed.objects.get(id=news_id, current_user_id=request.user.id, news_type=3)
            news_caller_data, news_reviewer_data, publisher_data = user_data_for_news()
            if health_news:
                list_empty = []
                if health_news.related_topics and health_news.related_topics != '' and health_news.related_topics != []:
                    links = health_news.related_topics.split(",")
                    current_article_list = links
                else:
                    current_article_list = list_empty
                user_is_publisher = None
                is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                if len(is_publisher):
                    user_is_publisher = True
                try:
                    pub_date = health_news.publish_date.strftime('%d-%m-%Y')
                except:
                    pub_date = None

                category_obj = Category.objects.filter(delete=False).order_by('name')
                current_cats = health_news.doctors_category
                if current_cats and current_cats != '' or current_cats != ' ':
                    current_cats = current_cats.strip()
                    current_cats = current_cats.split(',')
                else:
                    current_cats = []
                return render(request, 'news/health_edit.html',
                              {'tab_listing': 'health_listing','health_news': health_news, 'tab': 'news_data', 'news_caller': news_caller_data,
                               'news_reviewer': news_reviewer_data, 'publisher_data': publisher_data,
                               'user_is_publisher': user_is_publisher,'health_news_articles':health_news_articles,
                               'pub_date':pub_date,'current_article_list':current_article_list,
                               'current_cats': current_cats, 'category_obj': category_obj})
            else:
                messages.error(request, 'You have not rights to edit this document')
        elif request.method == 'POST' and news_id is not None :
            page_title = request.POST['page_title']
            page_keywords = request.POST['page_keywords']
            page_description = request.POST['page_description']
            try:
                small_description = request.POST['small_description'].strip()
            except:
                small_description = ''
            try:
                publish_date = request.POST['publish_date'].strip()
                import datetime
                #publish_date = datetime.strptime('02/11/2010', '%d/%m/%Y').strftime('%d-%m-%Y')

                day, month, year = publish_date.split('-')
                publish_date = datetime.date(int(year),int(month),int(day) )
            except Exception as e:
                #print e
                publish_date = None
            related_topics = request.POST.getlist('related_topics')
            tag_string = request.POST['tag_string'].strip()
            newsfeed_html_refined = request.POST['newsfeed_html_refined'].strip()
            topic_title = request.POST['topic_title'].strip()
            #doctors_category = request.POST['doctors_category'].strip()
            doctors_category = request.POST.getlist('category')
            tmpstr1 = ''
            counter = 0
            if doctors_category and doctors_category != []:
                counter += 1
                for i in doctors_category:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                doctors_category = tmpstr1
            else:
                doctors_category = ''

            tmpstr1 = ''
            counter = 0
            if related_topics and related_topics != []:
                counter += 1
                for i in related_topics:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                related_topics = tmpstr1
            else:
                related_topics = ''
            newsfeed_obj = NewsFeed.objects.get(pk=news_id)
            if newsfeed_obj:
                newsfeed_obj.topic_title = topic_title
                newsfeed_obj.doctors_category = doctors_category
                newsfeed_obj.tag_string = tag_string
                newsfeed_obj.related_topics = related_topics
                newsfeed_obj.newsfeed_html_refined = newsfeed_html_refined
                newsfeed_obj.publish_date = publish_date
                newsfeed_obj.small_description = small_description
                newsfeed_obj.page_title = page_title
                newsfeed_obj.page_keywords = page_keywords
                newsfeed_obj.page_description = page_description
                newsfeed_obj.save()
                messages.success(request, 'Health NewsFeed Data Successfully Updated')
                return redirect(reverse('edit-health-news', args=[news_id]))
    except Exception as e:
        messages.error(request, 'Something Bad Happened')
        is_publisher = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
        if len(is_publisher):
            return HttpResponseRedirect(reverse('health-listing'))
        return HttpResponseRedirect(reverse('health-listing'))

####################################################################
# Name - update_health_news                                        #
# By Nishank                                                       #
####################################################################
#@check_news_login
@login_required(login_url='/')
@csrf_exempt
@require_POST
def update_health_news(request, news_id=None):
    try:
        news_header = request.POST["news_header"]
        tag_string = request.POST['tag_string']
        article_intro = request.POST['article_intro']
        small_description = request.POST['small_description']
        conclusion = request.POST['conclusion']
        image_data = request.FILES.get('image_data')
        bullet_header = request.POST.getlist('bullet_header')
        bullet_body = request.POST.getlist('bullet_body')
        """Added by Nishank to make uploading the image again  > non compulsory  """
        if (not image_data):
            image_data = NewsFeed.objects.get(id=news_id).image
        if image_data and bullet_header and bullet_body and news_header and tag_string and small_description and conclusion and article_intro and news_id:
            data_obj = edit_rights(news_id, request, 3)
            if data_obj is not False:
                article_body = [{'bullet_header': bullet_header[bh], 'bullet_body': bullet_body[bh]} for bh in
                                range(0, len(bullet_header))]
                news_update_data = NewsFeed.objects.get(id=news_id)
                news_update_data.image = image_data
                news_update_data.save()
                data_obj.update(tag_string=tag_string, small_desc=small_description, article_body=article_body,
                                article_intro=article_intro, article_conclusion=conclusion)
                messages.success(request, "Successfully Updated")
            is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)
            if len(is_publisher):
                return HttpResponseRedirect(reverse('get-publish-health-feed'))
            elif request.user.is_superuser :
                return HttpResponseRedirect(reverse('get-assign-health-feed'))
            return HttpResponseRedirect(reverse('health-listing'))
        else:
            messages.error(request, "Please enter all fields")
            return HttpResponseRedirect('/news-feed/edit/health/' + news_id + '/')
    except Exception as e:
        messages.error(request, "Something Bad happened, Please Try Again")
        return HttpResponseRedirect('/news-feed/edit/health/' + news_id + '/')

""" Mark as completed Function start from here """
####################################################################
# Name - set_reviewer_mark                                         #
# Owner - Visnu Badal                                              #
####################################################################
#@check_news_login commented this to allow publisher to use this
@login_required(login_url='/')
@csrf_exempt
@require_POST
def set_reviewer_mark(request, news_type=None):
    try:
        news_id = request.POST['news_id']
        news_reviewer_id = request.POST['news_reviewer_id']
        try:
            free_text = request.POST['free_text']
        except:
            free_text=''
        if news_id and news_reviewer_id:
            try:
                NewsFeed.objects.filter(id=news_id).update(stage_id=3, current_user_id=int(news_reviewer_id),
                                                           previous_user=request.user.id, free_text= free_text)
                messages.success(request, "Successfully Completed")
                is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)
                if news_type == 'global':
                    if len(is_publisher):
                        return HttpResponseRedirect(reverse('get-publish-global-feed'))
                    else:
                        return HttpResponseRedirect('/news-feed/global/listing/')
                elif news_type == 'wellness':
                    if len(is_publisher):
                        return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
                    else:
                        return HttpResponseRedirect('/news-feed/wellness/listing/')
                elif news_type == 'health':
                    if len(is_publisher):
                        return HttpResponseRedirect(reverse('get-publish-health-feed'))
                    else:
                        return HttpResponseRedirect('/news-feed/health/listing/')
            except:
                messages.error(request, "Something Bad happened")
        else:
            messages.error(request, 'Please Select Proper User')
        is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)
        if news_type == 'global':
            if len(is_publisher):
                return HttpResponseRedirect(reverse('get-publish-global-feed'))
            else:
                return HttpResponseRedirect('/news-feed/edit/global/' + news_id + '/')
        elif news_type == 'wellness':
            if len(is_publisher):
                return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
            else:
                return HttpResponseRedirect('/news-feed/edit/global/' + news_id + '/')
    except Exception as e:
        raise Http404

####################################################################
# Name - set_caller_mark                                           #
# Owner - Visnu Badal                                              #
####################################################################
#@check_news_login  commented this to enable publisher to use this view to send back
@login_required(login_url='/')
@csrf_exempt
@require_POST
def set_caller_mark(request, news_type=None):
    try:
        news_id = request.POST['news_id']
        news_caller = request.POST['news_caller']
        try:
            free_text = request.POST['free_text']
        except:
            free_text=''
        if news_id and news_caller:
            try:
                NewsFeed.objects.filter(id=news_id).update(stage_id=2, current_user_id=int(news_caller),
                                                           previous_user=request.user.id,free_text=free_text)

                messages.success(request, "Successfully Completed")
                is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)
                if news_type == 'global':
                    if len(is_publisher):
                        return HttpResponseRedirect(reverse('get-publish-global-feed'))
                    else:
                        return HttpResponseRedirect('/news-feed/global/listing/')
                elif news_type == 'wellness':
                    if len(is_publisher):
                        return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
                    else:
                        return HttpResponseRedirect('/news-feed/wellness/listing/')
                elif news_type == 'health':
                    if len(is_publisher):
                        return HttpResponseRedirect(reverse('get-publish-health-feed'))
                    else:
                        return HttpResponseRedirect('/news-feed/health/listing/')
            except:
                messages.error(request, "Something Bad happened")
        else:
            messages.error(request, 'Please Select Proper User')
        is_publisher = UserManagement.objects.filter(user_id= request.user.id,is_publisher=True)
        if news_type == 'global':
            if len(is_publisher):
                        return HttpResponseRedirect(reverse('get-publish-global-feed'))
            else:
                return HttpResponseRedirect('/news-feed/edit/global/' + news_id + '/')
        elif news_type == 'wellness':
            if len(is_publisher):
                return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
            else:
                return HttpResponseRedirect('/news-feed/edit/global/' + news_id + '/')
    except Exception as e:
        raise Http404

####################################################################
# Name - set_publisher_mark                                        #
# Owner - Visnu Badal                                              #
####################################################################
@check_news_login
@csrf_exempt
@require_POST
def set_publisher_mark(request, news_type=None):
    try:
        news_id = request.POST['news_id']
        publisher_user = request.POST['publisher_user']
        try:
            free_text= request.POST['free_text']
        except:
            free_text=''
        if news_id and publisher_user:
            try:
                NewsFeed.objects.filter(id=news_id).update(stage_id=4, current_user_id=int(publisher_user),
                                                           previous_user=request.user.id,free_text=free_text)
                messages.success(request, "Successfully Completed")
                if news_type == 'global':
                    return HttpResponseRedirect('/news-feed/global/listing/')
                elif news_type == 'wellness':
                    return HttpResponseRedirect('/news-feed/wellness/listing/')
                elif news_type == 'health':
                    return HttpResponseRedirect('/news-feed/health/listing/')
            except:
                messages.error(request, "Something Bad happened")
        else:
            messages.error(request, 'Please Select Proper User')
        if news_type == 'global':
            return HttpResponseRedirect('/news-feed/edit/global/' + news_id + '/')
        elif news_type == 'wellness':
            return HttpResponseRedirect('/news-feed/edit/global/' + news_id + '/')
    except Exception as e:
        raise Http404
""" End assignment Function Here """
""" Publisher Function Here """

####################################################################
# Name - get_news_data_publisher                                   #
# Owner - Visnu Badal                                              #
####################################################################
@publisher_permission
@login_required(login_url='/')
@require_GET
def get_news_data_publisher(request, news_type=None):
    if news_type is not None:
        stage_data = None
        search_data = None
        try:
            search_data =  request.GET['search_data']
        except:
            search_data = None
        if  search_data :
            publisher_data = NewsFeed.objects.filter(current_user_id=request.user.id, topic_title__icontains=search_data, activation_status=True,
                                              blocked_news=False, news_type_id=int(news_type)).order_by('topic_title')
        else:
            publisher_data, stage_data = getting_news_publisher_data(request, news_type)
        #publisher_data = paginate(publisher_data, 3)
        paginator = Paginator(publisher_data, 50)
        page = request.GET.get('page')
        try:
            publisher_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            publisher_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            publisher_data = paginator.page(paginator.num_pages)

        if news_type == 1:
            return render(request, 'news/publisher/global/globle_publisher_listing.html',
                          {'publisher_data': publisher_data, 'tab': 'publish_global_feed', 'stage_data': stage_data,'search_data':search_data})
        elif news_type == 2:
            return render(request, 'news/publisher/wellness/wellness_publisher_listing.html',
                          {'publisher_data': publisher_data, 'tab': 'publish_wellness_feed', 'stage_data': stage_data,'search_data':search_data})

        elif news_type == 3:
            return render(request, 'news/publisher/health/health_publisher_listing.html',
                          {'publisher_data': publisher_data, 'tab': 'publish_health_feed', 'stage_data': stage_data,'search_data':search_data})
    else:
        messages.error(request, "Something Bad Happened Please Contact to admin")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
""" End Publisher Function Here """
""" satrt File functions Here """

####################################################################
# Name - put_data_global_file                                      #
# Owner - Visnu Badal                                              #
####################################################################
@publisher_permission
@login_required(login_url='/')
@csrf_exempt
@require_POST
def put_data_global_file(request):
    response_data = {}
    try:
        check_value = request.POST.getlist('checkedValues')
        data_type = request.POST.get('data_type')
        from ast import literal_eval

        #print len(check_value[0])
        if check_value and data_type == 'global' or data_type == 'wellness' or  data_type == 'health':
            # if len(check_value[0]) > 2:
            #     check_value = [item for value in check_value for item in literal_eval(value)]
            # else:
            #     check_value = [check_value[0]]
            check_value = check_value[0].split(',')
            if data_type == 'global' :
                response = data_publisher("newsfeed", check_value,request)
            elif data_type == 'wellness' :
                response = data_publisher("newsfeed", check_value,request)
            elif data_type == 'health' :
                response = data_publisher("newsfeed", check_value,request)
            if response is True:
                response_data['Message'] = "Data has been sucessfully published"
    except Exception as e:
        response_data['Message'] = "Something Bad Happened Please Tr again"
        #print e
    response_data = json.dumps(response_data)
    return HttpResponse(response_data)

####################################################################
# Name - put_data_global_unpublish                                 #
# Owner - Visnu Badal                                              #
####################################################################
@publisher_permission
@login_required(login_url='/')
@csrf_exempt
@require_POST
def put_data_global_unpublish(request):
    response_data = {}
    try:
        check_value = request.POST.getlist('checkedValues')
        data_type = request.POST.get('data_type')
        from ast import literal_eval
        #print len(check_value[0])
        if check_value and data_type == 'global' or data_type == 'wellness' or data_type == 'health':
            # if len(check_value[0]) > 2:
            #     check_value = [item for value in check_value for item in literal_eval(value)]
            # else:
            #     check_value = [check_value[0]]
            check_value = check_value[0].split(',')
            response = data_un_publisher("newsfeed", check_value,request)
            if response is True:
                response_data['Message'] = "Data has been successfully unpublished"
            else:
                response_data['Message'] = "Something Bad Happened Please Try again"

    except Exception as e:
        response_data['Message'] = "Something Bad Happened Please Try again"
        #print e
    response_data = json.dumps(response_data)
    return HttpResponse(response_data)

####################################################################
# Name - search_news_by_stages_by_publisher                        #
# Owner - Visnu Badal                                              #
####################################################################
@publisher_permission
@login_required(login_url='/')
@csrf_exempt
def search_news_by_stages_by_publisher(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            t = request.POST['formDATA[t]']
            results = []
            if q is not None and t is not '':
                if t == 'global':
                    results = NewsFeed.objects.filter(Q(stage_id=q) & Q(news_type=1),Q(blocked_news=False)).order_by('news_header')
                elif t == 'wellness':
                    results = NewsFeed.objects.filter(Q(stage_id=q) & Q(news_type=2),Q(blocked_news=False)).order_by('news_header')
                elif t == 'health':
                    results = NewsFeed.objects.filter(Q(stage_id=q) & Q(news_type=3), Q(blocked_news=False)).order_by(
                        'news_header')
            results = paginate(results, 50)
            html = render_to_string('news/publisher/global/search_global_publisher.html',
                                    {'tab': 'publish_doctor_data', 'publisher_data': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404
""" Search for admin and other user"""

####################################################################
# Name - search_global_news_admin                                  #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_global_news_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q != '':
                results = NewsFeed.objects.filter(Q(topic_title__icontains=q) & Q(news_type=1)).order_by('topic_title')
            else:
                results = NewsFeed.objects.filter(news_type=1).order_by('topic_title')
            results = paginate(results, 100)
            html = render_to_string('news/assign/search_global_admin.html',
                                    {'admin_news_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_wellness_news_admin                                #
# Owner - Visnu Badal                                              #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_wellness_news_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q != '':
                results = NewsFeed.objects.filter(Q(topic_title__icontains=q) & Q(news_type=2)).order_by('topic_title')
            else:
                results = NewsFeed.objects.filter(news_type=2).order_by('topic_title')
            results = paginate(results, 100)
            html = render_to_string('news/assign/search_wellness_admin.html',
                                    {'admin_news_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_health_news_admin                                  #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_health_news_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q != '':
                results = NewsFeed.objects.filter(Q(topic_title__icontains=q) & Q(news_type=3)).order_by('topic_title')
            else:
                results = NewsFeed.objects.filter(news_type=3).order_by('topic_title')
            results = paginate(results, 100)
            html = render_to_string('news/assign/search_health_admin.html',
                                    {'admin_news_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

from hfu_cms.models import AssociateDoctorWithOrganization
import csv

@require_GET
def get_data(request):
    objects = AssociateDoctorWithOrganization.objects.all()
    with open('associate.csv', 'w') as csvfile:
        fieldnames = ['organisation', 'doctor', 'department']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in objects:
            try:
                writer.writerow(
                    {'doctor': i.doctor.name, 'organisation': i.organisation.name, 'department': i.department.name})
            except Exception as e:

                pass



@login_required(login_url='/')
def publish_news_to_live(request):
    try:

        if request.method == 'POST' :
            sn = 5
            news_id = request.POST.get('news_id')

            #data_obj = edit_rights(news_id, request, 2)

            #data_obj  = NewsFeed.objects.filter(id=news_id, current_user_id=request.user.id)
            data_obj = NewsFeed.objects.get(id=news_id, current_user_id=request.user.id)
            if data_obj is not False:
                data_obj.stage_id = sn #Stage.objects.get(pk=5)
                data_obj.save()
                messages.success(request,"News Successfully Published")
                if data_obj.news_type == NewsTypeMaster.objects.get(pk=1) :
                    return HttpResponseRedirect(reverse('get-publish-global-feed'))
                elif data_obj.news_type == NewsTypeMaster.objects.get(pk=2) :
                    return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
                elif data_obj.news_type == NewsTypeMaster.objects.get(pk=3) :
                    return HttpResponseRedirect(reverse('get-publish-health-feed'))
                else :
                    return HttpResponseRedirect(reverse('users-dashboard'))
            else:
                messages.error(request, 'You have not rights to edit this document')

    except Exception as e:

        messages.error(request, 'Something Bad 555 Happened')
    return HttpResponseRedirect(reverse('wellness-listing'))

####################################################################
# Name - Wellness_data_by_users                                    #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def wellness_data_by_users(request):
    try:
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            user_data_obj = UserManagement.objects.all()
            wellness_all_data = NewsFeed.objects.filter(current_user_id=search_data,news_type=2).order_by('topic_title')
            paginator = Paginator(wellness_all_data, 100)
            page = request.GET.get('page')
            try:
                wellness_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                wellness_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                wellness_all_data = paginator.page(paginator.num_pages)

            return render(request, 'news/by_user/wellness_by_user.html',
                      {'tab': 'news_data', 'crosal': 'wellnessbymanage', 'wellness_all_data': wellness_all_data,
                       'user_data_obj': user_data_obj,'search_data':search_data})
        wellness_all_data = NewsFeed.objects.filter(news_type=2).order_by('topic_title')
        user_data_obj = UserManagement.objects.all()
        paginator = Paginator(wellness_all_data, 100)
        page = request.GET.get('page')
        try:
            wellness_all_data= paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            wellness_all_data= paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            wellness_all_data= paginator.page(paginator.num_pages)
        return render(request, 'news/by_user/wellness_by_user.html',
                      {'tab': 'news_data', 'crosal': 'wellnessbymanage', 'wellness_all_data': wellness_all_data,
                       'user_data_obj': user_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - Wellness_data_by_users                                    #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_wellness_by_users_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(current_user_id=q,news_type=2).order_by('topic_title')
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/by_user/search_by_user_admin_wellness.html',
                                    {'tab': 'news_data', 'crosal': 'labbymanage',
                                     'wellness_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_wellness_by stage and user                         #
# Owner -  Nishank Gupta                                           #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_wellness_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(topic_title__icontains=q,news_type=2).order_by('topic_title')
            else:
                results = NewsFeed.objects.filter(news_type=2)
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/search_wellness_by_stage_user.html',
                                    {'tab': 'news_data', 'crosal': 'wellnessbymanage', 'wellness_all_data': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - global_data_by_users                                      #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def global_data_by_users(request):
    try:
        search_data=None
        search_data = request.GET.get('search_data')
        if search_data :
            user_data_obj = UserManagement.objects.all()
            global_all_data = NewsFeed.objects.filter(current_user_id=search_data,news_type=1).order_by('topic_title')
            paginator = Paginator(global_all_data, 100)
            page = request.GET.get('page')
            try:
                global_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                global_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                global_all_data = paginator.page(paginator.num_pages)
            return render(request, 'news/by_user/global_by_user.html',
                      {'tab': 'news_data', 'crosal': 'globalbymanage', 'global_all_data': global_all_data,
                       'user_data_obj': user_data_obj,'search_data':search_data})

        global_all_data = NewsFeed.objects.filter(news_type=1).order_by('topic_title')
        user_data_obj = UserManagement.objects.all()
        paginator = Paginator(global_all_data, 100)
        page = request.GET.get('page')
        try:
            global_all_data= paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            global_all_data= paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            global_all_data= paginator.page(paginator.num_pages)
        return render(request, 'news/by_user/global_by_user.html',
                      {'tab': 'news_data', 'crosal': 'globalbymanage', 'global_all_data': global_all_data,
                       'user_data_obj': user_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - health_data_by_users                                      #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def health_data_by_users(request):
    try:
        search_data = None
        search_data = request.GET.get('search_data')
        if search_data:
            user_data_obj = UserManagement.objects.all()
            health_all_data = NewsFeed.objects.filter(current_user_id=search_data, news_type=3).order_by('topic_title')

            paginator = Paginator(health_all_data, 100)
            page = request.GET.get('page')
            try:
                health_all_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                health_all_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                health_all_data = paginator.page(paginator.num_pages)
            return render(request, 'news/by_user/health_by_user.html',
                          {'tab': 'news_data', 'crosal': 'healthbymanage', 'health_all_data': health_all_data,
                           'user_data_obj': user_data_obj, 'search_data': search_data})
        health_all_data = NewsFeed.objects.filter(news_type=3).order_by('topic_title')
        user_data_obj = UserManagement.objects.all()
        paginator = Paginator(health_all_data, 100)
        page = request.GET.get('page')
        try:
            health_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            health_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            health_all_data = paginator.page(paginator.num_pages)
        return render(request, 'news/by_user/health_by_user.html',
                      {'tab': 'news_data', 'crosal': 'healthbymanage', 'health_all_data': health_all_data,
                       'user_data_obj': user_data_obj})
    except Exception as e:
        raise Http404

####################################################################
# Name - global_data_by_users                                      #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_global_by_users_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(current_user_id=q,news_type=1).order_by('topic_title')
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/by_user/search_by_user_admin_global.html',
                                    {'tab': 'news_data', 'crosal': 'labbymanage',
                                     'global_all_data': results,'search_data':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - health_data_by_users                                      #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_health_by_users_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(current_user_id=q, news_type=3).order_by('topic_title')
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/by_user/search_by_user_admin_health.html',
                                    {'tab': 'news_data', 'crosal': 'labbymanage',
                                     'health_all_data': results, 'search_data': q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_global_by stage and user                           #
# Owner -  Nishank Gupta                                           #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_global_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(topic_title__icontains=q,news_type=1)
            else:
                results = NewsFeed.objects.filter(news_type=1)
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/search_global_by_stage_user.html',
                                    {'tab': 'news_data', 'crosal': 'globalbymanage', 'global_all_data': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_health_by stage and user                           #
# By-  Nishank Gupta                                               #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_health_admin_on_stage_user(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(topic_title__icontains=q, news_type=3).order_by('topic_title')
            else:
                results = NewsFeed.objects.filter(news_type=3)
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/search_health_by_stage_user.html',
                                    {'tab': 'news_data', 'crosal': 'healthbymanage', 'health_all_data': results})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - Wellness_data_by_stages                                   #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def wellness_data_by_stages(request):
    try:
        stage_id = request.GET.get('stage_id')
        if stage_id:
            wellness_all_data = NewsFeed.objects.filter(news_type = 2,stage_id=stage_id).order_by('topic_title')
        else:
            wellness_all_data = NewsFeed.objects.filter(news_type = 2).order_by('topic_title')
            stage_id = None
        stage_data = Stage.objects.all()
        paginator = Paginator(wellness_all_data, 100)
        page = request.GET.get('page')
        try:
            wellness_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            wellness_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            wellness_all_data = paginator.page(paginator.num_pages)
        return render(request, 'news/by_stages/wellness_by_stages.html',
                      {'tab': 'news_data', 'crosal': 'wellnessbymanage', 'wellness_all_data': wellness_all_data,
                       'stage_data': stage_data,'stage_no':stage_id})
    except:
        raise Http404

####################################################################
# Name - global_data_by_stages                                     #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def global_data_by_stages(request):
    try:
        stage_id = request.GET.get('stage_id')
        if stage_id:
            global_all_data = NewsFeed.objects.filter(news_type = 1,stage_id=stage_id).order_by('topic_title')
        else:
            global_all_data = NewsFeed.objects.filter(news_type = 1).order_by('topic_title')
            stage_id = None
        stage_data = Stage.objects.all()
        paginator = Paginator(global_all_data, 100)
        page = request.GET.get('page')
        try:
            global_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            global_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            global_all_data = paginator.page(paginator.num_pages)

        return render(request, 'news/by_stages/global_by_stages.html',
                      {'tab': 'news_data', 'crosal': 'globalbymanage', 'global_all_data': global_all_data,
                      'stage_data': stage_data,'stage_no':stage_id})
    except Exception as e:
        raise Http404

####################################################################
# Name - health_data_by_stages                                     #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@require_GET
def health_data_by_stages(request):
    try:
        stage_id = request.GET.get('stage_id')
        if stage_id:
            health_all_data = NewsFeed.objects.filter(news_type=3, stage_id=stage_id).order_by('topic_title')
        else:
            health_all_data = NewsFeed.objects.filter(news_type=3).order_by('topic_title')
            stage_id = None
        stage_data = Stage.objects.all()
        paginator = Paginator(health_all_data, 100)
        page = request.GET.get('page')
        try:
            health_all_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            health_all_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            health_all_data = paginator.page(paginator.num_pages)

        return render(request, 'news/by_stages/health_by_stages.html',
                      {'tab': 'news_data', 'crosal': 'healthbymanage', 'health_all_data': health_all_data,
                       'stage_data': stage_data, 'stage_no': stage_id})
    except Exception as e:
        raise Http404

####################################################################
# Name - search_wellness_by_stages_by_admin                        #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_wellness_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(stage_id=q,news_type =2).order_by('topic_title')
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/by_stages/search_wellness_stages.html',
                                    {'tab': 'news_data', 'crosal': 'wellnessbymanage', 'wellness_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_global_by_stages_by_admin                          #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_global_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(stage_id=q,news_type =1).order_by('topic_title')
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/by_stages/search_global_stages.html',
                                    {'tab': 'news_data', 'crosal': 'globalbymanage', 'global_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

####################################################################
# Name - search_health_by_stages_by_admin                          #
# By - Nishank                                                     #
####################################################################
@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def search_health_by_stages_by_admin(request):
    try:
        if request.method == 'POST':
            q = request.POST['formDATA[q]']
            results = []
            if q is not None:
                results = NewsFeed.objects.filter(stage_id=q,news_type =3).order_by('topic_title')
            paginator = Paginator(results, 100)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/by_stages/search_health_stages.html',
                                    {'tab': 'news_data', 'crosal': 'healthbymanage', 'health_all_data': results,
                                     'stage_no':q})
            return HttpResponse(html)
    except Exception as e:
        raise Http404

######################################################################
# Name - newstype_master_data                                        #
# By - Nishank                                                       #
######################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def newstype_master_data(request):
    try:
        if request.method == "GET":
            newstype_master = NewsTypeMaster.objects.all().order_by('name')
            paginator = Paginator(newstype_master, 100)
            page = request.GET.get('page')
            try:
                newstype_master = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                newstype_master = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                newstype_master = paginator.page(paginator.num_pages)

            return render(request, 'admin/master_data_management/newstype_master_data_management.html',
                          {'newstype_master': newstype_master})
    except Exception as e:
        raise Http404

####################################################################
# Name - newstype_master_add_edit                                  #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
def newstype_master_add_edit(request, newstype_master_id=None):
    try:
        if newstype_master_id != None:
            admin_action = 'Edit'
            if request.method == "GET":
                type_obj = NewsTypeMaster.objects.get(id=newstype_master_id)
                return render(request, 'admin/master_data_management/newstype_master_add_edit.html',
                              {'type_obj': type_obj, 'admin_action': admin_action})
            elif request.method == "POST":
                name = request.POST['type_name'].strip()
                if 'active' in request.POST:
                    status = request.POST['active'].strip()
                else:
                    status = 'not found'
                if name:
                    type_obj = NewsTypeMaster.objects.get(id=newstype_master_id)
                    type_obj.name = name
                    if status == '11':
                        type_obj.delete = False
                    else:
                        type_obj.delete = True
                    type_obj.save()
                    messages.success(request, "News Master Type edited successfully")
                    return redirect('newstype_master_data_page')
                else:
                    messages.error(request, "Please provide name")
                    return redirect(reverse("newstype_master_edit", args=[newstype_master_id, ]))
        else:
            admin_action = 'Add'
            if request.method == "GET":
                return render(request, 'admin/master_data_management/newstype_master_add_edit.html',
                              {'admin_action': admin_action})

            elif request.method == "POST":
                name = request.POST['type_name'].strip()
                if 'active' in request.POST:
                    status = request.POST['active'].strip()
                else:
                    status = 'not found'
                if name:
                    new_object = NewsTypeMaster(name=name)
                    if status == '11':
                        new_object.delete = False
                    else:
                        new_object.delete = True
                    new_object.save()
                    messages.success(request, "News Type Master added successfully")
                    return redirect('newstype_master_data_page')
                else:
                    messages.error(request, "Please provide name")
                    return redirect(reverse("newstype_master_add"))
    except Exception as e:
        raise Http404

####################################################################
# Name - DELETE Newsfeed                                           #
# Owner - Nishank                                                  #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def delete_newsfeed(request,newsfeed_id=None,newsfeed_type_id=None):
    try:
        if request.method == "POST":
            messages.error("Method not allowed")
            if request.user.is_superuser:
                if newsfeed_type_id == 1 :
                    return HttpResponseRedirect(reverse('get-assign-global-feed'))
                elif newsfeed_type_id == 2 :
                    return HttpResponseRedirect(reverse('get-assign-wellness-feed'))
                elif newsfeed_type_id == 3 :
                    return HttpResponseRedirect(reverse('get-assign-health-feed'))
            User_management_obj = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
            if (len(User_management_obj)):
                if newsfeed_type_id == 1 :
                    return HttpResponseRedirect(reverse('get-publish-global-feed'))
                elif newsfeed_type_id == 2 :
                    return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
                elif newsfeed_type_id == 3 :
                    return HttpResponseRedirect(reverse('get-publish-health-feed'))
            if newsfeed_type_id == 1 :
                return HttpResponseRedirect(reverse('global-listing'))
            elif newsfeed_type_id == 2 :
                return HttpResponseRedirect(reverse('wellness-listing'))
            elif newsfeed_type_id == 3 :
                return HttpResponseRedirect(reverse('health-listing'))

        elif request.method == "GET":
            if newsfeed_id and newsfeed_type_id:
                newsfeed_obj = get_object_or_404(NewsFeed,id=newsfeed_id,news_type_id=newsfeed_type_id)
                try:
                    file =  newsfeed_obj.newsfeed_docx_file.name
                    file_deleted = file + "_DELETED"
                    back_to = os.getcwd()
                    os.chdir(settings.DOCX_PATH_NEWSFEED)
                    os.rename(file,file_deleted)
                    image = settings.DOCX_PATH_NEWSFEED +'/' + newsfeed_obj.newsfeed_image_file_name
                    image_deleted = settings.DOCX_PATH_NEWSFEED +'/' + newsfeed_obj.newsfeed_image_file_name + "_DELETED"
                    os.rename(image, image_deleted)
                    os.chdir(back_to)
                    print("Files Removed!")
                except Exception as e:
                    print e
                    print("Failed!")

                newsfeed_obj.delete()
                messages.success(request,"Successfully Deleted Newsfeed Article")
                if request.user.is_superuser:
                    if newsfeed_type_id == '1' :
                        return HttpResponseRedirect(reverse('get-assign-global-feed'))
                    elif newsfeed_type_id == '2' :
                        return HttpResponseRedirect(reverse('get-assign-wellness-feed'))
                    elif newsfeed_type_id == '3' :
                        return HttpResponseRedirect(reverse('get-assign-health-feed'))

                User_management_obj = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                if (len(User_management_obj)):
                    if newsfeed_type_id == '1' :
                        return HttpResponseRedirect(reverse('get-publish-global-feed'))
                    elif newsfeed_type_id == '2' :
                        return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
                    elif newsfeed_type_id == '3' :
                        return HttpResponseRedirect(reverse('get-publish-health-feed'))

                if newsfeed_type_id == '1' :
                    return HttpResponseRedirect(reverse('global-listing'))
                elif newsfeed_type_id == '2' :
                    return HttpResponseRedirect(reverse('wellness-listing'))
                elif newsfeed_type_id == '3' :
                    return HttpResponseRedirect(reverse('health-listing'))

            else:
                messages.error("MISSING Newsfeed and / or Newsfeed type ID")
                if request.user.is_superuser:
                    if newsfeed_type_id == 1 :
                        return HttpResponseRedirect(reverse('get-assign-global-feed'))
                    elif newsfeed_type_id == 2 :
                        return HttpResponseRedirect(reverse('get-assign-wellness-feed'))
                    elif newsfeed_type_id == 3 :
                        return HttpResponseRedirect(reverse('get-assign-health-feed'))

                User_management_obj = UserManagement.objects.filter(user_id=request.user.id, is_publisher=True)
                if (len(User_management_obj)):
                    if newsfeed_type_id == 1 :
                        return HttpResponseRedirect(reverse('get-publish-global-feed'))
                    elif newsfeed_type_id == 2 :
                        return HttpResponseRedirect(reverse('get-publish-wellness-feed'))
                    elif newsfeed_type_id == 3 :
                        return HttpResponseRedirect(reverse('get-publish-health-feed'))

                if newsfeed_type_id == 1 :
                    return HttpResponseRedirect(reverse('global-listing'))
                elif newsfeed_type_id == 2 :
                    return HttpResponseRedirect(reverse('wellness-listing'))
                elif newsfeed_type_id == 3 :
                    return HttpResponseRedirect(reverse('health-listing'))

    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - global_by_name_publisher                                  #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def global_by_name_publisher(request):
    try:
        if request.method == 'POST':
            search_name =  None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = NewsFeed.objects.filter(current_user_id=user_id, topic_title__icontains=q,activation_status=True,
                                                  blocked_news=False, news_type_id = 1).order_by('topic_title')
            elif user_id:
                #results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
            paginator = Paginator(results, 50)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            html = render_to_string('news/publisher/global/search_global_by_name_publisher.html',
                                    {'publisher_data': results, 'search_data':q,'tab_listing': 'global_listing',
                                     'tab': 'news_data'})
            return HttpResponse(html)
    except Exception as e:
        #print e
        raise Http404

####################################################################
# Name - wellness_by_name_publisher                                #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def wellness_by_name_publisher(request):
    try:
        if request.method == 'POST':
            search_name = None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = NewsFeed.objects.filter(current_user_id=user_id, topic_title__icontains=q,
                                                  activation_status=True,
                                                  blocked_news=False, news_type_id=2).order_by('topic_title')
            elif user_id:
                # results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
            paginator = Paginator(results, 50)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            # We reuse the same temp[late for global everywhere
            html = render_to_string('news/publisher/wellness/search_wellness_by_name_publisher.html',
                                    {'publisher_data': results, 'search_data': q, 'tab_listing': 'wellness_listing',
                                     'tab': 'news_data'})
            return HttpResponse(html)
    except Exception as e:
        # print e
        raise Http404

####################################################################
# Name - health_by_name_publisher                                  #
# By Nishank                                                       #
####################################################################
@login_required(login_url='/')
@csrf_exempt
def health_by_name_publisher(request):
    try:
        if request.method == 'POST':
            search_name = None
            q = request.POST['formDATA[q]']
            user_id = request.POST['formDATA[user_id]']
            results = []
            if user_id and q is not None:
                results = NewsFeed.objects.filter(current_user_id=user_id, topic_title__icontains=q,
                                                  activation_status=True,
                                                  blocked_news=False, news_type_id=3).order_by('topic_title')
            elif user_id:
                # results = Doctor.objects.filter(current_user_id=user_id, is_disable=False).order_by('name')
                results = []
            paginator = Paginator(results, 50)
            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                results = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                results = paginator.page(paginator.num_pages)
            # We reuse the same temp[late for global everywhere
            html = render_to_string('news/publisher/health/search_health_by_name_publisher.html',
                                    {'publisher_data': results, 'search_data': q, 'tab_listing': 'health_listing',
                                     'tab': 'news_data'})
            return HttpResponse(html)
    except Exception as e:
        # print e
        raise Http404


###################################################
# name = Doctors news feed listing                #
# owner = Ashutosh Kesharvani                     #
###################################################
@csrf_exempt
@login_required(login_url='/')
def doctors_feed_listing(request):
    try:
        obj = Doctorsfeed.objects.all()
        return render(request,'news/doctors_feed/doctorsfeed_admin_listing.html',{'doctors_feed':obj})
    except Exception as e:
        print e

###################################################
# name = Doctors news feed listing                #
# owner = Ashutosh Kesharvani                     #
###################################################
@csrf_exempt
@login_required(login_url='/')
def publisher_doctorsfeed_listing(request):
    try:
        obj = Doctorsfeed.objects.filter(current_user_id = request.user.id)
        return render(request, 'news/doctors_feed/doctorsfeed_publisher_listing.html', {'doctors_feed': obj})
    except Exception as e:
        print e

###################################################
# name = Doctors news feed listing                #
# owner = Ashutosh Kesharvani                     #
###################################################
@csrf_exempt
@login_required(login_url='/')
def users_doctorsfeed_listing(request):
    try:
        obj = Doctorsfeed.objects.filter(current_user_id = request.user.id)
        return render(request, 'news/doctors_feed/doctorsfeed_users_listing.html', {'doctors_feed': obj})
    except Exception as e:
        print e


###################################################
# name = Doctors news feed listing                #
# owner = Ashutosh Kesharvani                     #
###################################################
@csrf_exempt
@login_required(login_url='/')
def edit_doctors_feed(request,feed_id = None):
    try:
        if request.method == 'GET' and feed_id is not None:
            if request.user.is_superuser:
                doctor_articles = NewsFeed.objects.all()
            else:
                doctor_articles = NewsFeed.objects.filter(activation_status=True,blocked_news=False).order_by('topic_title')
            news_type_obj = NewsTypeMaster.objects.all()
            obj = Doctorsfeed.objects.get(id=feed_id)
            cat_obj = Category.objects.all()
            return render(request,'news/doctors_feed/edit_doctorsfeed.html',{'doctors_feed':obj,'category_obj':cat_obj,'other_articles':doctor_articles,'news_type_obj':news_type_obj})

        if request.method == 'POST' and feed_id is not None:
            page_title = request.POST['page_title']
            page_keywords = request.POST['page_keywords']
            page_description = request.POST['page_description']
            news_type = request.POST['news_type']
            n_id = int(news_type )
            n_obj = NewsTypeMaster.objects.get(id=n_id)
            try:
                small_description = request.POST['small_description'].strip()
            except:
                small_description = ''
            try:
                publish_date = request.POST['publish_date'].strip()
                import datetime
                # publish_date = datetime.strptime('02/11/2010', '%d/%m/%Y').strftime('%d-%m-%Y')

                day, month, year = publish_date.split('-')
                publish_date = datetime.date(int(year), int(month), int(day))
            except Exception as e:
                # print e
                print 2
            related_topics = request.POST.getlist('related_topics')
            tag_string = request.POST['tag_string'].strip()
            newsfeed_html_refined = request.POST['newsfeed_html_refined'].strip()
            topic_title = request.POST['topic_title'].strip()
            # doctors_category = request.POST['doctors_category'].strip()
            # doctors_category = request.POST.getlist('category')
            # tmpstr1 = ''
            # counter = 0
            # if doctors_category and doctors_category != []:
            #     counter += 1
            #     for i in doctors_category:
            #         if counter == 1:
            #             tmpstr1 = tmpstr1 + i
            #             counter += 1
            #         else:
            #             tmpstr1 = tmpstr1 + ',' + i
            #             counter += 1
            #     doctors_category = tmpstr1
            # else:
            #     doctors_category = ''

            tmpstr1 = ''
            counter = 0
            if related_topics and related_topics != []:
                counter += 1
                for i in related_topics:
                    if counter == 1:
                        tmpstr1 = tmpstr1 + i
                        counter += 1
                    else:
                        tmpstr1 = tmpstr1 + ',' + i
                        counter += 1
                related_topics = tmpstr1
            else:
                related_topics = ''
            docfeed_obj = Doctorsfeed.objects.get(id=feed_id)
            if docfeed_obj:
                docfeed_obj.topic_title = topic_title
                # docfeed_obj.doctors_category = doctors_category
                docfeed_obj.tag_string = tag_string
                docfeed_obj.related_topics = related_topics
                docfeed_obj.newsfeed_html_refined = newsfeed_html_refined
                docfeed_obj.publish_date = publish_date
                docfeed_obj.small_description = small_description
                docfeed_obj.page_title = page_title
                docfeed_obj.page_keywords = page_keywords
                docfeed_obj.page_description = page_description
                docfeed_obj.news_type = n_obj
                docfeed_obj.save()
                messages.success(request, 'Doctor NewsFeed Data Successfully Updated')
                return redirect(reverse('edit_doctors_feed', args=[feed_id]))
    except Exception as e:
        print e

###################################################
# name = publish unpublish doctors feed           #
# owner = Ashutosh Kesharvani                     #
###################################################
@csrf_exempt
@login_required(login_url='/')
def publish_unpublish_docsfeed(request):
    response_data = {}
    try:
        check_value = request.POST.getlist('checkedValues')
        data_type = request.POST.get('data_type')
        type = request.POST.get('type')

        if type == 'publish':
            if check_value :
                check_value = check_value[0].split(',')
                response = data_publisher("docsfeed",check_value, request)
                if response is True:
                    response_data['Message'] = "Data has been sucessfully published"

        elif type == 'un-publish':
            if check_value :
                check_value = check_value[0].split(',')
                response = data_un_publisher("docsfeed", check_value, request)
                if response is True:
                    response_data['Message'] = "Data has been sucessfully un published"
    except Exception as e:
        response_data['Message'] = "Something Bad Happened Please Tr again"
        # print e
    response_data = json.dumps(response_data)
    return HttpResponse(response_data)