---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EODelayedObserver.html
archived_at: '2026-07-18T01:28:35.405946Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EODataSource-4.md)
[!](EODelayedObserver-4.md)

---

# EODelayedObserver

__Inherits From:__
NSObject

__Conforms To:__ EODelayedObserving
NSObject (NSObject)

__Declared in:__ EOControl/EOObserver.h

---

### Class Description

The EODelayedObserver class is a part of EOControl's change tracking mechanism. It is an abstract superclass that defines the basic functionality for coalescing change notifications for multiple objects and postponing notification according to a prioritized queue. For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework-2.md) in the introduction to the EOControl Framework.

EODelayedObserver is primarily used to implement the interface layer's associations and wouldn't ordinarily be used outside the scope of a Java Client or Yellow Box application (not in a command line tool or WebObjects application, for example). See the [EODelayedObserverQueue](EODelayedObserverQueue-3.md) class specification for general information.

You would never create an instance of EODelayedObserver. Instead, you use subclasses-typically EOAssociations (EOInterface). For information on creating your own EODelayedObserver subclass, see "[Creating a Subclass of EODelayedObserver](EODelayedObserver-4.md)."

## Constants

The following integer constants are defined to represent the priority of a notification in the queue:

| EOObserverPriorityImmediate | EOObserverPriorityFourth |
| EOObserverPriorityFirst | EOObserverPriorityFifth |
| EOObserverPrioritySecond | EOObserverPrioritySixth |
| EOObserverPriorityThird | EOObserverPriorityLater |

```
```

---

## Adopted Protocols

**EOObserving**

**- objectWillChange:**

---

### Method Types

**Change notification**

**- subjectChanged**

**Canceling change notification**

**- discardPendingNotification**

**Getting the queue and priority**

**- observerQueue

**- priority****

---

### Instance Methods

---

#### discardPendingNotification

- (void)__discardPendingNotification__

Sends a [__dequeueObserver:__](EODelayedObserverQueue-3.md)message to the receiver's EODelayedObserverQueue to clear it from receiving a change notification. A subclass of EODelayedObserver should invoke this method in its implementation of __dealloc__ .

__See also:__ __observerQueue__

---

#### objectWillChange:

@protocol EOObserving

- (void)__objectWillChange:__ (id)_anObject_

Implemented by EODelayedObserver to enqueue the receiver on its EODelayedObserverQueue. Subclasses shouldn't need to override this method; if they do, they must be sure to invoke __super__ 's implementation.

__See also:__ __observerQueue__ , [- __enqueueObserver:__](EODelayedObserverQueue-3.md)(EODelayedObserverQueue), [__objectWillChange:__](EOObserving-2.md)(EOObserving)

---

#### observerQueue

- (EODelayedObserverQueue \*)__observerQueue__

Overridden by subclasses to return the receiver's designated EODelayedObserverQueue. EODelayedObserver's implementation returns the default EODelayedObserverQueue.

__See also:__ __[defaultObserverQueue](EODelayedObserverQueue-3.md)__ (EODelayedObserverQueue)

---

#### priority

- (EOObserverPriority)__priority__

Overridden by subclasses to return the receiver's change notification priority, one of:

- EOObserverPriorityImmediate
- EOObserverPriorityFirst
- EOObserverPrioritySecond
- EOObserverPriorityThird
- EOObserverPriorityFourth
- EOObserverPriorityFifth
- EOObserverPrioritySixth
- EOObserverPriorityLater

EODelayedObserver's implementation returns EOObserverPriorityThird. See the EODelayedObserverQueue class specification for more information on priorities.

---

#### subjectChanged

- (void)__subjectChanged__

Implemented by subclasses to examine the receiver's observed objects and take whatever action is necessary. EODelayedObserver's implementation does nothing.

---

[!](EODataSource-4.md)
[!](EODelayedObserver-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
