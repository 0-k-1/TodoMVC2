from django.shortcuts import render,redirect
from App.models import Todo
import json
# from django.forms.models import model_to_dict

def todoMVC_view(request):
    # list=[{"content":"任务1","completed":"True"},{"content":"任务2","completed":"False"}]

    # list=[
    #         {"completed": "false","id": "1","title": "31"},
    #         {"completed": "true","id": "2","title": "35"},
    #         {"completed": "true","id": "0","title": "32"}
    # ]

    # list_value = list.values()
    # list = model_to_dict(list[0])
    # print(list_value)
    ls = Todo.objects.all()
    ls = list(ls.values())
    print(ls)
    return render(request, 'VueExample.html', {"list":json.dumps(ls)})
    #return render(request, 'VueExample.html', {"list":list})

def save_view(request):
    print(request.POST['q'])
    # print(request.body)
    # print(type(request.body))
    # print(request.body.decode())
    # para = json.loads(request.body.decode())
    # print(para)

    # 直接覆盖
    ls = Todo.objects.all()
    ls.delete()
    for item in json.loads(request.POST['q']):
        Todo.objects.create(title=item['title'], completed=item['completed'])

        # 删除不起作用
        # try:
        #     for k in item.keys():
        #         print(k,item[k])
        #     Todo.objects.update_or_create(id=item['id'],
        #                                   defaults={'id': item['id'], 'title': item['title'],
        #                                             'completed': item['completed']})
        # except:
        #     pass
    #return render(request, 'VueExample.html')
    return redirect('/')