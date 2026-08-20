---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.028.html
archived_at: '2026-07-15T07:58:38.708518Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.027.md)

## WOApplication Methods

The following methods have been added to WOApplication to support the use of WORequestHandler objects:

|  WOApplication |  |
|  Method |  Description |
|  registerRequestHandler:forKey: (Objective-C)  registerRequestHandler (Java) |  Adds a new WORequestHandler to the list of request handlers. The key is a string that will be used in the URL to indicate which request handler should process the request. The key can be any string of letters and numbers, but it must include at least one letter. |
|  removeRequestHandlerForKey: |  Removes a WORequestHandler from the list of request handlers. |
|  defaultRequestHandler |  Returns the request handler that is used when the request URL doesn't contain a request handler key. This typically happens only on the first request. |
|  setDefaultRequestHandler: |  Sets the request handler that should be used when the request URL doesn't contain a request handler key. If you don't use this method, the default request handler is WOComponentRequestHandler, which handles requests routed through a component. |
|  handlerForRequest: |  Returns the WORequestHandler that can handle the current request, determined by the request handler key in the URL. That handler is returned and is subsequently sent the message __handleRequest__:, where all request-specific processing is done. |
|  registeredRequestHandlerKeys |  Returns an array of request handler keys that have been registered with the application. |
|  setComponentRequestHandlerKey: (class or static method) |  Sets the key used to indicate the WOComponentRequestHandler, which handles the traditional WebObjects URL containing a component name, session ID, and context ID. The default is "wo". |
|  setDirectActionRequestHandlerKey: (class or static method) |  Sets the key used to indicate the WODirectActionRequestHandler, which handles the WODirectAction-style URLs containing an action name. The default is "wa". |
|  setResourceRequestHandlerKey: (class or static method) |  Sets the key used to indicate the WOResourceRequestHandler, which handles resource requests, such as requests for images. The default is "wr". |
|  dispatchRequest: |  Determines which request handler should handle the request and then sends that request handler a __handleRequest:__ message. This method determines which WORequestHandler should handle the request by looking up the request handler key in the URL. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.029.md)
