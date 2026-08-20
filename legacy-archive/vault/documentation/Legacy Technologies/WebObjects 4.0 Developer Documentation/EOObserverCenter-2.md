---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOObserverCenter.html
archived_at: '2026-07-18T01:28:36.972291Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOObjectStoreCoordinator-2.md)
[!](EOObserverProxy-2.md)

---

# EOObserverCenter

__Inherits From:__
NSObject

__Conforms To:__ NSObject (NSObject)

__Declared in:__ EOControl/EOObserver.h

EOObserverCenter is the central player in EOControl's change tracking mechanism. EOObserverCenter records observers and the objects they observe, and it distributes notifications when the observable objects change. For an overview of the change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework-2.md) in the introduction to the EOControl Framework.

You don't ever create instances of EOObserverCenter. Instead, the class itself acts as the central manager of change notification, registering observers and notifying them of changes. The EOObserverCenter API is provided entirely in class methods.

---

### Registering an Observer

Objects that directly observe others must adopt the EOObserving protocol, which consists of the single method [__objectWillChange:__](EOObserving-2.md). To register an object as an observer, invoke EOObserverCenter's __addObserver:forObject:__ with the observer and the object to be observed. Once this is done, any time the observed object invokes its [__willChange__](EOEnterpriseObject-3.md)method, the observer is sent an [__objectWillChange:__](EOObserving-2.md)message informing it of the pending change. You can also register an observer to be notified when any object changes using __addOmniscientObserver:__ . This can be useful in certain situations, but as it's very costly to deal out frequent change notifications, you should use omniscient observers sparingly. To unregister either kind of observer, simply use the corresponding __remove...__ method.

---

### Change Notification

Objects that are about to change invoke [__willChange__](EOEnterpriseObject-3.md), a method that the Framework adds to NSObject. The implementations of this method invoke EOObserverCenter's __notifyObserversObjectWillChange:__ , which sends an [__objectWillChange:__](EOObserving-2.md)message to all observers registered for the object that's changing, as well as to any omniscient observers. __notifyObserversObjectWillChange:__ optimizes the process by suppressing redundant [__objectWillChange:__](EOObserving-2.md)messages when the same object invokes [__willChange__](EOEnterpriseObject-3.md)several times in a row (as often happens when multiple properties are changed). Change notification is immediate, and takes place _before_ the object's state changes. If you need to compare the object's state before and after the change, you must arrange to examine the new state at the end of the run loop.

You can suppress change notification when necessary, using the __suppressObserverNotification__ and __enableObserverNotification__ methods. While notification is suppressed, neither regular nor omniscient observers are informed of changes. These methods nest, so you can invoke __suppressObserverNotification__ multiple times, and notification isn't re-enabled until a matching number of __enableObserverNotification__ message have been sent.

**Registering and unregistering observers**

**+ addObserver:forObject:

**+ removeObserver:forObject:

**+ addOmniscientObserver:

**+ removeOmniscientObserver:********

**Notifying observers of change**

**+ notifyObserversObjectWillChange:**

**Getting observers**

**+ observersForObject:

**+ observerForObject:ofClass:****

**Suppressing change notification**

**+ suppressObserverNotification

**+ enableObserverNotification

**+ observerNotificationSuppressCount******

---

#### addObserver:forObject:

+ (void)__addObserver:__ (id <EOObserving>)_anObserver___forObject:__ (id)_anObject_

Records _anObserver_ to be notified with an [__objectWillChange:__](EOObserving-2.md)message when _anObject_ changes.

__See also:__ + __removeObserver:forObject:__

---

#### addOmniscientObserver:

+ (void)__addOmniscientObserver:__ (id <EOObserving>)_anObserver_

Records _anObserver_ to be notified with an [__objectWillChange:__](EOObserving-2.md)message when any object changes. This can cause significant performance degradation, and so should be used with care. The ominiscient observer must be prepared to receive the [__objectWillChange:__](EOObserving-2.md)message with a `nil` argument.

__See also:__ + __addObserver:forObject:__ , + __removeOmniscientObserver:__

---

#### enableObserverNotification

+ (void)__enableObserverNotification__

Counters a prior __suppressObserverNotification__ message. When no such messages remain in effect, the __notifyObserversObjectWillChange:__ method is re-enabled. Raises an NSInternalInconsistencyException if not paired with a prior __suppressObserverNotification__ message.

---

#### notifyObserversObjectWillChange:

+ (void)__notifyObserversObjectWillChange:__ (id)_anObject_

Unless change notification is suppressed, sends an [__objectWillChange:__](EOObserving-2.md)to all observers registered for _anObject_ with that object as the argument, and sends that message to all omniscient observers as well. If invoked several times in a row with the same object, only the first invocation has any effect, since subsequent change notifications are redundant.

If an observer wants to ensure that it receives notification the next time the last object to change changes again, it should use the statement:

> ```
> [EOObserverCenter notifyObserversObjectWillChange:nil];
> ```

An observable object (typically an enterprise object) invokes this method from its [__willChange__](EOEnterpriseObject-3.md)implementation, so you should never have to invoke this method directly.

__See also:__ + __suppressObserverNotification__ , + __addObserver:forObject:__ , + __addOmniscientObserver:__

---

#### observerForObject:ofClass:

+ (id)__observerForObject:__ (id)_anObject___ofClass:__ (Class)_aClass_

Returns an observer for _anObject_ that's a kind of _aClass_. If more than one observer of _anObject_ is a kind of _aClass_, the specific observer returned is undetermined. You can use __observersForObject:__ instead to get all observers and examine their class membership.

---

#### observerNotificationSuppressCount

+ (unsigned int)__observerNotificationSuppressCount__

Returns the number of __suppressObserverNotification__ messages in effect.

__See also:__ + __enableObserverNotification__

---

#### observersForObject:

+ (NSArray \*)__observersForObject:__ (id)_anObject_

Returns all observers of _anObject_.

---

#### removeObserver:forObject:

+ (void)__removeObserver:__ (id <EOObserving>)_anObserver_ __forObject:__ (id)_anObject_

Removes _anObserver_ as an observer of _anObject_.

__See also:__ - __addObserver:forObject:__

---

#### removeOmniscientObserver:

+ (void)__removeOmniscientObserver:__ (id <EOObserving>)_anObserver_

Unregisters _anObserver_ as an observer of all objects.

__See also:__ + __removeObserver:forObject:__ , + __addOmniscientObserver:__

---

#### suppressObserverNotification

+ (void)__suppressObserverNotification__

Disables the __notifyObserversObjectWillChange:__ method, so that no change notifications are sent. This method can be invoked multiple times; __enableObserverNotification__ must then be invoked an equal number of times to re-enable change notification.

---

[!](EOObjectStoreCoordinator-2.md)
[!](EOObserverProxy-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
