---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EODelayedObserverQueue.html
archived_at: '2026-07-15T08:11:37.449859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EODelayedObserverQueue

> **__Inherits from:__**
> : (com.apple.client.eocontrol) Object
>
> (com.apple.yellow.eocontrol) NSObject

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

The EODelayedObserverQueue class is a part of EOControl's
change tracking mechanism. An EODelayedObserverQueue collects change
notifications for observers of multiple objects and notifies them
of the changes _en masse_ during the application's
run loop, according to their individual priorities. For an overview
of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework.md#apple-ijeucrchivauo) in the introduction
to the EOControl Framework.

EODelayedObserverQueue's style of notification is particularly
useful for coalescing and prioritizing multiple changes; the interface
layer's EOAssociation classes use it extensively to update Java
Client and Application Kit user interfaces, for example. Instead
of being told that an object will change, an EODelayedObserver is
told that it did change, with a [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) message, as described
in the EODelayedObserver class specification. Delayed observation
is thus not useful for comparing old and new states, but only for
examining the new state. Delayed observation also isn't ordinarily
used outside the scope of a Java Client or Application Kit application
(in a command line tool or WebObjects application, for example).

The motivation for a delayed change notification mechanism
arises mainly from issues in observing multiple objects. Any single
change to an observed object typically requires the observer to
update some state or perform an action. When many such objects change,
it makes no sense to recalculate the new state and perform the action
for each object. EODelayedObserverQueue allows these changes to be
collected into a single notification. It further orders change notifications
according to priorities, allowing observers to be updated in sequence
according to dependencies among them. For example, an EOMasterDetailAssociation
(EOInterface), which must update its detail EODisplayGroup (EOInterface)
according to the selection in the master _before_ any
redisplay occurs, has an earlier priority than the default for EOAssociations.
This prevents regular EOAssociations from redisplaying old values
and then displaying the new values after the EOMasterDetailAssociation
updates.

For more information on using EODelayedObserverQueues, see
the sections

- ["Enqueuing a Delayed Observer"](EODelayedObserverQueue-2.md#apple-ijauercgijbei)
- ["Change Notification"](EODelayedObserverQueue-2.md#apple-ijauercijjbes)
- ["Observer Proxies"](EODelayedObserverQueue-2.md#apple-ijaueq2kifcuc)

## Constants

---

EODelayedObserverQueue defines the following `int` constant:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| FlushDelayedObserversRunLoopOrdering | Determines when to notify delayed observers during end of event processing. |

## Method Types

---

> **Constructors**
> : [EODelayedObserverQueue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5cu6rdfnrqxszlej5rhgzlsozsxeulvmv2wk)
>
> **Getting the default queue**
> : [defaultObserverQueue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdfnrqxszlej5rhgzlsozsxeulvmv2wkl3emvtgc5lmorhwe43foj3gk4srovsxkzi)
>
> **Enqueuing and dequeuing
> observers**
> : [enqueueObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sw44lvmv2wkt3consxe5tfoi)
> : [dequeueObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sgk4lvmv2wkt3consxe5tfoi)
>
> **Sending change notifications**
> : [notifyObserversUpToPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5xg65djmz4u6yttmvzhmzlsonkxavdpkbzgs33snf2hs)
>
> **Configuring notification
> behavior**
> : [runLoopModes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5zhk3smn5xxatlpmrsxg) (com.apple.yellow.eocontrol only)
> : [setRunLoopModes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5zwk5csovxey33pobgw6zdfom) (com.apple.yellow.eocontrol only)

## Constructors

---

### EODelayedObserverQueue

`public EODelayedObserverQueue()`

Creates and returns a new EODelayedObserverQueue
with NSRunLoop.DefaultRunLoopMode as its only run loop mode.

__See
Also:__  [runLoopModes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5zhk3smn5xxatlpmrsxg) (com.apple.yellow.eocontrol only)

---

## Static Methods

---

### defaultObserverQueue

`public static EODelayedObserverQueue defaultObserverQueue()`

Returns the EODelayedObserverQueue that EODelayedObservers
use by default.

---

## Instance Methods

---

### dequeueObserver

`public void dequeueObserver(EODelayedObserver anObserver)`

Removes _anObserver_ from
the receiver.

__See Also:__  [enqueueObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sw44lvmv2wkt3consxe5tfoi)

---

### enqueueObserver

`public void enqueueObserver(EODelayedObserver anObserver)`

Records _anObserver_ to
be sent [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) messages. If _anObserver_'s
priority is [ObserverPriorityImmediate](EODelayedObserver.md#apple-incuorcjircem), it's immediately
sent the message and not enqueued. Otherwise _anObserver_ is
sent the message the next time [notifyObserversUpToPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5xg65djmz4u6yttmvzhmzlsonkxavdpkbzgs33snf2hs) is invoked
with a priority later than or equal to _anObserver_'s.
Does nothing if _anObserver_ is already
recorded.

The first time this method is invoked during the
run loop with an observer whose priority isn't `ObserverPriorityImmediate`,
it registers the receiver to be sent a [notifyObserversUpToPriority](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5xg65djmz4u6yttmvzhmzlsonkxavdpkbzgs33snf2hs) message at
the end of the run loop, using [FlushDelayedObserversRunLoopOrdering](#apple-ijauerkdjfcek) and
the receiver's run loop modes. This causes enqueued observers
up to a priority of [ObserverPrioritySixth](EODelayedObserver.md#apple-incuorceindum) to be notified automatically
during each pass of the run loop.

When _anObserver_ is done
observing changes, it should invoke [discardPendingNotification](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5sgs43dmfzgiudfnzsgs3thjzxxi2lgnfrwc5djn5xa) to
remove itself from the queue.

__See Also:__  [dequeueObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sgk4lvmv2wkt3consxe5tfoi), [priority](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5yhe2lpojuxi6i) (EODelayedObserver), [discardPendingNotification](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5sgs43dmfzgiudfnzsgs3thjzxxi2lgnfrwc5djn5xa) (EODelayedObserver), [runLoopModes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5zhk3smn5xxatlpmrsxg) (com.apple.yellow.eocontrol only)

---

### notifyObserversUpToPriority

`public void notifyObserversUpToPriority(int priority)`

Sends [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) messages to all of
the receiver's enqueued observers whose priority is _priority_ or
earlier. This method cycles through the receiver's enqueued observers
in priority order, sending each a `subjectChanged`message
and then returning to the very beginning of the queue, in case another observer
with an earlier priority was enqueued as a result of the message.

EODelayedObserverQueue
invokes this method automatically as needed during the run loop,
with a _priority_ of [ObserverPrioritySixth](EODelayedObserver.md#apple-incuorceindum).

__See
Also:__  [enqueueObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sw44lvmv2wkt3consxe5tfoi), [priority](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5yhe2lpojuxi6i) (EODelayedObserver)

---

### runLoopModes

`public NSArray runLoopModes()`

(com.apple.yellow.eocontrol only) Returns
the receiver's run loop modes.

---

### setRunLoopModes

`public void setRunLoopModes(NSArray modes)`

(com.apple.yellow.eocontrol only) Sets
the receiver's run loop modes to _modes,_
an array of NSString objects representing run loop modes. For more
information see the Foundation class NSRunLoop.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
