---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/PageCacheSize.html
archived_at: '2026-07-15T07:52:17.297534Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](ManagingComponentResources.md)

### Adjusting the Page Cache Size

As noted in ["WebObjects Viewed Through Its Classes"](../HowWOWorks/HowWOWorks.md), except for the first request, a request to a WebObjects application contains a session ID, page name, and context ID. The application uses this information to ask the appropriate session object for the page identified by the name and context ID. As long as the page is still in the cache, it can be retrieved and enlisted in handling the request.

By default, a WebObjects application caches the last 30 pages that a user has visited within a session. You can change the size of the cache using the application object's setPageCacheSize: method and retrieve the cache size with the pageCacheSize method. Within each session, new pages are added to the cache until the cache size limit is reached. Thereafter, for each new page added to the cache, the cached page object representing the least recently visited page is released.
To reduce the resource requirements for an application, you could set the page cache to a smaller number. However, doing so increases the possibility that a request could address a page that is no longer in the cache. For example, if you set the page cache size to four, a user could backtrack five pages to an order form, make some changes, and resubmit the form. The result would be an error page like this:!Figure 36. Backtracking Error Message
To keep users from encountering this error, your application should maintain a moderate sized cache of pages. (Another strategy is to limit the number of identical page instances that your application creates; see ["pageWithName: and Page Caching"](PageWithName.md#apple-ha2tk) for one way to do this.) The default cache size of 30 pages is a reasonable value that protects users from reaching the backtracking limit under normal conditions; however, you can adjust the limit to any positive value you like or even zero.

Setting the page cache size to 0 has two effects. As expected, it disables page caching. Furthermore, it signals to WebObjects that you intend to provide for component state persistence rather than rely on WebObjects' inherent support. Thus, if you set the cache size to 0, no error page is generated if a request addresses a page that can't be found in the cache. Instead, WebObjects creates a new page by sending the application object a pageWithName: message. Since with this model pages do not persist from one request to the next, you assume responsibility for maintaining any needed component state. For this reason, it's rarely advisable to turn off page caching.

[!Table of Contents](StateTOC.md) [!Next Section](PageAwake.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
