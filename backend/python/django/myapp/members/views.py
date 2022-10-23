from django.http import HttpResponse, HttpResponseRedirect #1
from django.template import loader
from django.urls import reverse #2
from .models import Members

# Create your views here.
def index(request):
    """ 
        models.object.all().values(column,column2,.....)  //multi column
        models.object.all().values_list(column,flat=true) //specific column
    """     
    myMemberData= Members.objects.all().values()
    template = loader.get_template('member.html')
    dataContent= {
        'myMemberData':myMemberData,
    }
    return HttpResponse(template.render(dataContent,request)) #回傳template
    
    # 直接顯示字串
    # myMemberData= Members.objects.all().values('id','firstName','lastName')
    # output=""
    # for x in myMemberData:
    #     output += x["firstName"] + ","
    # print(output)    
    # return HttpResponse(output)    

    # 使用template
    # template = loader.get_template('member.html')
    # return HttpResponse(template.render()) #回傳template
    # return HttpResponse("Hello World!") #回傳字串到前端

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request)) #回傳template

def addRecord(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    member = Members(firstName=firstName,lastName=firstName)
    member.save()
    return HttpResponseRedirect(reverse('index')) #藉由導路由方式決定跳轉頁面

def update(request,id):
    memberData = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    dataContent= {
        'memberData':memberData,
    }
    return HttpResponse(template.render(dataContent,request)) #回傳template

def updateRecord(request,id):
    memberData = Members.objects.get(id=id)
    memberData.firstName= request.POST['firstName']
    memberData.lastName = request.POST['lastName']
    memberData.save()
    return HttpResponseRedirect(reverse('index')) #藉由導路由方式決定跳轉頁面

def deleteRecord(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index')) #藉由導路由方式決定跳轉頁面