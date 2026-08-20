---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOFaultHandler.html
archived_at: '2026-07-15T08:11:37.583459Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOFaultHandler

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

EOFaultHandler is an abstract class that defines the mechanisms
that create faults and help them to fire. __Faults__ are
used as placeholders for an enterprise object's relationship destinations.
For example, suppose an Employee object has a `department` relationship
to the employee's department. When an employee is fetched, faults
are created for its relationship destinations. In the case of the `department` relationship,
an empty Department object is created. The Department object's
data isn't fetched until the Department is accessed, at which
time the fault is said to __fire__.

Subclasses of EOFaultHandler perform the specific steps necessary
to get data for the fault and fire it. The Access Layer, for example,
uses private subclasses to fetch data using an EODatabaseContext (defined
in EOAccess). Most of EOFaultHandler's methods are properly defined;
you need only override [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi) to
provide appropriate behavior. In com.apple.yellow.eocontrol applications,
you can optionally implement [faultWillFire](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6ztbovwhiv3jnrwem2lsmu) to prepare for conversion.

In a com.apple.yellow.eocontrol application you create an EOFaultHandler using
the standard constructor. To create a fault in
a com.apple.yellow.eocontrol application, you invoke the static
method [makeObjectIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5wwc23fj5rguzldorew45dpizqxk3du) with
the object to turn into a fault and the EOFaultHandler. An EOFaultHandler belongs
exclusively to a single fault, and shouldn't be shared or used
by any other object.

