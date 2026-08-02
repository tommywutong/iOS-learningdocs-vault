---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ManagingState8.html
archived_at: '2026-07-18T01:20:16.229843Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState7.md)

### State in the Server

Storing state in memory on the application server is the default behavior, so no setup is necessary. However, if you want access to the session store object, you can include the following code in the application object's initialization method:

```
// WebScript example
id sessionStore = [WOSessionStore serverSessionStore];
[self setSessionStore:sessionStore];
// Java example
WOSessionStore sessionStore =
WOSessionStore.serverSessionStore();
this.setSessionStore(sessionStore);
```


When state is stored in the server, the application keeps a cache of session objects in the session store, and each session keeps a cache of component objects. Because these objects can take up a lot of memory, WebObjects gives you ways to control the amount of memory this state storage mechanism consumes:

- Setting session time-outs (see "[Controlling Session State](Controlling%20Session%20State.md#apple-gm2dona)")
- Setting the size of the page cache (see "[Adjusting the Page Cache Size](ManagingState18.md#apple-heyde)")

A significant consequence of storing state in memory is the effect on
load-balanced applications. When an application is load balanced, there are several instances of that application running on different physical machines to reduce the load on a particular server. (The online book [_Serving WebObject_](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)s describes how to set this up.) WebObjects can route any request to any application instance running on any machine as long as that instance doesn't store state in memory in the server (that is, as long as the application is stateless or uses one of the other state-storage mechanisms described in this chapter). When state is stored in the server, however, it is stored in the application instance. Because state is stored in the application instance, all requests made by one session must return to that instance.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
