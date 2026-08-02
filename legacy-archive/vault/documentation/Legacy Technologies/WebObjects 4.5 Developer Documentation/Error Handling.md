---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Deployment5.html
archived_at: '2026-07-15T08:05:22.453283Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Deployment4.md)

# Error Handling

When an error occurs, WebObjects by default returns a page containing debugging information and displays that page in the Web browser. This information is useful when you're in the debugging phase, but when you're ready to deploy, you probably want to make sure that your users don't see such information.
The WOApplication class provides the following methods that you can override to show your own error page.

|  __Method__ |  Invoked When |
|  handleSessionCreationErrorInContext: |  The application needs to create a new session but can't. |
|  handleSessionRestorationErrorInContext: |  The application receives a request from a session that has timed out. |
|  handlePageRestorationErrorInContext: |  The application tries to access an existing page but cannot. Usually, this occurs when the user has backtracked beyond the limit set by __setPageCacheSize:__ and __setPageRefreshOnBacktrackEnabled:__ is NO. |
|  handleException:inContext: (__handleException__ in Java) |  The application receives an exception; that is, any general type of error has occurred. |

```
```


For example, the following implementation of __handleException:inContext:__ returns a component named ErrorPage whenever an error occurs in the application.

```
public WOResponse handleException(java.lang.Throwable
anException, WOContext aContext) {
    WOResponse response = aContext.component().
        pageWithName("ErrorPage").generateResponse();

    return response;
}
```


Notice that this method, and all of the error-handling methods, return a WOResponse object instead of a WOComponent object.

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](Automatically%20Terminating%20an%20Application.md)
