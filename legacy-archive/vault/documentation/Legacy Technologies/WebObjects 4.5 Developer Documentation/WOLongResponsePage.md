---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WOLongResponsePage.html
archived_at: '2026-07-15T08:11:46.949434Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)

# WOLongResponsePage

> __Inherits
> from:__  [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) [WOElement](WOElement.md#apple-k5huk3dfnvsw45a) NSObject

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

WOLongReponsePage is an abstract subclass of WOComponent that
spawns a separate thread in which to perform the action and returns
a status page indicating that the request is being processed. Use
WOLongReponsePage when a requested action will take a long time
to complete (more than 5 seconds, say).

To use WOLongResponsePage, your long-running action should
use WOComponent's [pageWithName](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobqwozkxnf2gqttbnvsq) method to instantiate and
return a component that is a subclass of WOLongResponsePage. This subclass
should override the [performAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxazlsmzxxe3kbmn2gs33o) method
and perform the actual computation.

|  |
| --- |
| If you access WebObjects framework objects from within your implementation of [performAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxazlsmzxxe3kbmn2gs33o), you must check out the session (using WOSessionStore's [checkOutSessionWithID](WOSessionStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss6y3imvrwwt3vorjwk43tnfxw4v3joruesra) method) just before invoking the WebObjects framework method, and check it back in (using WOSessionStore's [checkInSessionForContext](WOSessionStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss6y3imvrwwsloknsxg43jn5xem33sinxw45dfpb2a) method) just after. |

## Method Types

---

> **Performing the computation**
> : [performAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxazlsmzxxe3kbmn2gs33o)
>
> **Returning pages**
> : [cancelPageForStatus](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxwgylomnswyudbm5sum33skn2gc5dvom)
> : [pageForException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxaylhmvdg64sfpbrwk4dunfxw4)
> : [pageForResult](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxaylhmvdg64ssmvzxk3du)
> : [refreshPageForStatus](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxezlgojsxg2cqmftwkrtpojjxiyluovzq)
>
> **Locking**
> : [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxwy33dnm)
> : [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxk3tmn5rww)
>
> **Managing refresh**
> : [refresh](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxezlgojsxg2a)
> : [refreshInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxezlgojsxg2cjnz2gk4twmfwa)
> : [setRefreshInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxgzlukjswm4tfonues3tumvzhmylm)
> : [setStatus](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxgzlukn2gc5dvom)
>
> **Managing cancellation**
> : [cancel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxwgylomnswy)
> : [isCancelled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxws42dmfxggzlmnrswi)

## Instance Methods

---

### cancel

`public WOComponent cancel()`

Cancels the request. You should bind a
cancel button on the refresh page to this method.

__See
Also:__  [isCancelled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxws42dmfxggzlmnrswi)

---

### cancelPageForStatus

`public WOComponent cancelPageForStatus(Object status)`

Returns the cancel page, which is displayed
when the request is cancelled.

---

### isCancelled

`public boolean isCancelled()`

Returns true if the request has been cancelled.
The long running computation should check this value to see if it
should abort.

__See Also:__  [cancel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxwgylomnswy)

---

### lock

`public void lock()`

Locks the page.

__See
Also:__  [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxk3tmn5rww)

---

### pageForException

`public WOComponent pageForException(Throwable anException)`

Returns the exception page, which is displayed
when an exception occurs in [performAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxazlsmzxxe3kbmn2gs33o).

---

### pageForResult

`public WOComponent pageForResult(Object aResult)`

Returns the result page that is displayed when [performAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxazlsmzxxe3kbmn2gs33o) completes.

---

### performAction

`public Object performAction()`

Override this method to perform the requested
long computation. Returns the result of that computation as an object.

---

### refresh

`public WOComponent refresh()`

Called by the WOMetaRefresh invokeAction callback
(can also be called manually if the page is not self refreshing).
This method either invokes [pageForException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxaylhmvdg64sfpbrwk4dunfxw4), [pageForResult](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxaylhmvdg64ssmvzxk3du), [refreshPageForStatus](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxezlgojsxg2cqmftwkrtpojjxiyluovzq),
or [cancelPageForStatus](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxwgylomnswyudbm5sum33skn2gc5dvom) depending
on the state of the long response.

---

### refreshInterval

`public double refreshInterval()`

Returns the interval after which the refresh
page is refreshed.

---

### refreshPageForStatus

`public WOComponent refreshPageForStatus(Object status)`

Returns the page that is displayed while the
long-running computation is running. This page displays the current
status of the computation.

---

### setRefreshInterval

`public void setRefreshInterval(double interval)`

Sets the refresh interval.

__See
Also:__  [refreshInterval](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxxezlgojsxg2cjnz2gk4twmfwa)

---

### setStatus

`public void setStatus(Object status)`

Sets the status of the computation to _status_.
The long computation should send this message periodically so that
the refresh page reflects the status of the computation.

---

### unlock

`public void unlock()`

Unlocks the page.

__See
Also:__  [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjrxw4z2smvzxa33oonsvaylhmuxwy33dnm)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
