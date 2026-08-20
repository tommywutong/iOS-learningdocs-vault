---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.047.html
archived_at: '2026-07-15T07:58:50.941021Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.046.md)

## WOLongResponsePage Class

WOLongResponsePage, defined in the WOExtensions Framework, is an abstract subclass of WOComponent. You use WOLongResponsePage when a requested action will take a long time to complete, say more than 5 seconds.
To use WOLongResponsePage, your long-running action should instantiate (with __pageWithName:__) and return a component that is a subclass of WOLongResponsePage. The subclass of WOLongResponsePage should override the method __performAction__, which is where the actual computation takes place. WOLongResponsePage performs the computation in a separate thread and returns a status page that indicates that the request is being processed.
__Note:__  If you access WebObjects framework objects within __performAction__, you must check out the session (using the WOSessionStore's __checkOutSessionWithSessionID:request:__ method) just before the WebObjects call and check it back in (with the __checkInSessionForContext:__ method) just after the call.
WOLongResponsePage defines the following methods:

|  WOLongResponsePage |  |
|  Method |  Description |
|  performAction |  Override this method to perform the requested long computation. Returns the result of that computation as an object. |
|  pageForResult: |  Returns the result page that is displayed when __performAction__ completes. |
|  setStatus: |  Sets the status of the computation. The long computation should send this message periodically so that the refresh page reflects the status of the computation. |
|  refreshPageForStatus: |  Returns the page that is displayed while the computation is running. This page displays the current status of the computation. |
|  refreshInterval |  The interval after which the refresh page is refreshed. |
|  setRefreshInterval: |  Sets the refresh interval. |
|  refresh |  Called by the WOMetaRefresh __invokeAction__ callback (can also be called manually if the page is not self refreshing). This method calls either __pageForException__:, __pageForResult__:, __refreshPageForStatus__: or __cancelPageForStatus__: depending of the state of the long response. |
|  isCancelled |  Returns YES or true if the request has been cancelled. The long running computation should check this value to see if it should abort. |
|  cancel |  Cancels the request. You should bind a cancel button on the refresh page to this method. |
|  cancelPageForStatus: |  Returns the cancel page, displayed when the request is cancelled. |
|  pageForException: |  Returns the exception page, displayed when an exception occurs in __performAction__. |
|  lock |  Locks the page. |
|  unlock |  Unlocks the page. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Dynamic%20Elements%20Changes.md)
