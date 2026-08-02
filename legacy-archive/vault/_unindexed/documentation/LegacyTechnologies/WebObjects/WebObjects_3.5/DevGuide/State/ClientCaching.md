---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/ClientCaching.html
archived_at: '2026-07-15T07:52:11.298715Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](PageWithName.md)

## Client-Side Page Caching

When accessing a web page, the user's browser associates the URL with the HTML page it downloads from the server and stores this information on the user's machine. If the browser is asked to display the URL again at a later date, it fetches the cached page rather than emitting another request. In many cases, this short-circuit is desirable because it reduces network traffic and increases a web site's perceived responsiveness.
Sometimes, however, you need to make sure the user is seeing the most up-to-date information. You must therefore disable client-side caching. WOApplication provides the setPageRefreshOnBacktrackEnabled: method for this purpose. In general, you send this message in the application object's initialization method:

```
    // WebScript example
    - init {
        [super init];
        [self setPageRefreshOnBacktrackEnabled:YES];
        return self;
    }
```


The setPageRefreshOnBacktrackEnabled: method adds a header to the HTTP response. This header sets the expiration date for an HTML page to the date and time of the creation of the page. Later, when the browser checks its cache for this page, it finds that the page is no longer valid and so refetches it by resubmitting the request URL to the WebObjects application.
A WebObjects application handles a page-refresh request differently than it would a standard request. When the application determines that the request URL is identical to one it has previously received (that is, the session and context IDs in the request URL are identical to those in a request it has previously received), it simply returns the response page that was associated with this earlier request. The first two steps of a normal request handling loop (value extraction from the request and action invocation) don't occur.

[!Table of Contents](StateTOC.md) [!Next Section](WODisplayGroupAndRefresh.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
