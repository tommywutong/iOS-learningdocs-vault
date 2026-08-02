---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/More/EODelayedObserverQueue.html
archived_at: '2026-07-15T08:11:40.111301Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)

# EODelayedObserverQueue

## Enqueuing a Delayed Observer

The [enqueueObserver:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmvxhc5lfovsu6yttmvzhmzlshi) method records an
EODelayedObserver for later change notification. However, enqueuing
is usually performed automatically by an EODelayedObserver in its [objectWillChange:](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpn5rguzldorlws3dminugc3thmu5a) method.
Hence, it's typically enough that an object being observed invoke [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu) as needed. For example,
in Java Client and Application Kit applications, an EODisplayGroup
(EOInterface) does this (among many other things) on receiving an [EOObjectsChangedInEditingContextNotification](EOEditingContext-2.md#apple-ijeuiq2gjbeem)from
its EOEditingContext.

Although you can create individual EODelayedObserverQueues using __alloc__ and [init](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpnfxgs5a), you typically use the single
instance provided by the class method [defaultObserverQueue](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuizlmmf4wkzcpmjzwk4twmvzfc5lfovss6zdfmzqxk3duj5rhgzlsozsxeulvmv2wk).
Using separate queues bypasses the prioritization mechanism, which
may cause problems between the objects using the separate queues.
If you do use separate queues, your EODelayedObserver subclasses
should record a designated EODelayedObserverQueue that they always
use, and implement [observerQueue](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpn5rhgzlsozsxeulvmv2wk) to return that object.

If you need to remove an enqueued observer, you can do so
using the [dequeueObserver:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmrsxc5lfovsu6yttmvzhmzlshi) method. EODelayedObserver
also defines the [discardPendingNotification](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpmruxgy3bojsfazlomruw4z2on52gsztjmnqxi2lpny) method,
which removes the receiver from its designated queue. This is useful
in an object's implementation of __dealloc__,
for example, to prevent a change notification from being sent to
it.

## Change Notification

The actual process of change notification is initiated by
the [enqueueObserver:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpmvxhc5lfovsu6yttmvzhmzlshi) messages that line observers
up to receive notifications. Regardless of how many times __enqueueObserver:__ is
invoked for a particular observer, that observer is only put in
the queue once. The first observer enqueued during the run loop
also triggers the EODelayedObserverQueue to set up a delayed invocation
of [notifyObserversUpToPriority:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpnzxxi2lgpfhwe43foj3gk4ttkvyfi32qojuw64tjor4tu),
which causes it to receive that message at the end of the run loop. EODelayedObserver
sets up this delayed invocation in NSDefaultRunLoopMode, but you
can change the mode or add additional modes in which delayed invocation
occurs using [setRunLoopModes:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjponsxiutvnzgg633qjvxwizlthi).

[notifyObserversUpToPriority:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpnzxxi2lgpfhwe43foj3gk4ttkvyfi32qojuw64tjor4tu) cycles
through the queue of EODelayedObservers in priority order, from [EOObserverPriorityFirst](EODelayedObserver-3.md#apple-incuorcfi5dee) to the priority
given, sending each observer a [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) message. Each time,
it returns to the earliest priority (rather than continuing through
the queue) in case the message resulted in another EODelayedObserver
with a earlier priority being enqueued. This guarantees an optimal
delivery of change notifications.

## Observer Proxies

It may not always be possible for a custom observer class
to inherit from EODelayedObserver. To aid such objects in participating
in delayed change notifications, the Framework defines a subclass
of EODelayedObserver, EOObserverProxy, which implements its [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) method to invoke an action
method of your custom object. You create an EOObserverProxy, using
the [initWithTarget:action:priority:](EOObserverProxy-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2pmjzwk4twmvzfa4tppb4s62lonf2fo2lunbkgc4thmv2duyldoruw63r2obzgs33snf2hsoq) method,
which records the "real" observer, the action method to invoke,
and the priority at which the EOObserverProxy should be enqueued.
Then, instead of registering the custom object as an observer of
objects, you register the proxy (using EOObserverCenter's [addObserver:forObject:](EOObserverCenter-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5rhgzlsozsxeotgn5ze6ytkmvrxioq)__)__.
When the proxy receives an [objectWillChange:](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpn5rguzldorlws3dminugc3thmu5a) message,
it enqueues itself for delayed change notification, receives the __subjectChanged__ message
from the EODelayedObserverQueue, and then sends the action message
to the "real" observer.

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
