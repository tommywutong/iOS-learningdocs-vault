---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOFaultHandler.html
archived_at: '2026-07-18T01:28:25.969193Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOEditingContext-2.md)
[!](EOFetchSpecification.md)

---

# EOFaultHandler

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOFaultHandler is an abstract class that defines the mechanisms that create faults and help them to fire. Faults are used as placeholders for an enterprise object's relationship destinations. For example, suppose an Employee object has a __department__ relationship to the employee's department. When an employee is fetched, faults are created for its relationship destinations. In the case of the __department__ relationship, an empty Department object is created. The Department object's data isn't fetched until the Department is accessed, at which time the fault is said to _fire_.

Subclasses of EOFaultHandler perform the specific steps necessary to get data for the fault and fire it. The Access Layer, for example, uses private subclasses to fetch data using an EODatabaseContext (defined in EOAccess). Most of EOFaultHandler's methods are properly defined; you need only override __completeInitializationOfObject__ to provide appropriate behavior. In Yellow Box applications, you can optionally implement __faultWillFire__ to prepare for conversion.

In a Yellow Box application you create an EOFaultHandler using the standard constructor. To create a fault in a Yellow Box application, you invoke the static method __makeObjectIntoFault__ with the object to turn into a fault and the EOFaultHandler. An EOFaultHandler belongs exclusively to a single fault, and shouldn't be shared or used by any other object.

In a Java Client application you also create an EOFaultHandler using the standard constructor. To create a fault in a Java Client application, though, you send a newly-created object a [__turnIntoFault__](EOFaulting.md)message and provide an EOFaultHandler that will help the fault to fire. In order for that newly-created object to be able to respond to [__turnIntoFault__](EOFaulting.md), the object must conform to the [EOFaulting](EOFaulting.md) interface. An EOFaultHandler belongs exclusively to a single fault, and shouldn't be shared or used by any other object. In Java Client applications, the fault handler is the private property of the fault; you shouldn't send any messages to the fault hander, instead dealing exclusively with the fault.

---

### Firing a Fault

When a fault receives a message that requires it to fire, it sends a __completeInitializationOfObject__ method to its EOFaultHandler. This method is responsible for invoking the __clearFault__ method to revert the fault to its original state, and then do whatever is necessary to complete initialization of the object. Doing so typically involves fetching data from an external repository and passing it to the object.

## Method Types

**Constructors**

**EOFaultHandler**

**Creating and examining faults**

**+ clearFault

**+ isFault

**+ makeObjectIntoFault

**+ handlerForFault********

**Reference counting**

**- incrementExtraRefCount

**- decrementExtraRefCountIsZero

**- extraRefCount******

**Getting the original class**

**- classForFault**

**Firing a fault**

**- completeInitializationOfObject

**- faultWillFire****

**Getting a description**

**- descriptionForObject**

**Checking class information**

**- respondsToSelectorForFault**

## Constructors

---

#### EOFaultHandler

public __EOFaultHandler__ ()

Creates and returns an EOFaultHandler object.

## Static Methods

---

#### clearFault

public static void __clearFault__ (java.lang.Object _aFault_)

This method is only available in Yellow Box; there is no Java Client equivalent. Restores _aFault_ to its status prior to the __makeObjectIntoFault__ message that created it. Throws an exception if _aFault_ isn't a fault.

You rarely use this method. Faults typically fire automatically when accessed, using the __completeInitializationOfObject__ method.

---

#### handlerForFault

public static EOFaultHandler __handlerForFault__ (java.lang.Object _aFault_)

This method is only available in Yellow Box; there is no Java Client equivalent. Returns the EOFaultHandler that will help _aFault_ to fire. Returns __null__ if _aFault_ isn't a fault.

---

#### isFault

public static boolean __isFault__ (java.lang.Object _anObject_)

Returns __true__ if _anObject_ is a fault, __false__ otherwise.

---

#### makeObjectIntoFault

public static void __makeObjectIntoFault__ (java.lang.Object _anObject_, EOFaultHandler _aFaultHandler_)

This method is only available in Yellow Box; there is no Java Client equivalent. Converts _anObject_ into a fault, assigning _aFaultHandler_ as the object that stores its original state and later converts the fault back into a normal object (typically by fetching data from an external repository). The new fault becomes the owner of _aFaultHandler_; you shouldn't assign it to another object.

---

#### targetClassForFault

