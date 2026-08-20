---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects3.html
archived_at: '2026-07-18T01:23:47.270288Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects2.md)

## Adaptor Modes

All WebObjects adaptors route incoming requests to WebObjects applications in one of two modes:

- Load-balancing between concurrent instances of the same application specified in the public configuration file (deployment)
- Choosing an application from the private configuration file (development)

The active adaptor tries to contact the requested application by going through the modes in the preceding order.
__Load Balancing__: When the client request tries to contact an application, the active WebObjects adaptor first checks the public configuration file for an application matching the specification in the URL. Load balancing typically occurs only for the first request of a session if the application stores state in the server. Afterwards, the application resolves the URL so that page navigation will always occur in the context of the same application. But if the application stores state on the page or in cookies, true load balancing will be performed for _each_ request.
__Private Configuration File__: If the adaptor cannot find a public configuration file, it attempts to resolve the URL against entries in the private configuration file. If the adaptor finds a matching entry but cannot contact it or if the adaptor cannot find a matching entry, it returns a page listing the contents of the configuration file. For example, if an application has been stopped, the adaptor might still list its entry in the private configuration file.
Note that if the public configuration file _NEXT_ROOT___/Library/WebObjects/Configuration/WebObjects.conf__ exists, no applications listed in the private configuration file are ever contacted. Also note that adding applications to the Monitor as described in the section "[Adding and Configuring an Application](ServingWebObjects12.md#apple-gyytqna)" creates the public configuration file. Thus, if you are using the Monitor application, autostarting is disabled.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects4.md)
