---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/DurationOfComponent.html
archived_at: '2026-07-15T07:48:00.915489Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](VisitorExample.md)

# The Duration of a Component

When users navigate to a page of an WebObjects application for the first time, a WOComponent object associated with the page is created and (in __init__) initialized. When users go to another page, the original component typically does not go away. It persists through an arbitrary number of subsequent transactions before it's deallocated. Thus when users backtrack to a page they visited earlier (as long as the transaction limit hasn't expired) things are as they left them---displayed results, entered values, and selected options.

__Note:__  An application looks first for request pages in its cache and if they're there, it restores them. Thus pages are restored when users backtrack to a page and when a request component returns itself as the response page. In typical request-handling scenarios, the response page is created. For example, the application's __pageWithName:__ method ( typically invoked in an action method ) returns a new instance of a page---even if that page has been visited before in the same session.

You set the number of pages the application caches, and thus the life span of an application's components, with WOApplication's __setPageCacheSize:__ method. If the page-cache size attribute is not explicitly set, the default is 30 pages. You can also determine the current transaction limit by sending __pageCacheSize__ to the application object.

To minimize the size of a session, you can reduce the page-cache size or you can turn off page caching altogether by setting the page-cache size to zero. If you turn off page caching, you must to re-initialize each page for each transaction it's involved in. You can perform initializations in __init__ or __awake__, since both are invoked with identical frequency.

Relying on the page cache to retain the state of a page for a user introduces certain issues and problems. One implication, of course, is scalability. If you want finer control over this aspect of an application, consider selectively storing page state in session variables, reinitializing variables in the __awake__ method, or some combination of the two.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](VariablesAndScope.md)
