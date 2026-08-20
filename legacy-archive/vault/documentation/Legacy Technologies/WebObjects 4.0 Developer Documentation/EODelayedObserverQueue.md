---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EODelayedObserverQueue.html
archived_at: '2026-07-18T01:28:25.574848Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODelayedObserver-2.md)
[!](EODelayedObserverQueue-2.md)

---

# EODelayedObserverQueue

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Class Description

The EODelayedObserverQueue class is a part of EOControl's change tracking mechanism. An EODelayedObserverQueue collects change notifications for observers of multiple objects and notifies them of the changes _en masse_ during the application's run loop, according to their individual priorities. For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework.md) in the introduction to the EOControl Framework.

EODelayedObserverQueue's style of notification is particularly useful for coalescing and prioritizing multiple changes; the interface layer's EOAssociation classes use it extensively to update Java Client and Yellow Box user interfaces, for example. Instead of being told that an object will change, an EODelayedObserver is told that it did change, with a [__subjectChanged__](EODelayedObserver.md)message, as described in the EODelayedObserver class specification. Delayed observation is thus not useful for comparing old and new states, but only for examining the new state. Delayed observation also isn't ordinarily used outside the scope of a Java Client or Yellow Box application (in a command line tool or WebObjects application, for example).

The motivation for a delayed change notification mechanism arises mainly from issues in observing multiple objects. Any single change to an observed object typically requires the observer to update some state or perform an action. When many such objects change, it makes no sense to recalculate the new state and perform the action for each object. EODelayedObserverQueue allows these changes to be collected into a single notification. It further orders change notifications according to priorities, allowing observers to be updated in sequence according to dependencies among them. For example, an EOMasterDetailAssociation (EOInterface), which must update its detail EODisplayGroup (EOInterface) according to the selection in the master _before_ any redisplay occurs, has an earlier priority than the default for EOAssociations. This prevents regular EOAssociations from redisplaying old values and then displaying the new values after the EOMasterDetailAssociation updates.

For more information on using EODelayedObserverQueues, see the sections

- [Enqueuing a Delayed Observer](EODelayedObserverQueue-2.md)
- [Change Notification](EODelayedObserverQueue-2.md)
- [Observer Proxies](EODelayedObserverQueue-2.md)

## Constants

EODelayedObserverQueue defines the following constant:

| __Constant__ | __Type__ | __Description__ |
| FlushDelayedObserversRunLoop | int | Determines when to notify delayed observers are notified, during end of event processing. |

```
```

## Method Types

**Constructors**

**EODelayedObserverQueue**

**Getting the default queue**

**+ defaultObserverQueue**

**Enqueuing and dequeuing observers**

**- enqueueObserver

**- dequeueObserver****

**Sending change notifications**

**- notifyObserversUpToPriority**

**Configuring notification behavior**

**- runLoopModes (Yellow Box only)

**- setRunLoopModes (Yellow Box only)****

## Constructors

---

#### EODelayedObserverQueue

public __EODelayedObserverQueue__ ()

Creates and returns a new EODelayedObserverQueue with NSRunLoop.DefaultRunLoopMode as its only run loop mode.

__See also:__ __runLoopModes__ (Yellow Box only)

## Static Methods

---

#### defaultObserverQueue

public static EODelayedObserverQueue __defaultObserverQueue__ ()

Returns the EODelayedObserverQueue that EODelayedObservers use by default.

## Instance Methods

---

#### dequeueObserver

public void __dequeueObserver__ (EODelayedObserver _anObserver_)

Removes _anObserver_ from the receiver.

__See also:__ - __enqueueObserver__

---

#### enqueueObserver

public void __enqueueObserver__ (EODelayedObserver _anObserver_)

Records _anObserver_ to be sent [__subjectChanged__](EODelayedObserver.md)messages. If _anObserver_'s priority is [ObserverPriorityImmediate](EODelayedObserver.md), it's immediately sent the message and not enqueued. Otherwise _anObserver_ is sent the message the next time __notifyObserversUpToPriority__ is invoked with a priority later than or equal to _anObserver_'s. Does nothing if _anObserver_ is already recorded.

The first time this method is invoked during the run loop with an observer whose priority isn't [ObserverPriorityImmediate](EODelayedObserver.md), it registers the receiver to be sent a __notifyObserversUpToPriority__ message at the end of the run loop, using FlushDelayedObserversRunLoopOrdering and the receiver's run loop modes. This causes enqueued observers up to a priority of [ObserverPrioritySixth](EODelayedObserver.md) to be notified automatically during each pass of the run loop.

When _anObserver_ is done observing changes, it should invoke __[discardPendingNotification](EODelayedObserver.md)__ to remove itself from the queue.

__See also:__ - __dequeueObserver__ , [- __priority__](EODelayedObserver.md)(EODelayedObserver), [- __discardPendingNotification__](EODelayedObserver.md)(EODelayedObserver), - __runLoopModes__ (Yellow Box only)

---

#### notifyObserversUpToPriority

public void __notifyObserversUpToPriority__ (int _priority_)

Sends [__subjectChanged__](EODelayedObserver.md)messages to all of the receiver's enqueued observers whose priority is _priority_ or earlier. This method cycles through the receiver's enqueued observers in priority order, sending each a [__subjectChanged__](EODelayedObserver.md)message and then returning to the very beginning of the queue, in case another observer with an earlier priority was enqueued as a result of the message.

EODelayedObserverQueue invokes this method automatically as needed during the run loop, with a _priority_ of [ObserverPrioritySixth](EODelayedObserver.md).

__See also:__ - __enqueueObserver__ , [- __priority__](EODelayedObserver.md)(EODelayedObserver)

---

#### runLoopModes

public NSArray __runLoopModes__ ()

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Returns the receiver's run loop modes.

---

#### setRunLoopModes

public void __setRunLoopModes__ (NSArray _modes_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Sets the receiver's run loop modes to _modes_, an array of NSString objects representing run loop modes. For more information see the Foundation class NSRunLoop.

---

[!](EODelayedObserver-2.md)
[!](EODelayedObserverQueue-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
