from django.views.generic import ListView
from django.views import View
from django.shortcuts import render,redirect
from searching.models import Category, SearchingData, UnknownSearch, CommentAnalysis
import nltk
from django.core.paginator import Paginator
nltk.download('stopwords')
nltk.download('punkt')
from searching.ProjectFunctionality.Preprocessing import Preprocess as pre
import searching.ProjectFunctionality.CommentAnlysis as CA

# Create your views here.
class HomePageView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'Category'


class FeedbackView(View):
    def get(self, request):
        return render(request, 'feedbackPage.html', {})


class SearchResultsView(ListView):
    model = SearchingData
    template_name = 'search_results.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['Category'] = Category.objects.all()
        return context

    def get_queryset(self):  # new
       # variables initiolaization
        query = self.request.GET.get('q').lower()
        q2 = self.request.GET.get('drop1')
        object_list1 = SearchingData.objects.filter(ID__ID=q2)
        object_list = list()

       # searching query
        newstring = preprocessing(query).strip()
        oldstring = pre.limitazation(newstring).strip()
        for data in object_list1:
            if newstring in data.Name.lower() or newstring in data.Description:
                object_list.append(data)
        for data in object_list1:
            if oldstring in data.Name.lower() or oldstring in data.Description:
                object_list.append(data)
        if len(object_list) != 0:
            return set(object_list)
        else:
            object_list = pre.ifNoResult(object_list1, newstring, oldstring)
            Un1 = UnknownSearch(Name=query, num=q2)
            Un1.save()
            return set(object_list)

#Preprocess function
def preprocessing(query):
    temp = pre.cleanSymbol(query)
    temp = pre.reduce_lengthening(temp)
    temp = pre.wildcard(temp)
    temp = temp.split(' ')
    newstring = str()
    for index in range(len(temp)):
        if temp[index] != pre.spellChecker(temp[index]):
            newstring += pre.spellChecker(temp[index]) + " "
        else:
            newstring += temp[index] + " "
    newstring = pre.stopWord(newstring)
    return newstring

#analize comments and add it to database
def commentredirect(request):
    if request.method == "POST":
        com = CommentAnalysis()
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('text')
        status = CA.predict(comment)
        com = CommentAnalysis(Name=name, Email=email, comment=comment, status=status)
        com.save()
        return redirect('http://127.0.0.1:8000/')