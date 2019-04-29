from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    def word_dictionary(list):
        result = {}
        for word in list:
            if not word in result:
                result[word] = 1
            else:
                result[word] += 1
        return result
    word_count = word_dictionary(word_list)

    return render(request, 'count.html',{'fulltext':full_text, 'total': len(word_list), 'countWord': word_count})