public static java.lang.Class __targetClassForFault__ (java.lang.Object _anObject_)

This method is only available in Yellow Box; there is no Java Client equivalent. Returns the class that will be instantiated when the fault fires. The returned class could be a superclass of the actual class instantiated.

## Instance Methods

---

#### classForFault

public java.lang.Class __classForFault__ (java.lang.Object _fault_)

This method is only available in Yellow Box; there is no Java Client equivalent. Returns the target class of the receiver's fault object, which must be passed as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't keep references to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ + __targetClassForFault__

---

#### completeInitializationOfObject

public void __completeInitializationOfObject__ (java.lang.Object _aFault_)

Implemented by subclasses to revert _aFault_ to its original state and complete its initialization in whatever means is appropriate to the subclass. For example, the Access layer subclasses of EOFaultHandler fetch data from the database and pass it to the object. This method is invoked automatically by a fault when it's sent a message it can't handle without fetching its data. EOFaultHandler's implementation merely throws an exception.

---

#### decrementExtraRefCountIsZero

public boolean __decrementExtraRefCountIsZero__ ()

This method is only available in Yellow Box; there is no Java Client equivalent. Decrements the reference count for the receiver's fault. An object's reference count is the number of objects that are accessing it. Newly created objects have a reference count of one. If another object is referencing an object, the object is said to have an _extra reference count_.

If, after decrementing the reference count, the fault's new reference count is zero, this method returns __true__ , If the reference count has not become zero, this method returns __false__ . Objects that have a zero reference count are marked for garbage collection.

This method is used by EOFaultHandler's internal reference counting mechanism.

---

#### descriptionForObject

public java.lang.String __descriptionForObject__ (java.lang.Object _aFault_)

This method is only available in Yellow Box; there is no Java Client equivalent. Returns a string naming the original class of the receiver's fault and giving _aFault_'s address, and also noting that it's a fault. (The fault must be passed as _aFault_ because EOFaultHandlers don't keep references to their faults.)

---

#### extraRefCount

public int __extraRefCount__

This method is only available in Yellow Box; there is no Java Client equivalent. Returnsthe receiver's current reference count. This method is used by EOFaultHandler's internal reference counting mechanism.

---

#### faultWillFire

public void __faultWillFire__ (java.lang.Object _aFault_)

This method is only available in Yellow Box; there is no Java Client equivalent. Informs the receiver that _aFault_ is about to be reverted to its original state. EOFaultHandler's implementation does nothing.

---

#### incrementExtraRefCount

public void __incrementExtraRefCount__ ()

This method is only available in Yellow Box; there is no Java Client equivalent. Increments the reference count for the receiver's fault. An object's reference count is the number of objects that are accessing it. Newly created objects have a reference count of one. If another object is referencing an object, the object is said to have an _extra reference count_.

This method is used by EOFaultHandler's internal reference counting mechanism.

__See also:__ - __extraRefCount__

---

#### isKindOfClass

public boolean __isKindOfClass__ (java.lang.Class _aClass_, java.lang.Object _aFault_)

This method is only available in Yellow Box; there is no Java Client equivalent. Returns __true__ if the target class of the receiver's fault is _aClass_ or a subclass of _aClass_. The fault must be passed in as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't keep references to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __completeInitializationOfObject__

---

#### isMemberOfClass

public boolean __isMemberOfClass__ (java.lang.Class _aClass_, java.lang.Object _aFault_)

This method is only available in Yellow Box; there is no Java Client equivalent. Returns __true__ if the target class of the receiver's fault is _aClass_. This fault must be passed as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't keep references to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __completeInitializationOfObject__

---

#### respondsToSelectorForFault

public boolean __respondsToSelectorForFault__ (NSSelector _aSelector_, java.lang.Object _aFault_)

This method is only available in Yellow Box; there is no Java Client equivalent. Returns __true__ if the target class of the receiver's fault responds to _aSelector_. This fault must be passed as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't store references to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __completeInitializationOfObject__

---

#### targetClass

public java.lang.Class __targetClass__ ()

This method is only available in Yellow Box; there is no Java Client equivalent. Returns the target class of the receiver's fault . The fault may, however, be converted to a member of this class or of a subclass of this class. For example, to support entity inheritance, the Access layer fires faults for entities with subentities into the appropriate class on fetching their data.

---

[!](EOEditingContext-2.md)
[!](EOFetchSpecification.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
