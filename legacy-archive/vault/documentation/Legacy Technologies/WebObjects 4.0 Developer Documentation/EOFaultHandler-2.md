---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOFaultHandler.html
archived_at: '2026-07-18T01:28:35.993018Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOFault.md)
[!](EOFetchSpecification-2.md)

---

# EOFaultHandler

__Inherits From:__
NSObject

__Conforms To:__ NSObject (NSObject)

__Declared in:__ EOControl/EOFault.h

EOFaultHandler is an abstract class that defines the mechanisms that create EOFaults (or faults) and help them to fire. Faults are used as placeholders for an enterprise object's relationship destinations. For example, suppose an Employee object has a __department__ relationship to the employee's department. When an employee is fetched, faults are created for its relationship destinations. In the case of the __department__ relationship, an empty Department object is created. The Department object's data isn't fetched until the Department is accessed, at which time the fault is said to _fire_.

Subclasses of EOFaultHandler perform the specific steps necessary to get data for the fault and fire it. The Access Layer, for example, uses private subclasses to fetch data using an EODatabaseContext (defined in EOAccess). Most of EOFaultHandler's methods are properly defined; you need only override __completeInitializationOfObject:__ to provide appropriate behavior. In Yellow Box applications, you can optionally implement __faultWillFire:__ to prepare for conversion, and __shouldPerformInvocation:__ to intercept particular messages sent to the fault without causing it to fire.

In a Yellow Box application you create an EOFaultHandler using the standard __alloc__ and __init__ methods, possibly using a more specific __init__ method with your subclass. To create a fault you invoke EOFault's [__makeObjectIntoFault:withHandler:__](EOFault.md)class method with the object to turn into a fault and the EOFaultHandler. An EOFaultHandler belongs exclusively to a single fault, and shouldn't be shared or used by any other object.

---

### Firing a Fault

When a fault receives a message that requires it to fire, it sends a __completeInitializationOfObject:__ method to its EOFaultHandler. This method is responsible for invoking EOFault's [__clearFault:__](EOFault.md)class method to revert the fault to its original state, and then do whatever is necessary to complete initialization of the object. Doing so typically involves fetching data from an external repository and passing it to the object.

As a trivial example, consider a subclass called FileFaultHandler, that simply stores a filename whose contents it reads from disk. Its initialization and __completeInitializationOfObject:__ methods might look like these:

> ```
> - (id)initWithFile:(NSString *)path
> {
>     self = [super init];
>     filename = [path copy];
>     return self;
> }
>
> - (void)completeInitializationOfObject:(id)anObject
> {
>     NSString *fileContents;
>
>     [self retain];      // retain self so we won't get released by clearing the
>                         // fault. Otherwise, accessing "filename" will cause a crash.
>
>     [EOFault clearFault:anObject];
>
>     fileContents = [NSString stringWithContentsOfFile:filename];
>     [anObject takeValue:fileContents forKey:@"fileContents"];
>     [self release];
>     return;
> }
> ```

__initWithFile:__ just stores the path of the file to read in the instance variable __filename__ . __completeInitializationOfObject:__ invokes EOFault's [__clearFault:__](EOFault.md)method, which reverts the fault into its original state (and also releases the fault handler, so references to __self__ after this are illegal). It then gets the contents of the file it was created with and passes them to the reverted object. Note that this implementation doesn't assume the class of the cleared EOFault, instead using the generic __takeValue:forKey:__ method to assign the file contents to it.

**Setting the target class and extra data**

**- setTargetClass:extraData:

**- targetClass

**- extraData******

**Reference counting**

**- incrementExtraRefCount

**- decrementExtraRefCountIsZero

**- extraRefCount******

**Getting the original class**

**- classForFault:**

**Firing a fault**

**- completeInitializationOfObject:

**- faultWillFire:

**- shouldPerformInvocation:******

**Getting a description**

**- descriptionForObject:**

**Checking class information**

**- isKindOfClass:forFault:

**- isMemberOfClass:forFault:

**- conformsToProtocol:forFault:

**- methodSignatureForSelector:forFault:

**- respondsToSelector:forFault:**********

---

#### classForFault:

- (Class)__classForFault:__ (id)_fault_

Returns the target class of the receiver's EOFault, which must be passed as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't store back pointers to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __targetClass__

---

#### completeInitializationOfObject:

- (void)__completeInitializationOfObject:__ (id)_aFault_

Implemented by subclasses to revert _aFault_ to its original state and complete its initialization in whatever means is appropriate to the subclass. For example, the Access layer subclasses of EOFaultHandler fetch data from the database and pass it to the object. This method is invoked automatically by an EOFaultwhen it's sent a message it can't handle without fetching its data. EOFaultHandler's implementation merely throws an exception.

---

#### conformsToProtocol:forFault:

- (BOOL)__conformsToProtocol:__ (Protocol \*)_aProtocol_ __forFault:__ (id)_aFault_

Returns YES if the target class of the receiver's EOFault conforms to _aProtocol_. This EOFault must be passed as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't store back pointers to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __completeInitializationOfObject:__

