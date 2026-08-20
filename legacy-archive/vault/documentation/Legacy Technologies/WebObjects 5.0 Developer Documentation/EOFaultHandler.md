---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOFaultHandler.html
archived_at: '2026-07-15T08:13:46.862450Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOFaultHandler

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOFaultHandler is an abstract class that defines the mechanisms that create faults and help them to fire. __Faults__ are used as placeholders for an enterprise object's relationship destinations. For example, suppose an Employee object has a __department__ relationship to the employee's department. When an employee is fetched, faults are created for its relationship destinations. In the case of the __department__ relationship, an empty Department object is created. The Department object's data isn't fetched until the Department is accessed, at which time the fault is said to __fire__.

Subclasses of EOFaultHandler perform the specific steps necessary to get data for the fault and fire it. The Access Layer, for example, uses private subclasses to fetch data using an EODatabaseContext (defined in EOAccess). Most of EOFaultHandler's methods are properly defined; you need only override [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi) to provide appropriate behavior.

You create an EOFaultHandler using the standard constructor. To create a fault in an application, you invoke the static method [makeObjectIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5wwc23fj5rguzldorew45dpizqxk3du) with the object to turn into a fault and the EOFaultHandler. An EOFaultHandler belongs exclusively to a single fault, and shouldn't be shared or used by any other object.

In a Java Client application you also create an EOFaultHandler using the standard constructor. To create a fault in a Java Client application, though, you send a newly-created object a turnIntoFault message and provide an EOFaultHandler that will help the fault to fire. In order for that newly-created object to be able to respond to __turnIntoFault__, the object must conform to the EOFaulting interface. An EOFaultHandler belongs exclusively to a single fault, and shouldn't be shared or used by any other object. In Java Client applications, the fault handler is the private property of the fault; you shouldn't send any messages to the fault handler, instead dealing exclusively with the fault.

## Firing a Fault

When a fault receives a message that requires it to fire, it sends a [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi) method to its EOFaultHandler. This method is responsible for invoking the [clearFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5rwyzlbojdgc5lmoq) method to revert the fault to its original state, and then do whatever is necessary to complete initialization of the object. Doing so typically involves fetching data from an external repository and passing it to the object.

## Method Types

---

> **Creating and examining faults**
> : [createFaultForDeferredFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3smvqxizkgmf2wy5cgn5zeizlgmvzhezleizqxk3du): [clearFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5rwyzlbojdgc5lmoq): [isFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5uxgrtbovwhi): [makeObjectIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5wwc23fj5rguzldorew45dpizqxk3du): [handlerForFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5ugc3tenrsxertpojdgc5lmoq)
>
> **Firing a fault**
> : [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi): [faultWillFire](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6ztbovwhiv3jnrwem2lsmu)
>
> **Getting a description**
> : [descriptionForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6zdfonrxe2lqoruw63sgn5ze6ytkmvrxi): [eoShallowDescription](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5sw6u3imfwgy33xirsxgy3snfyhi2lpny)

## Constructors

---

### EOFaultHandler

`public EOFaultHandler()`

Description forthcoming.

---

## Static Methods

---

### eoShallowDescription

`public static String eoShallowDescription(Object anObject)`

See the method description for EOEnterpriseObject's eoShallowDescription.

---

### clearFault

`public static void clearFault(Object aFault)`

Restores _aFault_ to its status prior to the [makeObjectIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5wwc23fj5rguzldorew45dpizqxk3du) message that created it. Throws an exception if _aFault_ isn't a fault.

You rarely use this method. Faults typically fire automatically when accessed, using the [completeInitializationOfObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3pnvygyzlumvew42lunfqwy2l2mf2gs33oj5te6ytkmvrxi) method.

---

### handlerForFault

`public static EOFaultHandler handlerForFault(Object aFault)`

Returns the EOFaultHandler that will help _aFault_ to fire. Returns __null__ if _aFault_ isn't a fault.

---

### isFault

`public static boolean isFault(Object anObject)`

Returns __true__ if _anObject_ is a fault, __false__ otherwise.

---

### makeObjectIntoFault

`public static void makeObjectIntoFault( Object anObject, EOFaultHandler aFaultHandler)`

Converts _anObject_ into a fault, assigning _aFaultHandler_ as the object that stores its original state and later converts the fault back into a normal object (typically by fetching data from an external repository). The new fault becomes the owner of _aFaultHandler_; you shouldn't assign it to another object.

---

## Instance Methods

---

### completeInitializationOfObject

`public abstract void completeInitializationOfObject(Object aFault)`

Implemented by subclasses to revert _aFault_ to its original state and complete its initialization in whatever means is appropriate to the subclass. For example, the Access layer subclasses of EOFaultHandler fetch data from the database and pass it to the object. This method is invoked automatically by a fault when it's sent a message it can't handle without fetching its data. EOFaultHandler's implementation merely throws an exception.

---

### createFaultForDeferredFault

`public Object createFaultForDeferredFault( Object fault, EOEnterpriseObject eo)`

Invoked by willReadRelationship to ensure that _fault_ isn't a deferred fault, and to replace it with a normal fault if it is. EOFaultHandler's implementation simply returns its fault. A private subclass that handles deferred faulting implements this method to return a normal fault if _fault_ is a deferred fault, so you should never need to override this method.

---

### descriptionForObject

`public String descriptionForObject(Object aFault)`

Returns a string naming the original class of the receiver's fault and giving _aFault_'s address, and also noting that it's a fault. (The fault must be passed as _aFault_ because EOFaultHandlers don't keep references to their faults.)

---

### faultWillFire

`public abstract void faultWillFire(Object aFault)`

Informs the receiver that _aFault_ is about to be reverted to its original state. EOFaultHandler's implementation does nothing.

---

### targetClass

`public Class targetClass()`

Returns the target class of the receiver's fault. The fault may, however, be converted to a member of this class or of a subclass of this class. For example, to support entity inheritance, the Access layer fires faults for entities with subentities into the appropriate class on fetching their data.

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
