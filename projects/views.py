from django.shortcuts import render
from django.http import HttpResponse

projects_List = [
    {
        'id': 1,
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': 2,
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': 3,
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    page = 'projects'
    number = 10
    context = {'page':page, 'number':number, 'projects':projects_List}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project_obj = None
    print('Given ID:' , pk)
    for i in projects_List:
        print('Object ', i['id'])
        if i['id'] == pk:
            print('I am object', pk)
            project_obj = i  
    print('Object:', project_obj)
    return render(request, 'projects/single-project.html', {'project': project_obj})