---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/EODelayedObserver_m.html
archived_at: '2026-07-18T01:28:37.794245Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODelayedObserver-3.md)
[!](EODelayedObserverQueue-3.md)

---

# EODelayedObserver

---

### Creating a Subclass of EODelayedObserver

EODelayedObserver implements the basic __[objectWillChange:](EODelayedObserver-3.md)__ method to simply enqueue the receiver on an EODelayedObserverQueue. Regardless of how many of these messages the receiver gets during the run loop, it receives a single [__subjectChanged__](EODelayedObserver-3.md)message from the queue-at the end of the run loop. In this method the delayed observer can check for changes and take whatever action is necessary. Subclasses should record objects they're interested in, perhaps in an __init__ method, and examine them in [__subjectChanged__](EODelayedObserver-3.md). An EOAssociation.(EOInterface) for example, examines each of the EODisplayGroups (EOInterface) it's bound to in order to find out what has changed. Another kind of subclass might record each changed object for later examination by overriding __[objectWillChange:](EODelayedObserver-3.md)__ , but it must be sure to invoke __super__ 's implementation when doing so.

The rest of EODelayedObserver's methods have meaningful, if static, default implementations. EODelayedObserverQueue sends change notifications according to the priority of each enqueued observer. EODelayedObserver's implementation of the [__priority__](EODelayedObserver-3.md)method returns [EOObserverPriorityThird](EODelayedObserver-3.md). Your subclass can override it to return a higher or lower priority, or to have a settable priority. The other method a subclass might override is __[observerQueue](EODelayedObserver-3.md)__ , which returns a default EODelayedObserverQueue normally shared by all EODelayedObservers. Because sharing a single queue keeps all EODelayedObserver's synchronized according to their priority, you should rarely override this method, doing so only if your subclass is involved in a completely independent system.

A final method, [__discardPendingNotification__](EODelayedObserver-3.md), need never be overridden by subclasses, but must be invoked from their implementation of __dealloc__ . This prevents observers from being sent change notifications after they've been deallocated.

---

[!](EODelayedObserver-3.md)
[!](EODelayedObserverQueue-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
