---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/Concepts/EODelayedObserverQueueCon.html
archived_at: '2026-07-15T08:13:43.636365Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md)

# EODelayedObserverQueue.Concepts

## Enqueuing a Delayed Observer

The enqueueObserver method records an EODelayedObserver for later change notification. However, enqueuing is usually performed automatically by an EODelayedObserver in its objectWillChange method. Hence, it's typically enough that an object being observed invoke willChange as needed. For example, in Java Client and Application Kit applications, an EODisplayGroup (EOInterface) does this (among many other things) on receiving an ObjectsChangedInEditingContextNotificationfrom its EOEditingContext.

Although you can create individual EODelayedObserverQueues, you typically use the single instance provided by the static method defaultObserverQueue. Using separate queues bypasses the prioritization mechanism, which may cause problems between the objects using the separate queues. If you do use separate queues, your EODelayedObserver subclasses should record a designated EODelayedObserverQueue that they always use, and implement observerQueue to return that object.

If you need to remove an enqueued observer, you can do so using the dequeueObserver method. EODelayedObserver also defines the discardPendingNotification method, which removes the receiver from its designated queue.

## Change Notification

The actual process of change notification is initiated by the enqueueObserver messages that line observers up to receive notifications. Regardless of how many times __enqueueObserver__ is invoked for a particular observer, that observer is only put in the queue once. The first observer enqueued during the run loop also sets up the EODelayedObserverQueue to receive a message at the end of the run loop. EODelayedObserver sets up this delayed invocation in NSRunLoop.DefaultRunLoopMode, but you can change the mode or add additional modes in which delayed invocation occurs using.

notifyObserversUpToPriority cycles through the queue of EODelayedObservers in priority order, from ObserverPriorityFirst to the priority given, sending each observer a subjectChanged message. Each time, it returns to the earliest priority (rather than continuing through the queue) in case the message resulted in another EODelayedObserver with a earlier priority being enqueued. This guarantees an optimal delivery of change notifications.

## Observer Proxies

It may not always be possible for a custom observer class to inherit from EODelayedObserver. To aid such objects in participating in delayed change notifications, the Framework defines a subclass of EODelayedObserver, EOObserverProxy, which implements its subjectChanged method to invoke an action method of your custom object. You create an EOObserverProxy, providing the "real" observer, the action method to invoke, and the priority at which the EOObserverProxy should be enqueued. Then, instead of registering the custom object as an observer of objects, you register the proxy (using EOObserverCenter's addObserver__)__. When the proxy receives an objectWillChange message, it enqueues itself for delayed change notification, receives the __subjectChanged__ message from the EODelayedObserverQueue, and then sends the action message to the "real" observer.

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
