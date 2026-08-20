---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/StateInServer.html
archived_at: '2026-07-15T07:47:53.896489Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](CloserLookAtStrats.md)

# State in the Server

Storing state in memory on the application server is WebObjects default behavior. As you can see from the SessionStores example, the server session store object is accessible from the WOSessionStore class:

```
id sessionStore = [WOSessionStore serverSessionStore];
```

```
[[self application] setSessionStore:sessionStore];
```

In later sections, we'll look at the principal ways of controlling the amount of memory that this state storage mechanism consumes:

- Setting session timeouts (see "[Managing Session Resources](ManagingSessionResources.md)")
- Setting the size of the page cache (see "[Adjusting the Page Cache Size](PageCacheSize.md)")
- Page uniquing by implement __pageWithName:__ in the session object (see "[pageWithName: and Page Caching](PageWithName.md)")

One consequence of storing state in memory should be emphasized: Once state for a session is established in a particular application instance, all subsequent requests in that session must return to that instance. WebObjects handles this automatically by including the application instance number in the URL, as illustrated in
Figure 2: "[Parts of a WebObjects URL](AccessingExistingSession.md#apple-kjcumobtgm2de)".

However, at a popular web site it may be desirable to have multiple application instances (perhaps running on different physical machines) service incoming requests. As long as the application is stateless---or the state is stored outside the application (as with any of the other techniques described here)---the WebObjects adaptor can route requests to any available application. However, if session state is stored in memory, a request must return to the application that stores that state. (See _Serving WebObjects_ for more information about running multiple application instances.)

[!Table of Contents](ManagingState.book.md)
[!Next Section](StateInPage.md)