---

#### decrementExtraRefCountIsZero

- (BOOL)__decrementExtraRefCountIsZero__

Decrements the reference count for the receiver's EOFault. An object's reference count is the number of objects that are accessing it. Newly created objects have a reference count of one. If another object is referencing an object, the object is said to have an _extra reference count_.

If, after decrementing the reference count, the fault's new reference count is zero, this method returns YES, If the reference count has not become zero, this method returns NO. Objects that have a zero reference count are released at the end of the current event loop.

This method is used by EOFaultHandler's internal reference counting mechanism-it functions as the Foundation function __NSDecrementExtraRefCountWasZero()__ for the receiver's EOFault.

---

#### descriptionForObject:

- (NSString \*)__descriptionForObject:__ (id)_aFault_

Returns a string naming the original class of the receiver's EOFault and giving _aFault_'s __id__ , and also noting that it's a fault; for example: "<Employee(Fault 0x3a07)>". (The fault must be passed as _aFault_ because EOFaultHandlers don't store back pointers to their faults.)

---

#### extraData

- (void \*)__extraData__

Returns the bytes replaced by the receiver's __id__ in the original object's state, as a pointer to __void__ . When the receiver's EOFault is reverted to its original state, both its __isa__ pointer and this data are replaced.

---

#### extraRefCount

- (unsigned int)__extraRefCount__

Returnsthe receiver's current reference count. This method is used by EOFaultHandler's internal reference counting mechanism and functions as the Foundation function __NSExtraRefCount()__ for the receiver's EOFault.

---

#### faultWillFire:

- (void)__faultWillFire:__ (id)_aFault_

Informs the receiver that _aFault_ is about to be reverted to its original state. EOFaultHandler's implementation does nothing. This method is invoked by EOFault's [__clearFault:__](EOFault.md)method.

---

#### incrementExtraRefCount

- (void)__incrementExtraRefCount__

Increments the reference count for the receiver's EOFault. An object's reference count is the number of objects that are accessing it. Newly created objects have a reference count of one. If another object is referencing an object, the object is said to have an _extra reference count_.

This method is used by EOFaultHandler's internal reference counting mechanism and functions as the Foundation function __NSIncrementExtraRefCount()__ for the receiver's EOFault.

__See also:__ - __extraRefCount__

---

#### isKindOfClass:forFault:

- (BOOL)__isKindOfClass:__ (Class)_aClass_ __forFault:__ (id)_aFault_

Returns YES if the target class of the receiver's EOFault is _aClass_ or a subclass of _aClass_. The fault must be passed in as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't store back pointers to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __completeInitializationOfObject:__

---

#### isMemberOfClass:forFault:

- (BOOL)__isMemberOfClass:__ (Class)_aClass_ __forFault:__ (id)_aFault_

Returns YES if the target class of the receiver's EOFault is _aClass_. This fault must be passed as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't store back pointers to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __completeInitializationOfObject:__

---

#### methodSignatureForSelector:forFault:

- (NSMethodSignature \*)__methodSignatureForSelector:__ (SEL)_aSelector_ __forFault:__ (id)_aFault_

Returns the NSMethodSignature for _aSelector_ in the target class of the receiver's EOFault, which must be passed as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't store back pointers to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __completeInitializationOfObject:__

---

#### respondsToSelector:forFault:

- (BOOL)__respondsToSelector:__ (SEL)_aSelector_ __forFault:__ (id)_aFault_

Returns YES if the target class of the receiver's EOFault responds to _aSelector_. This fault must be passed as _aFault_ in case the receiver needs to fire it (EOFaultHandlers don't store back pointers to their faults). For example, to support entity inheritance, the Access layer fires faults for entities with subentities to confirm their precise class membership.

__See also:__ - __completeInitializationOfObject:__

---

#### setTargetClass:extraData:

- (void)__setTargetClass:__ (Class)_targetClass_ __extraData:__ (void \*)_extraData_

Stores _targetClass_ and _extraData_ as state of the original object overwritten when an EOFault is created by EOFault's __makeObjectIntoFault:withHandler:__ <<should be XRef>> method, which replaces _targetClass_ with the EOFault class, and _extraData_ with the EOFaultHandler's __id__ .

---

#### shouldPerformInvocation:

- (BOOL)__shouldPerformInvocation:__ (NSInvocation \*)_anInvocation_

Overridden by subclasses to circumvent reversion of an EOFault to its original state. Returns YES if the EOFault should revert and perform _anInvocation_, NO if it shouldn't. If this method returns NO, the receiver should set _anInvocation_'s return value appropriately. EOFaultHandler's implementation returns YES.

__See also:__ - __setReturnValue:__ (NSInvocation class of the Foundation Framework)

---

#### targetClass

- (Class)__targetClass__

Returns the target class of the receiver's EOFault . The EOFault may, however, be converted to a member of this class or of a subclass of this class. For example, to support entity inheritance, the Access layer fires EOFaults for entities with subentities into the appropriate class on fetching their data.

---

[!](EOFault.md)
[!](EOFetchSpecification-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