In a com.apple.client.eocontrol application you also create
an EOFaultHandler using the standard constructor.
To create a fault in a com.apple.client.eocontrol application, though,
you send a newly-created object a [turnIntoFault](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3uovzg4sloorxumylvnr2a) message and provide
an EOFaultHandler that will help the fault to
fire. In order for that newly-created object to be able to respond
to `turnIntoFault`, the object must conform
to the [EOFaulting](EOFaulting.md#apple-ijcuiq2gijdee) interface.
An EOFaultHandler belongs exclusively to
a single fault, and shouldn't be shared or used by any other object.
In com.apple.client.eocontrol applications, the fault handler is
the private property of the fault; you shouldn't send any messages
to the fault handler, instead dealing exclusively with the fault.

## Firing a Fault

When a fault receives a message that requires it to fire,
it sends a [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi) method
to its EOFaultHandler. This method is responsible for invoking the [clearFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5rwyzlbojdgc5lmoq) method
to revert the fault to its original state, and then do whatever
is necessary to complete initialization of the object. Doing so
typically involves fetching data from an external repository and
passing it to the object.

## Method Types

---

> **Creating and examining
> faults**
> : [createFaultForDeferredFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3smvqxizkgmf2wy5cgn5zeizlgmvzhezleizqxk3du) (com.apple.yellow.eocontrol only)
> : [clearFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5rwyzlbojdgc5lmoq) (com.apple.yellow.eocontrol only)
> : [isFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5uxgrtbovwhi)
> : [makeObjectIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5wwc23fj5rguzldorew45dpizqxk3du) (com.apple.yellow.eocontrol only)
> : [handlerForFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5ugc3tenrsxertpojdgc5lmoq) (com.apple.yellow.eocontrol only)
> : [targetClassForFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf52gc4thmv2eg3dbonzum33sizqxk3du) (com.apple.yellow.eocontrol only)
>
> **Reference counting**
> : [incrementExtraRefCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc62lomnzgk3lfnz2ek6duojqvezlginxxk3tu) (com.apple.yellow.eocontrol only)
> : [decrementExtraRefCountIsZero](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6zdfmnzgk3lfnz2ek6duojqvezlginxxk3tujfzvuzlsn4) (com.apple.yellow.eocontrol only)
> : [extraRefCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6zlyorzgcutfmzbw65looq) (com.apple.yellow.eocontrol only)
>
> **Getting the original
> class**
> : [classForFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3mmfzxgrtpojdgc5lmoq) (com.apple.yellow.eocontrol only)
>
> **Firing a fault**
> : [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi)
> : [faultWillFire](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6ztbovwhiv3jnrwem2lsmu) (com.apple.yellow.eocontrol only)
>
> **Getting a description**
> : [descriptionForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6zdfonrxe2lqoruw63sgn5ze6ytkmvrxi)
> : [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5sw6u3imfwgy33xirsxgy3snfyhi2lpny) (com.apple.client.eocontrol only)
>
> **Checking class information**
> : [isKindOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc62ltjnuw4zcpmzbwyyltom) (com.apple.yellow.eocontrol only)
> : [isMemberOfClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc62ltjvsw2ytfojhwmq3mmfzxg) (com.apple.yellow.eocontrol only)
> : [respondsToSelectorForFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc64tfonyg63teonkg6u3fnrswg5dpojdg64sgmf2wy5a) (com.apple.yellow.eocontrol only)

## Static Methods

---

### eoShallowDescription

`public static String eoShallowDescription(Object anObject)`

(com.apple.client.eocontrol only) See the method
description for EOEnterpriseObject's [eoShallowDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwk32tnbqwy3dpo5cgk43dojuxa5djn5xa).

---

### clearFault

`public static void clearFault(Object aFault)`

(com.apple.yellow.eocontrol only) Restores _aFault_ to
its status prior to the [makeObjectIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5wwc23fj5rguzldorew45dpizqxk3du) message
that created it. Throws an exception if _aFault_ isn't
a fault.

You rarely use this method. Faults typically fire
automatically when accessed, using the [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi) method.

---

### handlerForFault

`public static EOFaultHandler handlerForFault(Object aFault)`

(com.apple.yellow.eocontrol only) Returns the
EOFaultHandler that will help _aFault_ to
fire. Returns `null` if _aFault_ isn't
a fault.

---

### isFault

`public static boolean isFault(Object anObject)`

Returns `true` if _anObject_ is
a fault, `false` otherwise.

---

### makeObjectIntoFault

`public static void makeObjectIntoFault(
Object anObject,
EOFaultHandler aFaultHandler)`

(com.apple.yellow.eocontrol only) Converts _anObject_ into
a fault, assigning _aFaultHandler_ as
the object that stores its original state and later converts the
fault back into a normal object (typically by fetching data from
an external repository). The new fault becomes the owner of _aFaultHandler_ ;
you shouldn't assign it to another object.

---

### targetClassForFault

`public static Class targetClassForFault(Object anObject)`

(com.apple.yellow.eocontrol only) Returns the
class that will be instantiated when the fault fires. The returned
class could be a superclass of the actual class instantiated.

---

## Instance Methods

---

### classForFault

`public Class classForFault(Object fault)`

(com.apple.yellow.eocontrol only) Returns the
target class of the receiver's fault object, which must be passed
as _aFault_ in case the receiver needs
to fire it (EOFaultHandlers don't keep references to their faults).
For example, to support entity inheritance, the Access layer fires
faults for entities with subentities to confirm their precise class
membership.

__See Also:__  [targetClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc65dbojtwk5cdnrqxg4y)

---

### completeInitializationOfObject

`public void completeInitializationOfObject(Object aFault)`

Implemented by subclasses to revert _aFault_ to
its original state and complete its initialization in whatever means
is appropriate to the subclass. For example, the Access layer subclasses
of EOFaultHandler fetch data from the database and pass it to the
object. This method is invoked automatically by a fault when it's
sent a message it can't handle without fetching its data. EOFaultHandler's
implementation merely throws an exception.

---

### createFaultForDeferredFault

`public Object createFaultForDeferredFault(Object fault, Object eo)`

(com.apple.yellow.eocontrol only) Invoked by [willReadRelationship](EODeferredFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirswmzlsojswirtbovwhi2lom4xxo2lmnrjgkylekjswyylunfxw443infya) to ensure that _fault_ isn't
a deferred fault, and to replace it with a normal fault if it is.
EOFaultHandler's implementation simply returns its fault. A private
subclass that handles deferred faulting implements this method to
return a normal fault if _fault_ is
a deferred fault, so you should never need to override this method.

---

### decrementExtraRefCountIsZero

`public boolean decrementExtraRefCountIsZero()`

(com.apple.yellow.eocontrol only) Decrements
the reference count for the receiver's fault. An object's reference
count is the number of objects that are accessing it. Newly created
objects have a reference count of one. If another object is referencing
an object, the object is said to have an extra reference count.

If,
after decrementing the reference count, the fault's new reference
count is zero, this method returns true, If the reference count
has not become zero, this method returns false. Objects that have
a zero reference count are candidates for garbage collection.

This
method is used by EOFaultHandler's internal reference counting
mechanism.

---

### descriptionForObject

`public String descriptionForObject(Object aFault)`

Returns a string naming the original class of
the receiver's fault and giving _aFault_'s address,
and also noting that it's a fault. (The fault must be passed as _aFault_ because
EOFaultHandlers don't keep references to their faults.)

---

### extraRefCount

`public int extraRefCount()`

(com.apple.yellow.eocontrol only) Returns the
receiver's current reference count. This method is used by EOFaultHandler's
internal reference counting mechanism.

---

### faultWillFire

`public void faultWillFire(Object aFault)`

(com.apple.yellow.eocontrol only) Informs the
receiver that _aFault_ is about to
be reverted to its original state. EOFaultHandler's implementation
does nothing.

---

### incrementExtraRefCount

`public void incrementExtraRefCount()`

(com.apple.yellow.eocontrol only) Increments
the reference count for the receiver's fault. An object's reference
count is the number of objects that are accessing it. Newly created
objects have a reference count of one. If another object is referencing
an object, the object is said to have an extra reference count.

This
method is used by EOFaultHandler's internal reference counting
mechanism.

__See Also:__  [extraRefCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6zlyorzgcutfmzbw65looq)

---

### isKindOfClass

`public boolean isKindOfClass(
Class aClass,
Object aFault)`

(com.apple.yellow.eocontrol only) Returns true if
the target class of the receiver's fault is _aClass_ or a
subclass of _aClass._ The fault must
be passed in as _aFault_ in case the
receiver needs to fire it (EOFaultHandlers don't keep references to
their faults). For example, to support entity inheritance, the Access
layer fires faults for entities with subentities to confirm their
precise class membership.

__See Also:__  [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi)

---

### isMemberOfClass

`public boolean isMemberOfClass(
Class aClass,
Object aFault)`

(com.apple.yellow.eocontrol only) Returns true if
the target class of the receiver's fault is _aClass._
This fault must be passed as _aFault_ in
case the receiver needs to fire it (EOFaultHandlers don't keep references to
their faults). For example, to support entity inheritance, the Access
layer fires faults for entities with subentities to confirm their
precise class membership.

__See Also:__  [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi)

---

### respondsToSelectorForFault

`public boolean respondsToSelectorForFault(
NSSelector aSelector,
Object aFault)`

(com.apple.yellow.eocontrol only) Returns true if
the target class of the receiver's fault responds to _aSelector._
This fault must be passed as _aFault_ in
case the receiver needs to fire it (EOFaultHandlers don't store references to
their faults). For example, to support entity inheritance, the Access
layer fires faults for entities with subentities to confirm their
precise class membership.

__See Also:__  [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi)

---

### targetClass

`public Class targetClass()`

(com.apple.yellow.eocontrol only) Returns the
target class of the receiver's fault. The fault may, however,
be converted to a member of this class or of a subclass of this
class. For example, to support entity inheritance, the Access layer
fires faults for entities with subentities into the appropriate
class on fetching their data.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
