---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObserverCenter.html
archived_at: '2026-07-15T08:11:39.929225Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOObserverCenter

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

EOObserverCenter is the central player in EOControl's change
tracking mechanism. EOObserverCenter records observers and the objects
they observe, and it distributes notifications when the observable
objects change. For an overview of the change tracking mechanism,
see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework-2.md#apple-ijeucrchivauo) in the introduction to the EOControl
Framework.

You don't ever create instances of EOObserverCenter. Instead,
the class itself acts as the central manager of change notification,
registering observers and notifying them of changes. The EOObserverCenter
API is provided entirely in class methods.

## Registering an Observer

Objects that directly observe others must adopt the EOObserving protocol,
which consists of the single method [objectWillChange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intfm/EOObserving/objectWillChange:).
To register an object as an observer, invoke EOObserverCenter's [addObserver:forObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5rhgzlsozsxeotgn5ze6ytkmvrxioq) with the observer
and the object to be observed. Once this is done, any time the observed
object invokes its [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu) method, the observer is
sent an __objectWillChange:__ message informing
it of the pending change. You can also register an observer to be
notified when any object changes using [addOmniscientObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5ww42ltmnuwk3tuj5rhgzlsozsxeoq). This can
be useful in certain situations, but as it's very costly to deal
out frequent change notifications, you should use omniscient observers
sparingly. To unregister either kind of observer, simply use the
corresponding __remove...__ method.

## Change Notification

Objects that are about to change invoke [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu), a method that the Framework
adds to NSObject. The implementations of this method invoke EOObserverCenter's [notifyObserversObjectWillChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixw433unfthst3consxe5tfojzu6ytkmvrxiv3jnrweg2dbnztwkoq), which
sends an [objectWillChange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intfm/EOObserving/objectWillChange:) message
to all observers registered for the object that's changing, as well
as to any omniscient observers. __notifyObserversObjectWillChange:__ optimizes
the process by suppressing redundant __objectWillChange:__ messages
when the same object invokes [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu) several times in a row
(as often happens when multiple properties are changed). Change
notification is immediate, and takes place _before_ the
object's state changes. If you need to compare the object's
state before and after the change, you must arrange to examine the
new state at the end of the run loop.

You can suppress change notification when necessary, using
the [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxg5lqobzgk43tj5rhgzlsozsxettporuwm2ldmf2gs33o) and [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwk3tbmjwgkt3consxe5tfojhg65djmzuwgylunfxw4) methods.
While notification is suppressed, neither regular nor omniscient observers
are informed of changes. These methods nest, so you can invoke __suppressObserverNotification__ multiple
times, and notification isn't re-enabled until a matching number
of __enableObserverNotification__ message have
been sent.

## Method Types

---

> **Registering and unregistering
> observers**
> : [+ addObserver:forObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5rhgzlsozsxeotgn5ze6ytkmvrxioq)
> : [+ removeObserver:forObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxezlnn53gkt3consxe5tfoi5gm33sj5rguzldoq5a)
> : [+ addOmniscientObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5ww42ltmnuwk3tuj5rhgzlsozsxeoq)
> : [+ removeOmniscientObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxezlnn53gkt3nnzuxgy3jmvxhit3consxe5tfoi5a)
>
> **Notifying observers of
> change**
> : [+ notifyObserversObjectWillChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixw433unfthst3consxe5tfojzu6ytkmvrxiv3jnrweg2dbnztwkoq)
>
> **Getting observers**
> : [+ observersForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixw6yttmvzhmzlsondg64spmjvgky3uhi)
> : [+ observerForObject:ofClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixw6yttmvzhmzlsizxxet3cnjswg5b2n5teg3dbonztu)
>
> **Suppressing change notification**
> : [+ suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxg5lqobzgk43tj5rhgzlsozsxettporuwm2ldmf2gs33o)
> : [+ enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwk3tbmjwgkt3consxe5tfojhg65djmzuwgylunfxw4)
> : [+ observerNotificationSuppressCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixw6yttmvzhmzlsjzxxi2lgnfrwc5djn5xfg5lqobzgk43tinxxk3tu)

## Class Methods

---

### addObserver:forObject:

`+ (void)addObserver:(id
<EOObserving>)anObserver
forObject:(id)anObject`

Records _anObserver_ to
be notified with an [objectWillChange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intfm/EOObserving/objectWillChange:) message
when _anObject_ changes.

__See
Also:__  [+ removeObserver:forObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxezlnn53gkt3consxe5tfoi5gm33sj5rguzldoq5a)

