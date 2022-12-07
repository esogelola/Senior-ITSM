from django.urls import path

from . import views

urlpatterns = [
    path('', views.HardwareListView.as_view(), name='inventory_index'),
    path('hardwares', views.HardwareListView.as_view(), name='inventory_hardwares'),
    path('hardwares/<int:rowid>', views.HardwareDetailedView.as_view(), name='hardware_detail'),
    path('hardwares/edit/<int:rowid>', views.HardwareEdit.as_view(), name='hardware_edit'),
    path('hardwares/delete/<int:rowid>', views.HardwareDelete.as_view(), name='hardware_delete'),

    path('softwares', views.SoftwareListView.as_view(), name='inventory_softwares'),
    path('softwares/<int:rowid>', views.SoftwareDetailedView.as_view(), name='software_detail'),
    path('softwares/edit/<int:rowid>', views.SoftwareEdit.as_view(), name='software_edit'),
    path('softwares/delete/<int:rowid>', views.SoftwareDelete.as_view(), name='software_delete'),

    path('contracts', views.ContractListView.as_view(), name='inventory_contracts'),
    path('contracts/<int:rowid>', views.ContractDetailedView.as_view(), name='contract_detail'),
    path('contracts/edit/<int:rowid>', views.ContractEdit.as_view(), name='contract_edit'),
    path('contracts/delete/<int:rowid>', views.ContractDelete.as_view(), name='contract_delete'),

    path('reports', views.ReportListView.as_view(), name='inventory_reports'),
    path('report/download/<str:file_name>', views.DownloadReportView.as_view(), name='report_download'),
    path('report/generate', views.GenerateReportView.as_view(), name='generate_report'),
    path('report/delete/<str:file_name>', views.DeleteReportView.as_view(), name='report_delete'),
   
]