from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import product,productManager
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned

# Create your views here.

# 1st way using class based view
class productlistview(ListView):
    queryset=product.objects.all()
    template_name="products/list.html"



class productfeaturedlistview(ListView):
    queryset=product.objects.all()
    template_name="products/list.html"
    def get_queryset(self,*args,**kwargs):
        request=self.request
        return product.objects.featured()




class productfeaturedDetailview(DetailView):
    queryset=product.objects.all()
    template_name="products/featured-detail.html"
    def get_queryset(self,*args,**kwargs):
        request=self.request
        return product.objects.featured()







# using function based value (fbv)
def product_list_view(request):
    queryset=product.objects.all()
    context={

'object_list':queryset

    }    
    return render(request,"products/list.html",context)


class productdetailslugview(DetailView):
    queryset=product.objects.all()

    template_name="products/detail.html"



    def get_object(self,*args,**kwargs):
        request=self.request
        slug=self.kwargs.get('slug')
        try:
            instance=product.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise Http404("not found....")
        except MultipleObjectsReturned:
            qs=product.objects.filter(slug=slug)
            instance=qs.first()
        except:
            raise Http404("huh")
        
        return instance


    

class productdetailview(DetailView):
    queryset=product.objects.all()

    template_name="products/detail.html"

    def get_object(self,*args,**kwargs):
        request=self.request
        pk=self.kwargs.get('pk')
        instance=product.objects.getbyid(pk)
        return instance
# using function based value (fbv)
def product_detail_view(request,pk=None,*args,**kwargs):
    
    instance=product.objects.getbyid(pk)
    print(instance)





    context={'object':instance}    
    return render(request,"products/detail.html",context)
