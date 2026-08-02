---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOObserverCenter.html
archived_at: '2026-07-15T08:13:47.154844Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOObserverCenter

> __Inherits from:__ Object

> __Package:__ com.webobjects.eocontrol

---

## Class Description

---

EOObserverCenter is the central player in EOControl's change tracking mechanism. EOObserverCenter records observers and the objects they observe, and it distributes notifications when the observable objects change. For an overview of the change tracking mechanism, see ["Tracking Enterprise Objects Changes" (page 22)](The%20EOControl%20Framework.md#apple-ijeucrchivauo) in the introduction to the EOControl Framework.

You don't ever create instances of EOObserverCenter. Instead, the class itself acts as the central manager of change notification, registering observers and notifying them of changes. The EOObserverCenter API is provided entirely in static methods.

EOObserverCenter is implemented using weak references (see the Sun documentation of java.lang.ref for details). Thus, if EOObserverCenter is the last object in your application with a reference to either an object which is registered to receive notifications, or to an object which is being observed, the object is garbage collected.

## Registering an Observer

Objects that directly observe others must implement the EOObserving interface, which consists of the single method objectWillChange. To register an object as an observer, invoke EOObserverCenter's [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q) with the observer and the object to be observed. Once this is done, any time the observed object invokes its willChange method, the observer is sent an __objectWillChange__ message informing it of the pending change. You can also register an observer to be notified when any object changes using [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhw23tjonrwszloorhwe43foj3gk4q). This can be useful in certain situations, but as it's very costly to deal out frequent change notifications, you should use omniscient observers sparingly. To unregister either kind of observer, simply use the corresponding __remove...__ method.

## Change Notification

Objects that are about to change invoke willChange, a method defined by the EOEnterpriseObject interface. The implementations of this method invoke EOObserverCenter's [notifyObserversObjectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc63tporuwm6kpmjzwk4twmvzhgt3cnjswg5cxnfwgyq3imfxgozi), which sends an objectWillChange message to all observers registered for the object that's changing, as well as to any omniscient observers. __notifyObserversObjectWillChange__ optimizes the process by suppressing redundant __objectWillChange__ messages when the same object invokes willChange several times in a row (as often happens when multiple properties are changed). Change notification is immediate, and takes place _before_ the object's state changes. If you need to compare the object's state before and after the change, you must arrange to examine the new state at the end of the run loop.

You can suppress change notification when necessary, using the [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny) and [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6zlomfrgyzkpmjzwk4twmvze433unftgsy3boruw63q) methods. While notification is suppressed, neither regular nor omniscient observers are informed of changes. These methods nest, so you can invoke __suppressObserverNotification__ multiple times, and notification isn't re-enabled until a matching number of __enableObserverNotification__ message have been sent.

## Method Types

---

> Registering and unregistering observers[addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q)[removeObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpmjzwk4twmvza)[addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhw23tjonrwszloorhwe43foj3gk4q)[removeOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpnvxgs43dnfsw45cpmjzwk4twmvza)Notifying observers of change[notifyObserversObjectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc63tporuwm6kpmjzwk4twmvzhgt3cnjswg5cxnfwgyq3imfxgozi)Getting observers[observersForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc633consxe5tfojzum33sj5rguzldoq)[observerForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc633consxe5tfojdg64spmjvgky3u)Suppressing change notification[suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny)[enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6zlomfrgyzkpmjzwk4twmvze433unftgsy3boruw63q)[observerNotificationSuppressCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc633consxe5tfojhg65djmzuwgylunfxw4u3vobyhezltonbw65looq)

## Constructors

---

### EOObserverCenter

`public EOObserverCenter()`

Description forthcoming.

---

## Static Methods

---

### addObserver

`public static synchronized void addObserver( EOObserving anObserver, Object anObject)`

Records _anObserver_ to be notified with an objectWillChange message when _anObject_ changes.

__See Also:__ [removeObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpmjzwk4twmvza)

---

### addOmniscientObserver

`public static synchronized void addOmniscientObserver(EOObserving anObserver)`

Records _anObserver_ to be notified with an objectWillChange message when any object changes. This can cause significant performance degradation, and so should be used with care. The ominiscient observer must be prepared to receive the __objectWillChange__ message with a null argument.

__See Also:__ [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q), [removeOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpnvxgs43dnfsw45cpmjzwk4twmvza)

---

### enableObserverNotification

`public static void enableObserverNotification()`

Counters a prior [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny) message. When no such messages remain in effect, the [notifyObserversObjectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc63tporuwm6kpmjzwk4twmvzhgt3cnjswg5cxnfwgyq3imfxgozi) method is re-enabled. Throws an exception if not paired with a prior [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny) message.

---

### notifyObserversObjectWillChange

`public synchronized void notifyObserversObjectWillChange(Object anObject)`

Unless change notification is suppressed, sends an objectWillChange to all observers registered for _anObject_ with that object as the argument, and sends that message to all omniscient observers as well. If invoked several times in a row with the same object, only the first invocation has any effect, since subsequent change notifications are redundant.

If an observer wants to ensure that it receives notification the next time the last object to change changes again, it should use the statement:

```
EOObserverCenter.notifyObserversObjectWillChange(null);
```

An observable object (typically an enterprise object) invokes this method from its willChange implementation, so you should never have to invoke this method directly.

__See Also:__ [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny), [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q), [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhw23tjonrwszloorhwe43foj3gk4q)

---

### observerForObject

`public static synchronized EOObserving observerForObject( Object anObject, Class aClass)`

Returns an observer for _anObject_ that's a kind of _aClass_. If more than one observer of _anObject_ is a kind of _aClass_, the specific observer returned is undetermined. You can use [observersForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc633consxe5tfojzum33sj5rguzldoq) instead to get all observers and examine their class membership.

---

### observerNotificationSuppressCount

`public static int observerNotificationSuppressCount()`

Returns the number of [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny) messages in effect.

__See Also:__ [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6zlomfrgyzkpmjzwk4twmvze433unftgsy3boruw63q)

---

### observersForObject

`public static synchronized NSArray observersForObject(Object anObject)`

Returns all observers of _anObject_.

---

### removeObserver

`public static synchronized void removeObserver( EOObserving anObserver, Object anObject)`

Removes _anObserver_ as an observer of _anObject_.

__See Also:__ [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q)

---

### removeOmniscientObserver

`public static synchronized void removeOmniscientObserver(EOObserving anObserver)`

Unregisters _anObserver_ as an observer of all objects.

__See Also:__ [removeObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpmjzwk4twmvza), [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhw23tjonrwszloorhwe43foj3gk4q)

---

### suppressObserverNotification

`public static void suppressObserverNotification()`

Disables the [notifyObserversObjectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc63tporuwm6kpmjzwk4twmvzhgt3cnjswg5cxnfwgyq3imfxgozi) method, so that no change notifications are sent. This method can be invoked multiple times; [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6zlomfrgyzkpmjzwk4twmvze433unftgsy3boruw63q) must then be invoked an equal number of times to re-enable change notification.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
