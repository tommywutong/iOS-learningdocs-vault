---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses9.html
archived_at: '2026-07-15T08:06:24.709616Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses8.md)

## Determining the Request Type

The first step in the request-response cycle is to determine which request handler should handle the request. A cycle of the request-response loop begins when the WOAdaptor receives an incoming HTTP request. The adaptor object packages this request in a WORequest object and forwards this object to the application object in a __dispatchRequest:__ message. The application object determines which WORequestHandler should handle the request with __handlerForRequest:__. (The request handler key in the request URL specifies which WORequestHandler should be used.)
If the request is the first one for a given user session, the request URL looks like the URL shown in [Figure 20](#apple-g43dcnq).

!

Figure 20. URL to Access a WebObjects Application

This URL does not have a request handler key. In this case, WOApplication uses the default request handler (returned by its __defaultRequestHandler__ method). Unless you override the default using __setDefaultRequestHandler:__, the default request handler is WOComponentRequestHandler.
After the initial request, subsequent URLs look like the one shown in [Figure 21](#apple-g43dena).

!

Figure 21. WebObjects URL in Existing Session

This URL contains a request handler key immediately following the application name. WOApplication maintains a dictionary of WORequestHandlers. It uses the request handler key to look up which request handler to use. By default, "wo" is the request handler key specifying component actions, and "wa" specifies direct actions (which are handled by the WODirectActionRequestHandler object).
Once the application has determined which request handler to use, it sends that handler a __handleRequest:__ message. From this point forward, what happens during the request-response loop is highly dependent on which type of request is being processed: a component action request, or a direct action request. The rest of this section looks at each type of request handler in detail.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses10.md)
