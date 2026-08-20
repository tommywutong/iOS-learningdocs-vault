---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/EODelayedObserverQueue_m.html
archived_at: '2026-07-18T01:28:27.958759Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EODelayedObserverQueue.md)
[!](EODetailDataSource.md)

---

# EODelayedObserverQueue

---

### Enqueuing a Delayed Observer

The [__enqueueObserver__](EODelayedObserverQueue.md)method records an EODelayedObserver for later change notification. However, enqueuing is usually performed automatically by an EODelayedObserver in its [__objectWillChange__](EODelayedObserver.md)method. Hence, it's typically enough that an object being observed invoke [__willChange__](EOEnterpriseObject.md)as needed. For example, in Siva and Yellow Box applications, an EODisplayGroup (EOInterface) does this (among many other things) on receiving an [ObjectsChangedInEditingContextNotification](EOEditingContext.md)from its EOEditingContext.

Although you can create individual EODelayedObserverQueues, you typically use the single instance provided by the static method [__defaultObserverQueue__](EODelayedObserverQueue.md). Using separate queues bypasses the prioritization mechanism, which may cause problems between the objects using the separate queues. If you do use separate queues, your EODelayedObserver subclasses should record a designated EODelayedObserverQueue that they always use, and implement [__observerQueue__](EODelayedObserver.md)to return that object.

If you need to remove an enqueued observer, you can do so using the [__dequeueObserver__](EODelayedObserverQueue.md)method. EODelayedObserver also defines the [__discardPendingNotification__](EODelayedObserver.md)method, which removes the receiver from its designated queue.

---

### Change Notification

The actual process of change notification is initiated by the [__enqueueObserver__](EODelayedObserverQueue.md)messages that line observers up to receive notifications. Regardless of how many times [__enqueueObserver__](EODelayedObserverQueue.md)is invoked for a particular observer, that observer is only put in the queue once. The first observer enqueued during the run loop also sets up the EODelayedObserverQueue to receive a message at the end of the run loop. EODelayedObserver sets up this delayed invocation in NSRunLoop.DefaultRunLoopMode, but you can change the mode or add additional modes in which delayed invocation occurs using [__setRunLoopModes__](EODelayedObserverQueue.md)(Yellow Box only).

[__notifyObserversUpToPriority__](EODelayedObserverQueue.md)cycles through the queue of EODelayedObservers in priority order, from [ObserverPriorityFirst](EODelayedObserver.md) to the priority given, sending each observer a [__subjectChanged__](EODelayedObserver.md)message. Each time, it returns to the earliest priority (rather than continuing through the queue) in case the message resulted in another EODelayedObserver with a earlier priority being enqueued. This guarantees an optimal delivery of change notifications.

---

### Observer Proxies

It may not always be possible for a custom observer class to inherit from EODelayedObserver. To aid such objects in participating in delayed change notifications, the Framework defines a subclass of EODelayedObserver, EOObserverProxy, which implements its [__subjectChanged__](EODelayedObserver.md)method to invoke an action method of your custom object. You create an EOObserverProxy, providing the "real" observer, the action method to invoke, and the priority at which the EOObserverProxy should be enqueued. Then, instead of registering the custom object as an observer of objects, you register the proxy (using EOObserverCenter's [__addObserver__](EOObserverCenter.md)__)__ . When the proxy receives an __[objectWillChange](EODelayedObserver.md)__ message, it enqueues itself for delayed change notification, receives the [__subjectChanged__](EODelayedObserver.md)message from the EODelayedObserverQueue, and then sends the action message to the "real" observer.

---

[!](EODelayedObserverQueue.md)
[!](EODetailDataSource.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
