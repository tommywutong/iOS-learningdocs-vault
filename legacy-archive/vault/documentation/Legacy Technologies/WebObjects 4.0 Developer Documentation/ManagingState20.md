---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ManagingState20.html
archived_at: '2026-07-18T01:20:14.623351Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState19.md)

## Client-Side Page Caching

When accessing a web page, the user's browser associates the URL with the HTML page it downloads from the server and stores this information on the user's machine. If the browser is asked to display the URL again at a later date, it fetches the cached page rather than emitting another request. In many cases, this short-circuit is desirable because it reduces network traffic and increases a web site's perceived responsiveness.
Sometimes, however, you need to make sure the user is seeing the most up-to-date information. You must therefore disable client-side caching. WOApplication provides the __setPageRefreshOnBacktrackEnabled__: method for this purpose. In general, you send this message in the application object's initialization method:

```
// WebScript example
- init {
    [super init];
    [self setPageRefreshOnBacktrackEnabled:YES];
    return self;
}
```


The __setPageRefreshOnBacktrackEnabled__: method adds a header to the HTTP response. This header sets the expiration date for an HTML page to the date and time of the creation of the page. Later, when the browser checks its cache for this page, it finds that the page is no longer valid and so refetches it by resubmitting the request URL to the WebObjects application.
If you only need to disable client caching for certain responses within your application, you can use WOResponse's __disableClientCaching__ method to disable caching on a response-by-response basis.
A WebObjects application handles a page-refresh request differently than it would a standard request. When the application determines that the request URL is identical to one it has previously received (that is, the session and context IDs in the request URL are identical to those in a request it has previously received), it simply returns the response page that was associated with this earlier request. The first two steps of a normal component action request handling loop (value extraction from the request and action invocation) don't occur.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState21.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
