---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/More/EODelayedObserverQueue.html
archived_at: '2026-07-15T08:11:38.064146Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)

# EODelayedObserverQueue

## Enqueuing a Delayed Observer

The [enqueueObserver](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sw44lvmv2wkt3consxe5tfoi) method records an
EODelayedObserver for later change notification. However, enqueuing
is usually performed automatically by an EODelayedObserver in its [objectWillChange](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe2tfmn2fo2lmnrbwqylom5sq) method.
Hence, it's typically enough that an object being observed invoke [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq) as needed. For example,
in Java Client and Application Kit applications, an EODisplayGroup
(EOInterface) does this (among many other things) on receiving an [ObjectsChangedInEditingContextNotification](EOEditingContext.md#apple-ijeuiq2gjbeem)from
its EOEditingContext.

Although you can create individual EODelayedObserverQueues,
you typically use the single instance provided by the static method [defaultObserverQueue](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdfnrqxszlej5rhgzlsozsxeulvmv2wkl3emvtgc5lmorhwe43foj3gk4srovsxkzi).
Using separate queues bypasses the prioritization mechanism, which
may cause problems between the objects using the separate queues.
If you do use separate queues, your EODelayedObserver subclasses
should record a designated EODelayedObserverQueue that they always
use, and implement [observerQueue](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe43foj3gk4srovsxkzi) to return that object.

If you need to remove an enqueued observer, you can do so
using the [dequeueObserver](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sgk4lvmv2wkt3consxe5tfoi) method. EODelayedObserver
also defines the [discardPendingNotification](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5sgs43dmfzgiudfnzsgs3thjzxxi2lgnfrwc5djn5xa) method,
which removes the receiver from its designated queue.

## Change Notification

The actual process of change notification is initiated by
the [enqueueObserver](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5sw44lvmv2wkt3consxe5tfoi) messages that line observers
up to receive notifications. Regardless of how many times `enqueueObserver` is
invoked for a particular observer, that observer is only put in
the queue once. The first observer enqueued during the run loop
also sets up the EODelayedObserverQueue to receive a message at
the end of the run loop. EODelayedObserver sets up this delayed
invocation in NSRunLoop.DefaultRunLoopMode, but you can change the
mode or add additional modes in which delayed invocation occurs
using [setRunLoopModes](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5zwk5csovxey33pobgw6zdfom) (Yellow Box only).

[notifyObserversUpToPriority](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5xg65djmz4u6yttmvzhmzlsonkxavdpkbzgs33snf2hs) cycles
through the queue of EODelayedObservers in priority order, from [ObserverPriorityFirst](EODelayedObserver.md#apple-incuorcfi5dee) to the priority
given, sending each observer a [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) message. Each time,
it returns to the earliest priority (rather than continuing through
the queue) in case the message resulted in another EODelayedObserver
with a earlier priority being enqueued. This guarantees an optimal
delivery of change notifications.

## Observer Proxies

It may not always be possible for a custom observer class
to inherit from EODelayedObserver. To aid such objects in participating
in delayed change notifications, the Framework defines a subclass
of EODelayedObserver, EOObserverProxy, which implements its [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) method to invoke an action
method of your custom object. You create an EOObserverProxy, providing the
"real" observer, the action method to invoke, and the priority
at which the EOObserverProxy should be enqueued. Then, instead of
registering the custom object as an observer of objects, you register
the proxy (using EOObserverCenter's [addObserver](EOObserverCenter.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q)`)`.
When the proxy receives an [objectWillChange](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5xwe2tfmn2fo2lmnrbwqylom5sq) message,
it enqueues itself for delayed change notification, receives the `subjectChanged` message
from the EODelayedObserverQueue, and then sends the action message
to the "real" observer.

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
