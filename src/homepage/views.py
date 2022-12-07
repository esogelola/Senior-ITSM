from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import redirect
from django.conf import settings
from inventory.models import Hardware, Contract, Software
import datetime as dt

# Create your views here.
class HomeView(View):
    template_name = "home.html"
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "about.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"

 
    def get(self, request, *args, **kwargs):
        context = {}
        # aggregate data from hardware, contract, software and make some metrics to display on the dashboard
        totalHardware = Hardware.objects.all().count()
        totalContract = Contract.objects.all().count()
        totalSoftware = Software.objects.all().count()
        totalOverall = totalHardware + totalContract + totalSoftware 
        totalContractCount =  0
        totalExpiredContractCount = 0

        # get the total number of contracts that have not expired
        for contract in Contract.objects.all():
            if contract.expiry > dt.date.today():
                totalContractCount += 1

        # get the total number of contracts that have expired
        for contract in Contract.objects.all():
            if contract.expiry < dt.date.today():
                totalExpiredContractCount += 1


        hardwarePercentage = round((totalHardware / totalOverall) * 100)
        contractPercentage = round((totalContract / totalOverall) * 100)
        softwarePercentage = round((totalSoftware / totalOverall) * 100)

        # calculate total softwaree cost
        def sumSoftwareCost():
            total = 0
            for software in Software.objects.all():
                total += software.price
            return total

        totalSoftwareCost = sumSoftwareCost()

        # count contracts that are about to expire
        def countExpiringContracts():
            total = 0
            for contract in Contract.objects.all():

                # get the difference between the expiry date and today's date
                diff = contract.expiry - dt.date.today()
                # if the difference is less than 30 days, then add to the total
                if diff.days < 30 and diff > dt.timedelta(0):
                    total += 1
    
            return total

        totalExpiringContracts = countExpiringContracts()
        # check reports folder and count the number of reports

        def get_report_count():
            import os
            path = os.path.join(settings.BASE_DIR, 'reports')
            return len(os.listdir(path))

        context['reports'] = get_report_count()


        context['totalOverall'] = totalOverall
        context['totalSoftwareCost'] = totalSoftwareCost
        context['hardwarePercentage'] = hardwarePercentage
        context['contractPercentage'] = contractPercentage
        context['softwarePercentage'] = softwarePercentage
        context['totalExpiringContracts'] = totalExpiringContracts
        context['totalContractCount'] = totalContractCount
        context['totalExpiredContractCount'] = totalExpiredContractCount


        return render(request, self.template_name, context)

        
        
    


