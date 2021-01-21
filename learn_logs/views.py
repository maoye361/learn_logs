from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.urls import reverse
from .models import Topic,Entry,Addfile
from .forms import TopicFrom,EntryFrom,AddfileFrom
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.forms.models import model_to_dict
from django.core.cache import cache
# Create your views here.
def index(request):
    return render(request,'learn_logs/index.html')
@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    files = Addfile.objects.filter(owner=request.user)
    context = {'topics': topics,'files':files}
    return render(request,'learn_logs/topics.html',context=context)
@csrf_exempt
def topics_json(request):
    if request.method == 'POST':
        name = request.POST.get('topic_id',0)
        topics = Topic.objects.filter(id=name).order_by('date_added')
        datas = []
        for topic in topics:
            data = {
                'topic_id': topic.id,
                'topic': topic.text,
                'topic_date':str(topic.date_added),
                'name':name
            }
            datas.append(data)
        return HttpResponse(json.dumps(datas),content_type='application/json')
    else:
        return HttpResponse('pls use post',content_type='application/json')
@login_required
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    print(topic)
    #topicall = Topic.objects.all().exists()
    #print(topicall)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries':entries}
    return render(request,'learn_logs/topic.html',context=context)
@login_required
def titles(request):
    titles = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,'learn_logs/titles.html',context=context)
@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicFrom()
    else:
        form = TopicFrom(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learn_logs:topics'))
    context = {'form': form}
    return render(request,'learn_logs/new_topic.html',context=context)
@login_required
def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryFrom
    else:
        form = EntryFrom(data=request.POST)
        if form.is_valid():
            new_entries = form.save(commit=False)
            new_entries.topic = topic
            new_entries.save()
            return HttpResponseRedirect(reverse('learn_logs:topic',args=[topic_id]))
    context = {'topic':topic ,'form': form}
    return render(request,'learn_logs/new_entry.html',context=context)
@login_required
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryFrom(instance=entry)
    else:
        form = EntryFrom(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learn_logs:topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic ,'form': form}
    return render(request,'learn_logs/edit_entry.html',context=context)
@login_required
def delete_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    entry.delete()
    return HttpResponseRedirect(reverse('learn_logs:topic',args=[topic.id]))
def delete_topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return HttpResponseRedirect(reverse('learn_logs:topics'))
def write_cache(request):
    cache.set('zz','222',10)
    print(cache.has_key('zz'))
    return HttpResponse('ok')
@login_required
def addfile(request):
    if request.method != 'POST':
        form = AddfileFrom()
    else:
        form = AddfileFrom(request.POST,request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.owner = request.user
            new_file.save()
        return HttpResponseRedirect(reverse('learn_logs:index'))
    return render(request,'learn_logs/addfile.html',{'form':form})