---

### addOmniscientObserver:

`+ (void)addOmniscientObserver:(id
<EOObserving>)anObserver`

Records _anObserver_ to
be notified with an [objectWillChange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intfm/EOObserving/objectWillChange:) message
when any object changes. This can cause significant performance
degradation, and so should be used with care. The ominiscient observer
must be prepared to receive the __objectWillChange:__ message
with a nil argument.

__See Also:__  [+ addObserver:forObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5rhgzlsozsxeotgn5ze6ytkmvrxioq), [+ removeOmniscientObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxezlnn53gkt3nnzuxgy3jmvxhit3consxe5tfoi5a)

---

### enableObserverNotification

`+ (void)enableObserverNotification`

Counters a prior [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxg5lqobzgk43tj5rhgzlsozsxettporuwm2ldmf2gs33o) message.
When no such messages remain in effect, the [notifyObserversObjectWillChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixw433unfthst3consxe5tfojzu6ytkmvrxiv3jnrweg2dbnztwkoq) method
is re-enabled. Raises an NSInternalInconsistencyException if not
paired with a prior [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxg5lqobzgk43tj5rhgzlsozsxettporuwm2ldmf2gs33o) message.

---

### notifyObserversObjectWillChange:

`+ (void)notifyObserversObjectWillChange:(id)anObject`

Unless change notification is suppressed, sends
an [objectWillChange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intfm/EOObserving/objectWillChange:) to
all observers registered for _anObject_ with
that object as the argument, and sends that message to all omniscient
observers as well. If invoked several times in a row with the same
object, only the first invocation has any effect, since subsequent
change notifications are redundant.

If an observer wants to
ensure that it receives notification the next time the last object
to change changes again, it should use the statement:

> ```
> [EOObserverCenter notifyObserversObjectWillChange:nil];
> ```

An
observable object (typically an enterprise object) invokes this
method from its [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu) implementation, so you
should never have to invoke this method directly.

__See
Also:__  [+ suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxg5lqobzgk43tj5rhgzlsozsxettporuwm2ldmf2gs33o), [+ addObserver:forObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5rhgzlsozsxeotgn5ze6ytkmvrxioq), [+ addOmniscientObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5ww42ltmnuwk3tuj5rhgzlsozsxeoq)

---

### observerForObject:ofClass:

`+ (id)observerForObject:(id)anObject
ofClass:(Class)aClass`

Returns an observer for _anObject_ that's
a kind of _aClass_. If more than one
observer of _anObject_ is a kind of _aClass_,
the specific observer returned is undetermined. You can use [observersForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixw6yttmvzhmzlsondg64spmjvgky3uhi) instead
to get all observers and examine their class membership.

---

### observerNotificationSuppressCount

`+ (unsigned int)observerNotificationSuppressCount`

Returns the number of [suppressObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxg5lqobzgk43tj5rhgzlsozsxettporuwm2ldmf2gs33o) messages
in effect.

__See Also:__  [+ enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwk3tbmjwgkt3consxe5tfojhg65djmzuwgylunfxw4)

---

### observersForObject:

`+ (NSArray *)observersForObject:(id)anObject`

Returns all observers of _anObject_.

---

### removeObserver:forObject:

`+ (void)removeObserver:(id
<EOObserving>)anObserver
forObject:(id)anObject`

Removes _anObserver_ as
an observer of _anObject_.

__See
Also:__  [- addObserver:forObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5rhgzlsozsxeotgn5ze6ytkmvrxioq)

---

### removeOmniscientObserver:

`+ (void)removeOmniscientObserver:(id
<EOObserving>)anObserver`

Unregisters _anObserver_ as
an observer of all objects.

__See Also:__  [+ removeObserver:forObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixxezlnn53gkt3consxe5tfoi5gm33sj5rguzldoq5a), [+ addOmniscientObserver:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwczdej5ww42ltmnuwk3tuj5rhgzlsozsxeoq)

---

### suppressObserverNotification

`+ (void)suppressObserverNotification`

Disables the [notifyObserversObjectWillChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixw433unfthst3consxe5tfojzu6ytkmvrxiv3jnrweg2dbnztwkoq) method,
so that no change notifications are sent. This method can be invoked
multiple times; [enableObserverNotification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhu6yttmvzhmzlsinsw45dfoixwk3tbmjwgkt3consxe5tfojhg65djmzuwgylunfxw4) must
then be invoked an equal number of times to re-enable change notification.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
