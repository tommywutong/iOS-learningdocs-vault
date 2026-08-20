---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.013.html
archived_at: '2026-07-15T07:58:27.217127Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.012.md)

## Changes to WebObjects Application URL

The typical WebObjects application URL now has the following format:

```
http://host[:port]/cgi-bin/WebObjects/App[[.woa][/instance]/key/...
```


where the variables are defined as follows:

|  Variable |  Description |
|  host |  The host name of your computer or localhost. |
|  port |  The port number. This is included if you want to direct connect. |
|  cgi-bin |  The cgi-bin directory of your server, usually cgi-bin or Scripts. |
|  WebObjects |  The name of the CGI adaptor, usually WebObjects or WebObjects.exe. |
|  App |  The application name.  This field is no longer the path to the application relative to DocRoot__/WebObjects__. It is simply the application name. The __WOApplicationBaseURL__ option provides the path. |
|  instance |  The application instance number. |
|  key |  The request handler key. This key specifies which WORequestHandler object should be used to process the request. The WORequestHandler class is new in WebObjects 4.0 and is described in the section [WORequestHandler Class](NewInWO4.027.md#apple-gmztmmbu). |
|  ... |  Information specific to the request handler. Each WORequestHandler uses a different format for the rest of the URL.  The two main request handlers are WOComponentRequestHandler and WODirectActionRequestHandler. WOComponentRequestHandler handles requests in exactly the same manner in which they were handled in earlier releases. Its format for the rest of the URL is:  _componentName_/_sessionID_/_elementID_  WODirectActionRequestHandler handles direct actions, a new feature in WebObjects 4.0. (You can read more about this feature in [Direct Actions](Direct%20Actions.md#apple-gm3tqmbu).) Its URLs have this format:  [_actionClass_ | _actionName_ | _actionClass_/_actionName_][?_key_=_value_&_key_=_value_.....] |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Support%20for%20Multithreaded%20Applications.md)
