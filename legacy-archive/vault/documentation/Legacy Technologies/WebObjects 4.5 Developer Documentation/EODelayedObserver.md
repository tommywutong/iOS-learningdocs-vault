---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EODelayedObserver.html
archived_at: '2026-07-15T08:11:37.433499Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EODelayedObserver

> **__Inherits from:__**
> : (com.apple.client.eocontrol) Object
>
> (com.apple.yellow.eocontrol) NSObject

> **__Implements:__**
> : EOObserving
> : (com.apple.client.eocontrol only) NSInlineObservable

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

The EODelayedObserver class is a part of EOControl's change
tracking mechanism. It is an abstract superclass that defines the
basic functionality for coalescing change notifications for multiple
objects and postponing notification according to a prioritized queue.
For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework.md#apple-ijeucrchivauo) in the introduction to the EOControl Framework.

EODelayedObserver is primarily used to implement the interface
layer's associations and wouldn't ordinarily be used outside
the scope of a Java Client or Application Kit application (not in
a command line tool or WebObjects application, for example). See
the [EODelayedObserverQueue](EODelayedObserverQueue.md#apple-ivhuizlmmf4wkzcpmjzwk4twmvzfc5lfovsq) class specification
for general information.

You would never create an instance of EODelayedObserver. Instead,
you use subclasses-typically EOAssociations (EOInterface). For
information on creating your own EODelayedObserver subclass, see ["Creating a Subclass of EODelayedObserver"](EODelayedObserver-2.md#apple-ineuuqsjifbeq).

## Constants

---

EODelayedObserver defines the following `int` constants
to represent the priority of a notification in the queue:

|  |  |
| --- | --- |
| ObserverPriorityImmediate | ObserverPriorityFourth |
| ObserverPriorityFirst | ObserverPriorityFifth |
| ObserverPrioritySecond | ObserverPrioritySixth |
| ObserverPriorityThird | ObserverPriorityLater |

EODelayedObserver also defines the following `int` constant
to identify the number of defined priorities (8 by default).

- ObserverNumberOfPriorities

## Interfaces Implemented

---

> EOObserving: [objectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe2tfmn2fo2lmnrbwqylom5sq)
>
> NSInlineObservable: `observerData`
> : `setObserverData`

## Method Types

---

> **Change notification**
> : [subjectChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle)
>
> **Canceling change notification**
> : [discardPendingNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5sgs43dmfzgiudfnzsgs3thjzxxi2lgnfrwc5djn5xa)
>
> **Getting the queue and
> priority**
> : [observerQueue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe43foj3gk4srovsxkzi)
> : [priority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5yhe2lpojuxi6i)

## Instance Methods

---

### discardPendingNotification

`public void discardPendingNotification()`

Sends a [dequeueObserver](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sgk4lvmv2wkt3consxe5tfoi) message to the receiver's
EODelayedObserverQueue to clear it from receiving a change notification.
A subclass of EODelayedObserver should invoke this method when its
done observing changes.

__See
Also:__  [observerQueue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe43foj3gk4srovsxkzi)

---

### objectWillChange

`public void objectWillChange(Object anObject)`

Implemented by EODelayedObserver to enqueue
the receiver on its EODelayedObserverQueue. Subclasses shouldn't
need to override this method; if they do, they must be sure to invoke `super`'s implementation.

__See
Also:__  [observerQueue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe43foj3gk4srovsxkzi), [enqueueObserver](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sw44lvmv2wkt3consxe5tfoi) (EODelayedObserverQueue), [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) (EOObserving)

---

### observerQueue

`public EODelayedObserverQueue observerQueue()`

Overridden by subclasses to return the receiver's
designated EODelayedObserverQueue. EODelayedObserver's implementation
returns the default EODelayedObserverQueue.

__See
Also:__  [defaultObserverQueue](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdfnrqxszlej5rhgzlsozsxeulvmv2wkl3emvtgc5lmorhwe43foj3gk4srovsxkzi) (EODelayedObserverQueue)

---

### priority

`public int priority()`

Overridden by subclasses to return the receiver's
change notification priority, one of:

- [ObserverPriorityImmediate](#apple-incuorcjircem)
- [ObserverPriorityFirst](#apple-incuorcfi5dee)
- [ObserverPrioritySecond](#apple-incuoq2fjjeuo)
- [ObserverPriorityThird](#apple-incuoq2difeem)
- [ObserverPriorityFourth](#apple-ineuusseifdue)
- [ObserverPriorityFifth](#apple-incuoq2gjfauu)
- [ObserverPrioritySixth](#apple-incuorceindum)
- [ObserverPriorityLater](#apple-incuorkcizbeq)

EODelayedObserver's
implementation returns `ObserverPriorityThird`.
See the EODelayedObserverQueue class specification for more information
on priorities.

---

### subjectChanged

`public abstract void subjectChanged()`

Implemented by subclasses to examine the receiver's
observed objects and take whatever action is necessary. EODelayedObserver's
implementation does nothing.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
