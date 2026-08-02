---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOObserverCenter.html
archived_at: '2026-07-18T01:28:26.982384Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOObjectStoreCoordinator.md)
[!](EOObserverProxy.md)

---

# EOObserverCenter

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Class Description

EOObserverCenter is the central player in EOControl's change tracking mechanism. EOObserverCenter records observers and the objects they observe, and it distributes notifications when the observable objects change. For an overview of the change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework.md) in the introduction to the EOControl Framework.

You don't ever create instances of EOObserverCenter. Instead, the class itself acts as the central manager of change notification, registering observers and notifying them of changes. The EOObserverCenter API is provided entirely in static methods.

---

### Registering an Observer

Objects that directly observe others must implement the EOObserving interface, which consists of the single method [__objectWillChange__](EOObserving.md). To register an object as an observer, invoke EOObserverCenter's __addObserver__ with the observer and the object to be observed. Once this is done, any time the observed object invokes its [__willChange__](EOEnterpriseObject.md)method, the observer is sent an [__objectWillChange__](EOObserving.md)message informing it of the pending change. You can also register an observer to be notified when any object changes using __addOmniscientObserver__ . This can be useful in certain situations, but as it's very costly to deal out frequent change notifications, you should use omniscient observers sparingly. To unregister either kind of observer, simply use the corresponding __remove...__ method.

---

### Change Notification

Objects that are about to change invoke [__willChange__](EOEnterpriseObject.md), a method defined by the EOEnterpriseObject interface. The implementations of this method invoke EOObserverCenter's __notifyObserversObjectWillChange__ , which sends an [__objectWillChange__](EOObserving.md)message to all observers registered for the object that's changing, as well as to any omniscient observers. __notifyObserversObjectWillChange__ optimizes the process by suppressing redundant [__objectWillChange__](EOObserving.md)messages when the same object invokes [__willChange__](EOEnterpriseObject.md)several times in a row (as often happens when multiple properties are changed). Change notification is immediate, and takes place _before_ the object's state changes. If you need to compare the object's state before and after the change, you must arrange to examine the new state at the end of the run loop.

You can suppress change notification when necessary, using the __suppressObserverNotification__ and __enableObserverNotification__ methods. While notification is suppressed, neither regular nor omniscient observers are informed of changes. These methods nest, so you can invoke __suppressObserverNotification__ multiple times, and notification isn't re-enabled until a matching number of __enableObserverNotification__ message have been sent.

## Method Types

**Registering and unregistering observers**

**+ addObserver

**+ removeObserver

**+ addOmniscientObserver

**+ removeOmniscientObserver********

**Notifying observers of change**

**+ notifyObserversObjectWillChange**

**Getting observers**

**+ observersForObject

**+ observerForObject****

**Suppressing change notification**

**+ suppressObserverNotification

**+ enableObserverNotification

**+ observerNotificationSuppressCount******

## Static Methods

---

#### addObserver

public static void __addObserver__ (
EOObserving _anObserver_,
java.lang.Object _anObject_)

Records _anObserver_ to be notified with an [__objectWillChange__](EOObserving.md)message when _anObject_ changes.

__See also:__ + __removeObserver__

---

#### addOmniscientObserver

public static void __addOmniscientObserver__ (EOObserving _anObserver_)

Records _anObserver_ to be notified with an [__objectWillChange__](EOObserving.md)message when any object changes. This can cause significant performance degradation, and so should be used with care. The ominiscient observer must be prepared to receive the [__objectWillChange__](EOObserving.md)message with a `null` argument.

__See also:__ + __addObserver__ , + __removeOmniscientObserver__

---

#### enableObserverNotification

public static void __enableObserverNotification__ ()

Counters a prior __suppressObserverNotification__ message. When no such messages remain in effect, the __notifyObserversObjectWillChange__ method is re-enabled. Throws an exception if not paired with a prior __suppressObserverNotification__ message.

---

#### notifyObserversObjectWillChange

public static void __notifyObserversObjectWillChange__ (java.lang.Object _anObject_)

Unless change notification is suppressed, sends an [__objectWillChange__](EOObserving.md)to all observers registered for _anObject_ with that object as the argument, and sends that message to all omniscient observers as well. If invoked several times in a row with the same object, only the first invocation has any effect, since subsequent change notifications are redundant.

If an observer wants to ensure that it receives notification the next time the last object to change changes again, it should use the statement:

> ```
> EOObserverCenter.notifyObserversObjectWillChange(null);
> ```

An observable object (typically an enterprise object) invokes this method from its [__willChange__](EOEnterpriseObject.md)implementation, so you should never have to invoke this method directly.

__See also:__ + __suppressObserverNotification__ , + __addObserver__ , + __addOmniscientObserver__

---

#### observerForObject

public static EOObserving __observerForObject__ (
java.lang.Object _anObject_,
java.lang.Class _aClass_)

Returns an observer for _anObject_ that's a kind of _aClass_. If more than one observer of _anObject_ is a kind of _aClass_, the specific observer returned is undetermined. You can use __observersForObject__ instead to get all observers and examine their class membership.

---

#### observerNotificationSuppressCount

public static int __observerNotificationSuppressCount__ ()

Returns the number of __suppressObserverNotification__ messages in effect.

__See also:__ + __enableObserverNotification__

---

#### observersForObject

public static NSArray __observersForObject__ (java.lang.Object _anObject_)

Returns all observers of _anObject_.

---

#### removeObserver

public static void __removeObserver__ (
EOObserving _anObserver_,
java.lang.Object _anObject_)

Removes _anObserver_ as an observer of _anObject_.

__See also:__ - __addObserver__

---

#### removeOmniscientObserver

public static void __removeOmniscientObserver__ (EOObserving _anObserver_)

Unregisters _anObserver_ as an observer of all objects.

__See also:__ + __removeObserver__ , + __addOmniscientObserver__

---

#### suppressObserverNotification

public static void __suppressObserverNotification__ ()

Disables the __notifyObserversObjectWillChange__ method, so that no change notifications are sent. This method can be invoked multiple times; __enableObserverNotification__ must then be invoked an equal number of times to re-enable change notification.

---

[!](EOObjectStoreCoordinator.md)
[!](EOObserverProxy.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
