---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/AdaptorModes.html
archived_at: '2026-07-15T07:49:51.735511Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](ConfigFiles.md)

# Adaptor Modes

All HTTP adaptors route incoming requests to WebObjects applications in one of three modes:

1. Load-balancing between concurrent instances of the same application specified in the public configuration file
2. Choosing an application from the private configuration file
3. Autostarting an application

The active adaptor tries to contact the requested application by going through the modes in the preceding order.

__Load Balancing__: When the client request tries to contact an application, the active HTTP adaptor first checks the public configuration file for an application matching the specification in the URL. Load balancing typically occurs only for the first request of a session if the application stores state in the server. Afterwards, the application resolves the URL so that page navigation will always occur in the context of the same application. But if the application stores state on the page or in cookies, true load balancing will be performed for _each_ request.

__Private Configuration File__: If the HTTP adaptor cannot find a public configuration file or fails to find any entry in the public configuration file matching the URL, it attempts to resolve the URL against entries in the private configuration file. If the adaptor finds a matching entry but cannot contact it (for example, the application has been stopped), the adaptor deletes the "dangling" entry from the private configuration file and autostarts the application.

__Autostarting__: If there is no public configuration file, and the adaptor fails to find an application matching the client's request in either the public configuration file or the private configuration file, it tries to start the application itself. The adaptor first searches in specific locations in the document root of the HTTP server or in _NEXT_ROOT___/NextLibrary/WOApps__ for a WebObjects application (one with a ".woa" extension) that matches the specification in the request URL. If it finds one, it invokes the WODefaultApp executable or, if the application is compiled, it invokes the executable in the application wrapper itself. This invocation starts the application on the HTTP server machine and causes the adaptor to register the application in the private configuration file, thereby allowing the adaptor to contact the new application instance. If the adaptor cannot find the requested application, it returns an error and stops. Autostarted applications always use the default adaptor (WODefaultAdaptor).

__Note__: Previous versions of WebObjects had an adaptor mode that allowed submissions of URLs having this format:

> http://_host_/cgi-bin/WebObjects/_ApplicationName_:_InstanceNumber_@_hostName_

This mode is no longer available to users.

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](InstalledAdaptors.md)
