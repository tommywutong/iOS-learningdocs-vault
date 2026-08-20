---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EODelayedObserverQueue.html
archived_at: '2026-07-15T08:11:39.619599Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EODelayedObserverQueue

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSObject
> : (NSObject)

> __Declared in:__ : EOControl/EOObserver.h

---

## Class Description

---

The EODelayedObserverQueue class is a part of EOControl's
change tracking mechanism. An EODelayedObserverQueue collects change
notifications for observers of multiple objects and notifies them
of the changes _en masse_ during the
application's run loop, according to their individual priorities. For
an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework-2.md#apple-ijeucrchivauo) in
the introduction to the EOControl Framework.

EODelayedObserverQueue's style of notification is particularly
useful for coalescing and prioritizing multiple changes; the interface
layer's EOAssociation classes use it extensively to update Java
Client and Application Kit user interfaces, for example. Instead
of being told that an object will change, an EODelayedObserver is
told that it did change, with a [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) message, as described
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

- ["Enqueuing a Delayed Observer"](EODelayedObserverQueue-4.md#apple-ijauercgijbei)
- ["Change Notification"](EODelayedObserverQueue-4.md#apple-ijauercijjbes)
- ["Observer Proxies"](EODelayedObserverQueue-4.md#apple-ijaueq2kifcuc)

## Constants

---

In EOObserver.h, EOControl defines an
enumeration with the following constant:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| EOFlushDelayedObserversRunLoopOrdering | Determines when to notify delayed observers during end of event processing. |

## Method Types

---

> **Creating instances**
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpnfxgs5a)
>
> **Getting the default queue**
> : [+ defaultObserverQueue](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuizlmmf4wkzcpmjzwk4twmvzfc5lfovss6zdfmzqxk3duj5rhgzlsozsxeulvmv2wk)
>
> **Enqueuing and dequeuing
> observers**
> : [- enqueueObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmvxhc5lfovsu6yttmvzhmzlshi)
> : [- dequeueObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmrsxc5lfovsu6yttmvzhmzlshi)
>
> **Sending change notifications**
> : [- notifyObserversUpToPriority:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpnzxxi2lgpfhwe43foj3gk4ttkvyfi32qojuw64tjor4tu)
>
> **Configuring notification
> behavior**
> : [- runLoopModes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpoj2w4tdpn5ye233emvzq)
> : [- setRunLoopModes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjponsxiutvnzgg633qjvxwizlthi)

## Class Methods

---

### defaultObserverQueue

`+ (EODelayedObserverQueue *)defaultObserverQueue`

Returns the EODelayedObserverQueue that EODelayedObservers
use by default.

---

## Instance Methods

---

### dequeueObserver:

`- (void)dequeueObserver:(EODelayedObserver
*)anObserver`

Removes _anObserver_ from
the receiver.

__See Also:__  [- enqueueObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmvxhc5lfovsu6yttmvzhmzlshi)

---

### enqueueObserver:

`- (void)enqueueObserver:(EODelayedObserver
*)anObserver`

Records _anObserver_ to
be sent [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) messages. If _anObserver_'s
priority is [EOObserverPriorityImmediate](EODelayedObserver-3.md#apple-incuorcjircem), it's
immediately sent the message and not enqueued. Otherwise _anObserver_ is
sent the message the next time [notifyObserversUpToPriority:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpnzxxi2lgpfhwe43foj3gk4ttkvyfi32qojuw64tjor4tu) is invoked
with a priority later than or equal to _anObserver_'s.
Does nothing if _anObserver_ is already
recorded.

The first time this method is invoked during the
run loop with an observer whose priority isn't `EOObserverPriorityImmediate`,
it registers the receiver to be sent a [notifyObserversUpToPriority:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpnzxxi2lgpfhwe43foj3gk4ttkvyfi32qojuw64tjor4tu) message
at the end of the run loop, using [EOFlushDelayedObserversRunLoopOrdering](#apple-ijauerkdjfcek) and
the receiver's run loop modes. This causes enqueued observers
up to a priority of [EOObserverPrioritySixth](EODelayedObserver-3.md#apple-incuorceindum) to be notified
automatically during each pass of the run loop.

This
method does not retain anObserver. When _anObserver_ is __deallocated__,
it should invoke [dequeueObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmrsxc5lfovsu6yttmvzhmzlshi) to
remove itself from the queue.

__See Also:__  [- dequeueObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmrsxc5lfovsu6yttmvzhmzlshi), [- priority](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpobzgs33snf2hs) (EODelayedObserver), [- discardPendingNotification](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpmruxgy3bojsfazlomruw4z2on52gsztjmnqxi2lpny) (EODelayedObserver), [- runLoopModes](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpoj2w4tdpn5ye233emvzq), __-
performSelector:target:argument:order:modes:__ (NSRunLoop
class of the Foundation Kit)

---

### init

`- (id)init`

Initializes a newly allocated EODelayedObserverQueue
with NSDefaultRunLoopMode as its only run loop mode. This is the
designated initializer for the EODelayedObserverQueue class. Returns __self__.

---

### notifyObserversUpToPriority:

`- (void)notifyObserversUpToPriority:(EOObserverPriority)priority`

Sends [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) messages to all of
the receiver's enqueued observers whose priority is _priority_ or
earlier. This method cycles through the receiver's enqueued observers
in priority order, sending each a __subjectChanged__message
and then returning to the very beginning of the queue, in case another observer
with an earlier priority was enqueued as a result of the message.

EODelayedObserverQueue
invokes this method automatically as needed during the run loop,
with a _priority_ of [EOObserverPrioritySixth](EODelayedObserver-3.md#apple-incuorceindum).

__See
Also:__  [- enqueueObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmvxhc5lfovsu6yttmvzhmzlshi), [- priority](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpobzgs33snf2hs) (EODelayedObserver)

---

### runLoopModes

`- (NSArray *)runLoopModes`

Returns the receiver's run loop modes.

---

### setRunLoopModes:

`- (void)setRunLoopModes:(NSArray
*)modes`

Sets the receiver's run loop modes to _modes_,
an array of NSString objects representing run loop modes. For more
information see the Foundation class NSRunLoop.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
