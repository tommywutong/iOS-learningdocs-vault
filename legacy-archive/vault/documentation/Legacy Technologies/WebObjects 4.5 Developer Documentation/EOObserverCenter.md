---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOObserverCenter.html
archived_at: '2026-07-15T08:11:37.851839Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOObserverCenter

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

EOObserverCenter is the central player in EOControl's change
tracking mechanism. EOObserverCenter records observers and the objects
they observe, and it distributes notifications when the observable
objects change. For an overview of the change tracking mechanism,
see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework.md#apple-ijeucrchivauo) in the introduction to the
EOControl Framework.

You don't ever create instances of EOObserverCenter. Instead,
the class itself acts as the central manager of change notification,
registering observers and notifying them of changes. The EOObserverCenter
API is provided entirely in static methods.

## Registering an Observer

Objects that directly observe others must implement the EOObserving interface,
which consists of the single method [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu).
To register an object as an observer, invoke EOObserverCenter's [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q) with the observer and
the object to be observed. Once this is done, any time the observed object
invokes its [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq) method, the observer is
sent an `objectWillChange` message informing
it of the pending change. You can also register an observer to be
notified when any object changes using [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhw23tjonrwszloorhwe43foj3gk4q). This can be
useful in certain situations, but as it's very costly to deal
out frequent change notifications, you should use omniscient observers
sparingly. To unregister either kind of observer, simply use the
corresponding `remove...` method.

## Change Notification

Objects that are about to change invoke [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq), a method defined by the
EOEnterpriseObject interface. The implementations of this method
invoke EOObserverCenter's [notifyObserversObjectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc63tporuwm6kpmjzwk4twmvzhgt3cnjswg5cxnfwgyq3imfxgozi),
which sends an [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) message
to all observers registered for the object that's changing, as
well as to any omniscient observers. `notifyObserversObjectWillChange` optimizes
the process by suppressing redundant `objectWillChange` messages
when the same object invokes [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq) several times in a row
(as often happens when multiple properties are changed). Change
notification is immediate, and takes place _before_ the
object's state changes. If you need to compare the object's
state before and after the change, you must arrange to examine the
new state at the end of the run loop.

You can suppress change notification when necessary, using
the [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny) and [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6zlomfrgyzkpmjzwk4twmvze433unftgsy3boruw63q) methods.
While notification is suppressed, neither regular nor omniscient observers
are informed of changes. These methods nest, so you can invoke `suppressObserverNotification` multiple
times, and notification isn't re-enabled until a matching number
of `enableObserverNotification` message have
been sent.

## Method Types

---

> **Registering and unregistering
> observers**
> : [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q)
> : [removeObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpmjzwk4twmvza)
> : [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhw23tjonrwszloorhwe43foj3gk4q)
> : [removeOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpnvxgs43dnfsw45cpmjzwk4twmvza)
>
> **Notifying observers of
> change**
> : [notifyObserversObjectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc63tporuwm6kpmjzwk4twmvzhgt3cnjswg5cxnfwgyq3imfxgozi)
>
> **Getting observers**
> : [observersForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc633consxe5tfojzum33sj5rguzldoq)
> : [observerForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc633consxe5tfojdg64spmjvgky3u)
>
> **Suppressing change notification**
> : [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny)
> : [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6zlomfrgyzkpmjzwk4twmvze433unftgsy3boruw63q)
> : [observerNotificationSuppressCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc633consxe5tfojhg65djmzuwgylunfxw4u3vobyhezltonbw65looq)

## Static Methods

---

### addObserver

`public static void addObserver(
EOObserving anObserver,
Object anObject)`

Records _anObserver_ to
be notified with an [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) message
when _anObject_ changes.

__See
Also:__  [removeObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpmjzwk4twmvza)

---

### addOmniscientObserver

`public static void addOmniscientObserver(EOObserving anObserver)`

Records _anObserver_ to
be notified with an [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) message
when any object changes. This can cause significant performance
degradation, and so should be used with care. The ominiscient observer must
be prepared to receive the `objectWillChange` message
with a null argument.

__See Also:__  [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q), [removeOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpnvxgs43dnfsw45cpmjzwk4twmvza)

---

### enableObserverNotification

`public static void enableObserverNotification()`

Counters a prior [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny) message.
When no such messages remain in effect, the [notifyObserversObjectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc63tporuwm6kpmjzwk4twmvzhgt3cnjswg5cxnfwgyq3imfxgozi) method
is re-enabled. Throws an exception if not paired with a prior [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny) message.

---

### notifyObserversObjectWillChange

`public static void notifyObserversObjectWillChange(Object anObject)`

Unless change notification is suppressed, sends
an [objectWillChange](EOObserving.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) to
all observers registered for _anObject_ with
that object as the argument, and sends that message to all omniscient
observers as well. If invoked several times in a row with the same
object, only the first invocation has any effect, since subsequent
change notifications are redundant.

If an observer wants to
ensure that it receives notification the next time the last object
to change changes again, it should use the statement:

> ```
> EOObserverCenter.notifyObserversObjectWillChange(null);
> ```

An
observable object (typically an enterprise object) invokes this
method from its [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq) implementation, so you
should never have to invoke this method directly.

__See
Also:__  [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny), [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q), [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhw23tjonrwszloorhwe43foj3gk4q)

---

### observerForObject

`public static EOObserving observerForObject(
Object anObject,
Class aClass)`

Returns an observer for _anObject_ that's
a kind of _aClass._ If more than one
observer of _anObject_ is a kind of _aClass,_
the specific observer returned is undetermined. You can use [observersForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc633consxe5tfojzum33sj5rguzldoq) instead
to get all observers and examine their class membership.

---

### observerNotificationSuppressCount

`public static int observerNotificationSuppressCount()`

Returns the number of [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc643vobyhezltonhwe43foj3gk4son52gsztjmnqxi2lpny) messages
in effect.

__See Also:__  [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6zlomfrgyzkpmjzwk4twmvze433unftgsy3boruw63q)

---

### observersForObject

`public static NSArray observersForObject(Object anObject)`

Returns all observers of _anObject._

---

### removeObserver

`public static void removeObserver(
EOObserving anObserver,
Object anObject)`

Removes _anObserver_ as
an observer of _anObject._

__See
Also:__  [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q)

---

### removeOmniscientObserver

`public static void removeOmniscientObserver(EOObserving anObserver)`

Unregisters _anObserver_ as
an observer of all objects.

__See Also:__  [removeObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc64tfnvxxmzkpmjzwk4twmvza), [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhw23tjonrwszloorhwe43foj3gk4q)

---

### suppressObserverNotification

`public static void suppressObserverNotification()`

Disables the [notifyObserversObjectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc63tporuwm6kpmjzwk4twmvzhgt3cnjswg5cxnfwgyq3imfxgozi) method,
so that no change notifications are sent. This method can be invoked
multiple times; [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6zlomfrgyzkpmjzwk4twmvze433unftgsy3boruw63q) must
then be invoked an equal number of times to re-enable change notification.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
