from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.conf import settings
import mimetypes
from django.utils.encoding import smart_str
from .models import Hardware, Contract, Software

from django.http import JsonResponse, Http404, HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

import datetime as dt

# Create your views here.
class Index(View):
    template_name = "inventory/hardware.html"
    def get(self, request, *args, **kwargs):
        # read data from database and pass it to the template
        hardware = Hardware.objects.all().values()
        contract = Contract.objects.all().values()
        software = Software.objects.all().values()
        context = {
            'hardware': hardware,
            'contract': contract,
            'software': software,
            'upkeep': 40000,
        }
        print(context['hardware'])
       
        return render(request, self.template_name, context)




class HardwareListView(View):
    template_name = "inventory/hardwares.html"
    def get(self, request, *args, **kwargs):
        context = {'hardware' : Hardware.objects.all().values()}

        return render(request, self.template_name, context)

class HardwareDetailedView(View):
    template_name = "inventory/hardware_detail.html"
    def get(self, request, *args, **kwargs):
        rowid = kwargs['rowid']
        # hardware = Hardware.objects.filter(hostname=str(hostname)).values()
        # context = {'hardware' : Hardware.objects.filter(hostname=hostname).values()}
        # return render(request, self.template_name, context)
        print(rowid)
        for hardware in Hardware.objects.all():
            if hardware.rowid == rowid:
                context = {'hardware' : hardware}
                return render(request, self.template_name, context)
        
        return render(request, self.template_name, context)
    
    def delete(self, request, *args, **kwargs):
        rowid = kwargs['rowid']
        print(rowid)
        for hardware in Hardware.objects.all():
            if hardware.rowid == rowid:
                print("Found")
                # hardware.delete()
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})



class HardwareEdit(View):


    def post(self, request, *args, **kwargs):
        rowid = kwargs['rowid']
        for hardware in Hardware.objects.all():
            if hardware.rowid == rowid:
                for key, value in request.POST.items():
                    if key == 'csrfmiddlewaretoken':
                        continue
                    if key == 'rowid':
                        continue
                    if key == 'boottime':
                        continue
                    if key == 'transdate':
                        continue

                    setattr(hardware, key, value)
                    


                
                hardware.save()
                return redirect('hardware_detail', rowid=rowid)



class HardwareDelete(View):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        rowid = kwargs['rowid']
        print(rowid)
        for hardware in Hardware.objects.all():
            if hardware.rowid == rowid:
                print(rowid)
                hardware.delete()
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})






class SoftwareListView(View):
    template_name = "inventory/softwares.html"
    def get(self, request, *args, **kwargs):
        # read data from database and pass it to the template
        software = Software.objects.all().values()
        context = {
            'software': software,
        }
        print(context['software'])
       
        return render(request, self.template_name, context)

    @csrf_exempt  
    def post(self, request, *args, **kwargs):
        software = Software()

        for key, value in request.POST.items():
            print(key, value)
            if key == 'csrfmiddlewaretoken':
                continue
            if key == 'rowid':
                continue

            setattr(software, key, value)
        software.save()
        return redirect('inventory_softwares')

class SoftwareDetailedView(View):
    template_name = "inventory/software_detail.html"
    def get(self, request, *args, **kwargs):
        rowid = kwargs['rowid']


        for software in Software.objects.all():
            if software.rowid == rowid:
                context = {'software' : software}
                return render(request, self.template_name, context)

        return render(request, self.template_name, context)

class SoftwareEdit(View):
    
        def post(self, request, *args, **kwargs):
            rowid = kwargs['rowid']
            for software in Software.objects.all():
                if software.rowid == rowid:
                    for key, value in request.POST.items():
                        if key == 'csrfmiddlewaretoken':
                            continue
                        if key == 'rowid':
                            continue
    
                        setattr(software, key, value)
                        
    
    
                    
                    software.save()
                    return redirect('software_detail', rowid=rowid)
                
class SoftwareDelete(View):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        rowid = kwargs['rowid']
        print(rowid)
        for software in Software.objects.all():
            if software.rowid == rowid:
                print(rowid)
                software.delete()
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})


class ContractListView(View):
    template_name = "inventory/contracts.html"
    def get(self, request, *args, **kwargs):
        # read data from database and pass it to the template
        contract = Contract.objects.all().values()
        context = {
            'contract': contract,
        }
        print(context['contract'])
        


        return render(request, self.template_name, context)

    @csrf_exempt  
    def post(self, request, *args, **kwargs):
        contract = Contract()

        for key, value in request.POST.items():
            print(key, value)
            if key == 'csrfmiddlewaretoken':
                continue
            if key == 'rowid':
                continue

            setattr(contract, key, value)
        contract.save()
        return redirect('inventory_contracts')


