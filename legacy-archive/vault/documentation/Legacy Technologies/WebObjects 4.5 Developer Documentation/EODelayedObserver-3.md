---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EODelayedObserver.html
archived_at: '2026-07-15T08:11:39.604122Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EODelayedObserver

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : EODelayedObserving
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EOObserver.h

---

## Class Description

---

The EODelayedObserver class is a part of EOControl's change
tracking mechanism. It is an abstract superclass that defines the
basic functionality for coalescing change notifications for multiple
objects and postponing notification according to a prioritized queue.
For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework-2.md#apple-ijeucrchivauo) in
the introduction to the EOControl Framework.

EODelayedObserver is primarily used to implement the interface
layer's associations and wouldn't ordinarily be used outside
the scope of a Java Client or Application Kit application (not in
a command line tool or WebObjects application, for example). See
the [EODelayedObserverQueue](EODelayedObserverQueue-3.md#apple-ivhuizlmmf4wkzcpmjzwk4twmvzfc5lfovsq) class specification
for general information.

You would never create an instance of EODelayedObserver. Instead,
you use subclasses-typically EOAssociations (EOInterface). For
information on creating your own EODelayedObserver subclass, see ["Creating a Subclass of EODelayedObserver"](EODelayedObserver-4.md#apple-ineuuqsjifbeq).

## Constants

---

In EOObserver.h, EOControl defines the
enumeration type `EOObserverPriority` to
represent the priority of a notification in the queue. The `EOObserverPriority` type's
constants are:

|  |  |
| --- | --- |
| EOObserverPriorityImmediate | EOObserverPriorityFourth |
| EOObserverPriorityFirst | EOObserverPriorityFifth |
| EOObserverPrioritySecond | EOObserverPrioritySixth |
| EOObserverPriorityThird | EOObserverPriorityLater |

EOObserver.h also defines the following `int` constant
to identify the number of defined priorities (8 by default).

- ObserverNumberOfPriorities

## Adopted Protocols

---

> EOObserving: [- objectWillChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpn5rguzldorlws3dminugc3thmu5a)

## Method Types

---

> **Change notification**
> : [- subjectChanged](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza)
>
> **Canceling change notification**
> : [- discardPendingNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpmruxgy3bojsfazlomruw4z2on52gsztjmnqxi2lpny)
>
> **Getting the queue and
> priority**
> : [- observerQueue](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpn5rhgzlsozsxeulvmv2wk)
> : [- priority](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpobzgs33snf2hs)

## Instance Methods

---

### discardPendingNotification

`- (void)discardPendingNotification`

Sends a [dequeueObserver:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmrsxc5lfovsu6yttmvzhmzlshi) message to the receiver's
EODelayedObserverQueue to clear it from receiving a change notification.
A subclass of EODelayedObserver should invoke this method in its implementation
of __dealloc__.

__See Also:__  [- observerQueue](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpn5rhgzlsozsxeulvmv2wk)

---

### objectWillChange:

`- (void)objectWillChange:(id)anObject`

Implemented by EODelayedObserver to enqueue
the receiver on its EODelayedObserverQueue. Subclasses shouldn't
need to override this method; if they do, they must be sure to invoke __super__'s implementation.

__See
Also:__  [- observerQueue](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpn5rhgzlsozsxeulvmv2wk), [- enqueueObserver:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmvxhc5lfovsu6yttmvzhmzlshi) (EODelayedObserverQueue), [objectWillChange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intfm/EOObserving/objectWillChange:) (EOObserving)

---

### observerQueue

`- (EODelayedObserverQueue *)observerQueue`

Overridden by subclasses to return the receiver's
designated EODelayedObserverQueue. EODelayedObserver's implementation
returns the default EODelayedObserverQueue.

__See
Also:__  [defaultObserverQueue](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuizlmmf4wkzcpmjzwk4twmvzfc5lfovss6zdfmzqxk3duj5rhgzlsozsxeulvmv2wk) (EODelayedObserverQueue)

---

### priority

`- (EOObserverPriority)priority`

Overridden by subclasses to return the receiver's
change notification priority, one of:

- [EOObserverPriorityImmediate](#apple-incuorcjircem)
- [EOObserverPriorityFirst](#apple-incuorcfi5dee)
- [EOObserverPrioritySecond](#apple-incuoq2fjjeuo)
- [EOObserverPriorityThird](#apple-incuoq2difeem)
- [EOObserverPriorityFourth](#apple-ineuusseifdue)
- [EOObserverPriorityFifth](#apple-incuoq2gjfauu)
- [EOObserverPrioritySixth](#apple-incuorceindum)
- [EOObserverPriorityLater](#apple-incuorkcizbeq)

EODelayedObserver's
implementation returns `EOObserverPriorityThird`.
See the EODelayedObserverQueue class specification for more information
on priorities.

---

### subjectChanged

`- (void)subjectChanged`

Implemented by subclasses to examine the receiver's
observed objects and take whatever action is necessary. EODelayedObserver's
implementation does nothing.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
