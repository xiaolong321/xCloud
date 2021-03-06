from django.conf.urls import patterns, url
urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'cloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^image/$', 'feature.image.views.image'),
    url(r'^overview/$', 'feature.overview.views.overview'),
    url(r'^volume/$', 'feature.volume.views.volume'),
    url(r'^metering/$', 'feature.metering.views.metering'),
    url(r'^mail/$','feature.mail.views.mail'),
    #url(r'^volume/create/$', 'feature.volume.views.volume_create'),
    url(r'^volume/create/acc/$', 'feature.volume.views.volume_create_acc'),
    url(r'^instance/$', 'feature.instance.views.instance'),
    url(r'^instance/createForm$', 'feature.instance.views.createForm'),
    url(r'^instance/createInstance$', 'feature.instance.views.instanceCreate'),
    url(r'^instance/attachVolume$', 'feature.instance.views.attachVolume'),                   
    url(r'^instance/renameInstance', 'feature.instance.views.renameInstance'),
    url(r'^instance/rebootInstance/p1(.*)p2(.*)/$', 'feature.instance.views.rebootInstance'),
    url(r'^instance/stopInstance/p1(.*)p2(.*)/$', 'feature.instance.views.stopInstance'),
    url(r'^instance/startInstance/p1(.*)p2(.*)/$', 'feature.instance.views.startInstance'),
    url(r'^instance/deleteInstance/p1(.*)p2(.*)/$', 'feature.instance.views.deleteInstance'),
    url(r'^instance/startConsole/p1(.*)p2(.*)/$', 'feature.instance.views.startConsole'),
    url(r'^instance/ajax_process/p1(.*)p2(.*)/$', 'feature.instance.views.ajax_process'),
    url(r'^instance/instanceDetail/p1(.*)p2(.*)/$', 'feature.instance.views.show_instance_detail'),
    url(r'^volume/load/$', 'feature.volume.views.load'),
    url(r'^volume/unload/p1(.*)p2(.*)/$', 'feature.volume.views.unload'),
    url(r'^volume/delete/p1(.*)p2(.*)/$', 'feature.volume.views.delete'),
    url(r'^volume/ajax_process/p1(.*)p2(.*)/$', 'feature.volume.views.ajax_process'),
    url(r'^volume/extend/$', 'feature.volume.views.extend'),
    url(r'^metering/detailOfInstance/p1(.*)p2(.*)/$', 'feature.metering.views.instance_metering_detail'),
    url(r'^metering/detailOfVolume/p1(.*)p2(.*)/$', 'feature.metering.views.volume_metering_detail'),
    url(r'^metering/listDetail/$', 'feature.serverlist.views.listDetail'),
)
