---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/initOrAwake.html
archived_at: '2026-07-15T07:47:31.859660Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](sleepAnddealloc.md)

# When Use init, When Use awake?

Since both __init__ and __awake__ are entry points for an object's involvement in request handling, they are both suitable places for initializations. So which method is a better place for this? When is it better to use __init__, and when is it better to use __awake__?

The short answer is that, because objects are typically persistent to some degree, __init__ is the better place to initialize an object. A WebObjects application, by default, stores page instances. Those component objects usually persist through a number of transactions (as specified in __setPageCacheSize:__) and are restored when the user backtracks to them. Pages that return __nil__ in an action method also restore a cached instance of themselves.

Page caching, however, can impose a penalty in terms of scalability for some applications. If scalability is a problem, you can optimize an application by initializing component instance variables in __awake__. Then, in __sleep__, you can deallocate these variables by setting them to __nil__.

Even when optimizing, however, an important consideration is the cost of initializing operations as offset against the cost of storing page instances. For example, it is sensible to perform static initializations in __awake__, but it is prohibitive to do database fetches in __awake__. Database and file system operations are expensive and so should not be repeated needlessly.

You might want finer control over page persistence than that afforded by the page-caching mechanism; for instance, you may want the action method invoked by a Submit button to return the most recent instance of a page instead of new page. To achieve this finer control, you can always cache selected pages and component variables in the session object and restore them when these pages and variables are requested.
See the chapter [Managing State](../State/ManagingState.book.md) for a discussion of storage strategies and techniques.

In the final analysis, what you do in __init__ and what you do in __awake__ are a matter of common sense, given the object involved and the frequency of invocation. For example, if you want to tally the number of transactions a page is involved in, the component's __awake__ method is the logical place to increment a counter. On the other hand, you need to set the session time-out period only once, at the beginning of a session, so the obvious place to do that is in the __init__ method of the session object.

[!Table of Contents](RunLoop.book.md)
[!Next Section](ApplicationInit.md)
