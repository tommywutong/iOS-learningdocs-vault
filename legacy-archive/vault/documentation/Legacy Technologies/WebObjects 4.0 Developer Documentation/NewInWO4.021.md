---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.021.html
archived_at: '2026-07-15T07:58:32.207226Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.020.md)

## How Direct Action Requests Are Received

Clicking the WOHyperlink from the previous section generates a URL that looks something like this:

```
http://localhost/cgi-bin/WebObjects/AppName.woa/wa/
display?sku=value&aKey=aValue...
```


The __wa__ after the application name is a request handler key. It specifies which WORequestHandler should handle the request. WORequestHandler is a new class in WebObjects 4.0. You can read more about it under [WORequestHandler Class](NewInWO4.027.md#apple-gmztmmbu). The __wa__ string is the key for the WODirectActionRequestHandler, a private subclass of WORequestHandler.

In WebObjects 4.0, when the WOApplication receives a request from the WOAdaptor, it looks at the request handler key to determine which WORequestHandler should handle the request. It then sends that WORequestHandler a __handleRequest:__ message.
If the URL doesn't have a request handler key (as is the case with the initial URL used to begin a session with a WebObjects application), WOApplication uses whatever its default request handler is set to be. By default, the default request handler is WOComponentRequestHandler, which performs the request handling scheme that you're used to. If you want to write an application entirely using direct actions, set the default request handler in your WOApplication's __init__ method or constructor in this way:

```
// Java implementation
public WOApplication() {
    super();
    ...
    setDefaultRequestHandler(requestHandlerForKey(
        WOApplication.directActionRequestHandlerKey()));
    ...
}
//WebScript implementation
- init {
    self = [super init];
    ...
    [self setDefaultRequestHandler:[self requestHandlerForKey:
        [WOApplication directActionRequestHandlerKey]]];
    ...
    return self;
}
```


If WODirectActionRequestHandler is the default request handler, the first request triggers the __defaultAction__ method, which is declared for you in your DirectAction class.
In its implementation of __handleRequest:__, WODirectActionRequestHandler extracts the direct action class and the action from the URL. (If your WODirectAction subclass isn't named DirectAction, the class name appears in the URL immediately before the action.) WODirectActionRequestHandler then sends the message __performActionNamed:__ to your WODirectAction object.
Each action method in your WODirectAction class should end with the string "Action" and should return either a WOComponent or a WOResponse object. For example:

```objc
- (WOComponent *)displayAction
```


There's a new protocol and interface named WOActionResults conformed to by WOResponse and WOComponent. Your action may actually return any object that conforms to WOActionResults.
When the action method returns, WODirectActionRequestHandler sends the message __generateResponse__ to the object returned by the action method. This is the method defined in the WOActionResults protocol. __generateResponse__ returns a WOResponse object. WOResponse's implementation is simply to return itself. WOComponent's implementation translates the component into a WOResponse by sending itself __appendToResponse:inContext:__.
__Note:__  WOComponent's __generateResponse__ method is also useful for the __handleException...__ methods defined in WOApplication.
Upon receiving the WOResponse, WODirectActionRequestHandler returns the response to the WOApplication, and the WOApplication passes it to the WOAdaptor.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.022.md)
