---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/AdaptorModes.html
archived_at: '2026-07-15T07:55:51.447016Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](ConfigFiles.md)

## Adaptor Modes

All WebObjects adaptors route incoming requests to WebObjects applications in one of three modes:

- Load-balancing between concurrent instances of the same application specified in the public configuration file
- Choosing an application from the private configuration file
- Autostarting an application

The active adaptor tries to contact the requested application by going through the modes in the preceding order.
__Load Balancing__: When the client request tries to contact an application, the active WebObjects adaptor first checks the public configuration file for an application matching the specification in the URL. Load balancing typically occurs only for the first request of a session if the application stores state in the server. Afterwards, the application resolves the URL so that page navigation will always occur in the context of the same application. But if the application stores state on the page or in cookies, true load balancing will be performed for _each_ request.
__Private Configuration File__: If the adaptor cannot find a public configuration file, it attempts to resolve the URL against entries in the private configuration file. If the adaptor finds a matching entry but cannot contact it (for example, the application has been stopped), the adaptor deletes the "dangling" entry from the private configuration file and autostarts the application.
__Autostarting__: If there is no public configuration file and the adaptor fails to find an application matching the client's request in the private configuration file, it tries to start the application itself. The adaptor first searches in specific locations in the document root of the HTTP server and then in _NeXT_ROOT___/NextLibrary/WOApps__ for a WebObjects application (one with a __.woa__ extension) that matches the specification in the request URL. If it finds one, it invokes the __WODefaultApp__ executable, or if the application is compiled, it invokes the executable in the application wrapper itself. This invocation starts the application on the HTTP server machine and registers it in the private configuration file, thereby allowing the adaptor to contact the new application instance. If the adaptor cannot find the requested application (for example, there's a typo in the URL), it returns a list of the applications it can find.
Note that if the public configuration file _NeXT_ROOT___/NextLibrary/WOAdaptors/Configuration/WebObjects.conf__ exists, no applications are ever autostarted. Also note that adding applications to the Monitor as described in the section "[Initial Monitor Setup](InitialSetup.md#apple-gq3temi)" creates the public configuration file. Thus, if you are using the Monitor application, autostarting is disabled.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](InstalledAdaptors.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