class ContractDetailedView(View):
    template_name = "inventory/contract_detail.html"
    def get(self, request, *args, **kwargs):
        rowid = kwargs['rowid']


        for contract in Contract.objects.all():
            if contract.rowid == rowid:
                context = {'contract' : contract}
                return render(request, self.template_name, context)

        return render(request, self.template_name, context)

class ContractEdit(View):

        def post(self, request, *args, **kwargs):
            rowid = kwargs['rowid']
            for contract in Contract.objects.all():
                if contract.rowid == rowid:
                    for key, value in request.POST.items():
                        if key == 'csrfmiddlewaretoken':
                            continue
                        if key == 'rowid':
                            continue
    
                        setattr(contract, key, value)

                    contract.save()
                    
                    return redirect('contract_detail', rowid=rowid)

class ContractDelete(View):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        rowid = kwargs['rowid']
        print(rowid)
        for contract in Contract.objects.all():
            if contract.rowid == rowid:
                print(rowid)
                contract.delete()
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})

class GenerateReportView(View):
    template_name = "report/generate_report.html"
    def get(self, request, *args, **kwargs):
        # read data from database and pass it to the template

        context = {}

        


        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {
        "report_type" : request.POST.get('report_type'), 
        "report_format" : request.POST.get('report_format'),
        "report_scope" : request.POST.get('report_scope')

        }   
        context = {}

        if data['report_type'] == '1':
            hardware = serializers.serialize('json', Hardware.objects.all())
            context = {
                'hardware': hardware,
            }
        elif data['report_type'] == '2':
            software = serializers.serialize('json', Software.objects.all())
            context = {
                'software': software,
            }
        elif data['report_type'] == '3':
            contract = serializers.serialize('json', Contract.objects.all())
            context = {
                'contract': contract,
            }
        elif data['report_type'] == '4':
            hardware = serializers.serialize('json', Hardware.objects.all())
            contract = serializers.serialize('json', Contract.objects.all())
            software = serializers.serialize('json', Software.objects.all())
            context = {
                'hardware': hardware,
                'contract': contract,
                'software': software,
            }
        import os
        path = os.path.join(settings.BASE_DIR, 'reports')
        print(path)
        # # write data to file 
        fileName = data['report_type'] + "-" + dt.datetime.now().strftime("%Y-%m-%d") 
        fileP = os.path.join(path, fileName)
        if data['report_format'] == '1':
            with open(fileP + ".csv", 'w') as f:
                for key in context.keys():
                    f.write("%s,%s \n" % (key, context[key]))
        elif data['report_format'] == '2':
            with open(fileP + '.json', 'w') as f:
                for key in context.keys():
                    f.write("%s,%s \n" % (key, context[key]))
        elif data['report_format'] == '3':
            with open(fileP + '.txt', 'w') as f:
                for key in context.keys():
                    f.write("%s,%s \n" % (key, context[key]))
        elif data['report_format'] == '4':
            with open(fileP + '.pdf', 'w') as f:
                for key in context.keys():
                    f.write("%s,%s \n" % (key, context[key]))

        return redirect('inventory_reports')
        



    



class ReportListView(View):
    template_name = "inventory/reports.html"
    def get(self, request, *args, **kwargs):
        
        context = {}

        # read reports from report folder
        def get_report_list():
            import os
            path = os.path.join(settings.BASE_DIR, 'reports')
            return os.listdir(path)
        
        context = { 'report_list' : get_report_list() }

 
        return render(request  , self.template_name, context)



class ReportDetailView(View):
    template_name = "report/report_detail.html"
    def get(self, request, *args, **kwargs):
        # read data from database and pass it to the template

        context = {}

        return download(request)
        
  
class DownloadReportView(View):
    template_name = "report/download_report.html"

    def get(self, request, *args, **kwargs):
        # read data from database and pass it to the template
        file_name = kwargs['file_name']
        import os
        path = os.path.join(settings.BASE_DIR, 'reports')
        # get file name of request body
        file_name = file_name
        print(file_name)


        file_path = os.path.join(path, file_name)
        file = open(file_path, 'r')

        # create a response object and pass file blob to it
        response = HttpResponse(file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        response['X-Sendfile'] = smart_str(file_path)
        return response

        

class DeleteReportView(View):
 
    def post(self, request, *args, **kwargs):
        def delete_file( file_name):
            import os
            path = os.path.join(settings.BASE_DIR, 'reports')
            fileP = os.path.join(path, file_name)
            os.remove(fileP)

        file_name = kwargs['file_name']
        delete_file(file_name)


        return redirect('inventory_reports')