from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import redirect
from django.http import JsonResponse

# Create your views here.
class Index(View):
    template_name = "inventory/index.html"
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)




def update(request):
    response_data = {}
    # post request to update the database periodically for a specific item
    if request.method == 'POST':
        # # get the item id from the request
        # item_id = request.POST.get('item_id')

        # # get the item from the database
        # item = Item.objects.get(id=item_id)

        # # update the item
        # item.update()

        # redirect to the item's page
        response_data['item'] = 'item'
        response_data['success'] = 'Item updated successfully'
        return JsonResponse(response_data)


    
