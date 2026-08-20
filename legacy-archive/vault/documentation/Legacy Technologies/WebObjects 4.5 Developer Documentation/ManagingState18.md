---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState18.html
archived_at: '2026-07-15T08:05:43.112896Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState17.md)

### Adjusting the Page Cache Size

As noted in ["WebObjects Viewed Through Its Classes"](WebObjects%20Viewed%20Through%20Its%20Classes.md#apple-he2tmmy), except for the first request, a component action request to a WebObjects application contains a session ID, page name, and context ID. The application uses this information to ask the appropriate session object for the page identified by the name and context ID. As long as the page is still in the cache, it can be retrieved and enlisted in handling the request.

By default, a WebObjects application caches the last 30 pages that a user has visited within a session. You can change the size of the cache using the application object's __setPageCacheSize__: method and retrieve the cache size with the __pageCacheSize__ method. Within each session, new pages are added to the cache until the cache size limit is reached. Thereafter, for each new page added to the cache, the cached page object representing the least recently visited page is released.
To reduce the resource requirements for an application, you could set the page cache to a smaller number. However, doing so increases the possibility that a request could address a page that is no longer in the cache. For example, if you set the page cache size to four, a user could backtrack five pages to an order form, make some changes, and resubmit the form. The result would be an error page.
To keep users from encountering this error, your application should maintain a moderate sized cache of pages. The default cache size of 30 pages is a reasonable value that protects users from reaching the backtracking limit under normal conditions; however, you can adjust the limit to any positive value you like or even zero.
Setting the page cache size to 0 has two effects. As expected, it disables page caching. Furthermore, it signals to WebObjects that you intend to provide for component state persistence rather than rely on WebObjects' inherent support. Thus, if you set the cache size to 0, no error page is generated if a request addresses a page that can't be found in the cache. Instead, WebObjects creates a new page by sending the application object a __pageWithName__: message. Since with this model pages do not persist from one request to the next, you assume responsibility for maintaining any needed component state. For this reason, it's rarely advisable to turn off page caching.
If your application uses frames and uses the default page cache size of 30, your users are more likely to see a backtracking error message. In
frames-based applications, the first few pages that the application generates (for example the navigation frame) often stay visible for long periods without being regenerated. It's possible for those pages to be bumped from the page cache.
For this reason, WebObjects actually supports two separate page caches: the page cache described above and a persistent page cache. If you want to ensure that a particular component is never bumped from the page cache, you should add it to the persistent page cache using the WOSession method __savePageInPermanentCache:__. For example, if your application always shows a navigation component in the left frame, you should add that component to the persistent page cache. This way, your users never see the backtracking error message in the application's left frame. Adjust the size of the persistent page cache with WOApplication's __setPermanentPageCacheSize:__ method.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState19.md)
