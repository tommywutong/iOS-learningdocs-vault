---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EODelayedObserver.html
archived_at: '2026-07-18T01:28:25.468657Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODataSource-2.md)
[!](EODelayedObserver-2.md)

---

# EODelayedObserver

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Implements:__
EOObserving

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

The EODelayedObserver class is a part of EOControl's change tracking mechanism. It is an abstract superclass that defines the basic functionality for coalescing change notifications for multiple objects and postponing notification according to a prioritized queue. For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes](The%20EOControl%20Framework.md) in the introduction to the EOControl Framework.

EODelayedObserver is primarily used to implement the interface layer's associations and wouldn't ordinarily be used outside the scope of a Java Client or Yellow Box application (not in a command line tool or WebObjects application, for example). See the [EODelayedObserverQueue](EODelayedObserverQueue.md) class specification for general information.

You would never create an instance of EODelayedObserver. Instead, you use subclasses-typically EOAssociations (EOInterface). For information on creating your own EODelayedObserver subclass, see "[Creating a Subclass of EODelayedObserver](EODelayedObserver-2.md)."

## Constants

The following integer constants are defined to represent the priority of a notification in the queue:

| ObserverPriorityImmediate | ObserverPriorityFourth |
| ObserverPriorityFirst | ObserverPriorityFifth |
| ObserverPrioritySecond | ObserverPrioritySixth |
| ObserverPriorityThird | ObserverPriorityLater |

```
```

## Interfaces Implemented

**EOObserving**

**- objectWillChange**

## Method Types

**Change notification**

**- subjectChanged**

**Canceling change notification**

**- discardPendingNotification**

**Getting the queue and priority**

**- observerQueue

**- priority****

## Instance Methods

---

#### discardPendingNotification

public void __discardPendingNotification()__

Sends a [__dequeueObserver__](EODelayedObserverQueue.md)message to the receiver's EODelayedObserverQueue to clear it from receiving a change notification. A subclass of EODelayedObserver should invoke this method when its done observing changes.

__See also:__ __observerQueue__

---

#### objectWillChange

interface EOObserving

public void __objectWillChange__ (java.lang.Object _anObject_)

Implemented by EODelayedObserver to enqueue the receiver on its EODelayedObserverQueue. Subclasses shouldn't need to override this method; if they do, they must be sure to invoke __super__ 's implementation.

__See also:__ __observerQueue__ , [- __enqueueObserver__](EODelayedObserverQueue.md)(EODelayedObserverQueue), [__objectWillChange__](EOObserving.md)(EOObserving)

---

#### observerQueue

public EODelayedObserverQueue __observerQueue__ ()

Overridden by subclasses to return the receiver's designated EODelayedObserverQueue. EODelayedObserver's implementation returns the default EODelayedObserverQueue.

__See also:__ __[defaultObserverQueue](EODelayedObserverQueue.md)__ (EODelayedObserverQueue)

---

#### priority

public int __priority__ ()

()

Overridden by subclasses to return the receiver's change notification priority, one of:

- ObserverPriorityImmediate
- ObserverPriorityFirst
- ObserverPrioritySecond
- ObserverPriorityThird
- ObserverPriorityFourth
- ObserverPriorityFifth
- ObserverPrioritySixth
- ObserverPriorityLater

EODelayedObserver's implementation returns ObserverPriorityThird. See the EODelayedObserverQueue class specification for more information on priorities.

---

#### subjectChanged

public abstract void __subjectChanged__ ()

Implemented by subclasses to examine the receiver's observed objects and take whatever action is necessary. EODelayedObserver's implementation does nothing.

---

[!](EODataSource-2.md)
[!](EODelayedObserver-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
