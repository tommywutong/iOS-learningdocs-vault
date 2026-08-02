---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/StateInServer.html
archived_at: '2026-07-15T07:52:22.315265Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](CloserLookAtStrats.md)

### State in the Server

Storing state in memory on the application server is the default behavior, so no setup is necessary. However, if you want access to the session store object, you can include the following code in the application object's initialization method:

```
    // WebScript example
    id sessionStore = [WOSessionStore serverSessionStore];
    [self setSessionStore:sessionStore];

    // Java example
    SessionStore sessionStore = SessionStore.serverSessionStore();
    this.setSessionStore(sessionStore);
```


When state is stored in the server, the application keeps a cache of session objects in the session store, and each session keeps a cache of component objects. Because these objects can take up a lot of memory, WebObjects gives you ways to control the amount of memory this state storage mechanism consumes:

- Setting session time-outs (see ["Controlling Session State"](ControllingSessionState.md#apple-gm2dona))
- Setting the size of the page cache (see ["Adjusting the Page Cache Size"](PageCacheSize.md#apple-heyde))
- Page uniquing by implementing pageWithName: in the session object (see ["pageWithName: and Page Caching"](PageWithName.md#apple-ha2tk))

A significant consequence of storing state in memory is the effect on load-balanced applications. When an application is load balanced, there are several instances of that application running on different physical machines to reduce the load on a particular server. (The online book [_Serving WebObjects_](../../ServingWebObjects/ServingWebObjectsTOC.md) describes how to set this up.) WebObjects can route any request to any application instance running on any machine as long as that instance doesn't store state in memory in the server (that is, as long as the application is stateless or uses one of the other state-storage mechanisms described in this chapter). When state is stored in the server, however, it is stored in the application instance. Because state is stored in the application instance, all requests made by one session must return to that instance.

[!Table of Contents](StateTOC.md) [!Next Section](StateInPage.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
