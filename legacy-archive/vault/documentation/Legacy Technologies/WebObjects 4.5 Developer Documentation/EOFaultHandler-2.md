---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOFaultHandler.html
archived_at: '2026-07-15T08:11:39.760938Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOFaultHandler

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSObject
> : (NSObject)

> __Declared in:__ : EOControl/EOFault.h

---

## Class Description

---

EOFaultHandler is an abstract class that defines the mechanisms
that create faults (EOFault objects) and help them to fire. _Faults_ are
used as placeholders for an enterprise object's relationship destinations.
For example, suppose an Employee object has a __department__ relationship
to the employee's department. When an employee is fetched, faults
are created for its relationship destinations. In the case of the __department__ relationship,
an empty Department object is created. The Department object's
data isn't fetched until the Department is accessed, at which
time the fault is said to _fire_.

Subclasses of EOFaultHandler perform the specific steps necessary
to get data for the fault and fire it. The Access Layer, for example,
uses private subclasses to fetch data using an EODatabaseContext (defined
in EOAccess). Most of EOFaultHandler's methods are properly defined;
you need only override [completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du) to
provide appropriate behavior. In Yellow Box applications, you can
optionally implement [faultWillFire:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwmylvnr2fo2lmnrdgs4tfhi) to
prepare for conversion, and [shouldPerformInvocation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixxg2dpovwgiudfojtg64tnjfxhm33dmf2gs33ohi) to
intercept particular messages sent to the fault without causing
it to fire.

In a Yellow Box application you create an EOFaultHandler using
the standard __alloc and init methods, possibly using
a more specific init method with your subclass__. To
create a fault you invoke EOFault's [makeObjectIntoFault:withHandler:](EOFault.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c63lbnnsu6ytkmvrxisloorxumylvnr2du53jorueqylomrwgk4r2) class
method with the object to turn into a fault and the EOFaultHandler.
An EOFaultHandler belongs exclusively to a single fault, and shouldn't
be shared or used by any other object.

## Firing a Fault

When a fault receives a message that requires it to fire,
it sends a [completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du) method
to its EOFaultHandler. This method is responsible for invoking EOFault's [clearFault:](EOFault.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c6y3mmvqxertbovwhioq)class method to revert
the fault to its original state, and then do whatever is necessary
to complete initialization of the object. Doing so typically involves
fetching data from an external repository and passing it to the
object.

As a trivial example, consider a subclass called FileFaultHandler,
that simply stores a filename whose contents it reads from disk.
Its initialization and [completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du) methods
might look like these:

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

__initWithFile:__ just stores the path
of the file to read in the instance variable __filename__. [completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du) invokes
EOFault's __clearFault:__ method, which reverts
the fault into its original state (and also releases the fault handler,
so references to __self__ after this are illegal).
It then gets the contents of the file it was created with and passes
them to the reverted object. Note that this implementation doesn't
assume the class of the cleared EOFault, instead using the generic __takeValue:forKey:__ method
to assign the file contents to it.

## Method Types

---

> **Creating and examining
> faults**
> : [- createFaultForDeferredFault:sourceObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg4tfmf2gkrtbovwhirtpojcgkztfojzgkzcgmf2wy5b2onxxk4tdmvhwe2tfmn2du)
>
> **Setting the target class
> and extra data**
> : [- setTargetClass:extraData:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixxgzlukrqxez3forbwyyltom5gk6duojquiylume5a)
> : [- targetClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixxiylsm5sxiq3mmfzxg)
> : [- extraData](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwk6duojquiylume)
>
> **Reference counting**
> : [- incrementExtraRefCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixws3tdojsw2zloorcxq5dsmfjgkzsdn52w45a)
> : [- decrementExtraRefCountIsZero](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwizldojsw2zloorcxq5dsmfjgkzsdn52w45cjonngk4tp)
> : [- extraRefCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwk6duojqvezlginxxk3tu)
>
> **Getting the original
> class**
> : [- classForFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg3dbonzum33sizqxk3duhi)
>
> **Firing a fault**
> : [- completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du)
> : [- faultWillFire:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwmylvnr2fo2lmnrdgs4tfhi)
> : [- shouldPerformInvocation:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixxg2dpovwgiudfojtg64tnjfxhm33dmf2gs33ohi)
>
> **Getting a description**
> : [- descriptionForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwizltmnzgs4dunfxw4rtpojhwe2tfmn2du)
>
> **Checking class information**
> : [- isKindOfClass:forFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixws42lnfxgit3ginwgc43thjtg64sgmf2wy5b2)
> : [- isMemberOfClass:forFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixws42nmvwwezlsj5teg3dbonztuztpojdgc5lmoq5a)
> : [- conformsToProtocol:forFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33omzxxe3ltkrxva4tporxwg33mhjtg64sgmf2wy5b2)
> : [- methodSignatureForSelector:forFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixw2zlunbxwiu3jm5xgc5dvojsum33sknswyzldorxxeotgn5zemylvnr2du)
> : [- respondsToSelector:forFault:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixxezltobxw4zdtkrxvgzlmmvrxi33shjtg64sgmf2wy5b2)

## Instance Methods

---

### classForFault:

`- (Class)classForFault:(id)fault`

Returns the target class of the receiver's EOFault,
which must be passed as _aFault_ in
case the receiver needs to fire it (EOFaultHandlers don't store
back pointers to their faults). For example, to support entity inheritance,
the Access layer fires faults for entities with subentities to confirm
their precise class membership.

__See Also:__  [- targetClass](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixxiylsm5sxiq3mmfzxg)

---

### completeInitializationOfObject:

`- (void)completeInitializationOfObject:(id)aFault`

Implemented by subclasses to revert _aFault_ to
its original state and complete its initialization in whatever means
is appropriate to the subclass. For example, the Access layer subclasses
of EOFaultHandler fetch data from the database and pass it to the
object. This method is invoked automatically by a fault when it's
sent a message it can't handle without fetching its data. EOFaultHandler's
implementation merely throws an exception.

---

### conformsToProtocol:forFault:

`- (BOOL)conformsToProtocol:(Protocol
*)aProtocol
forFault:(id)aFault`

Returns YES if the target class of the receiver's
EOFault conforms to _aProtocol_. This
EOFault must be passed as _aFault_ in
case the receiver needs to fire it (EOFaultHandlers don't store
back pointers to their faults). For example, to support entity inheritance,
the Access layer fires faults for entities with subentities to confirm
their precise class membership.

__See Also:__  [- completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du)

---

### createFaultForDeferredFault:sourceObject:

`- (id)createFaultForDeferredFault:(id)fault
sourceObject:(id)eo`

Invoked by [willReadRelationship](EODeferredFaulting-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpirswmzlsojswirtbovwhi2lom4xxo2lmnrjgkylekjswyylunfxw443infya) to ensure that _fault_ isn't
a deferred fault, and to replace it with a normal fault if it is.
EOFaultHandler's implementation simply returns its fault. A private
subclass that handles deferred faulting implements this method to
return a normal fault if _fault_ is
a deferred fault, so you should never need to override this method.

---

### decrementExtraRefCountIsZero

`- (BOOL)decrementExtraRefCountIsZero`

Decrements the reference count for the receiver's
fault. An object's reference count is the number of objects that
are accessing it. Newly created objects have a reference count of
one. If another object is referencing an object, the object is said
to have an extra reference count.

If, after decrementing the
reference count, the fault's new reference count is zero, this
method returns YES, If the reference count has not become zero,
this method returns NO. Objects that have a zero reference count
are released at the end of the current event loop.

This
method is used by EOFaultHandler's internal reference counting
mechanism-it functions as the Foundation function `NSDecrementExtraRefCountWasZero()` for
the receiver's EOFault.

---

### descriptionForObject:

`- (NSString *)descriptionForObject:(id)aFault`

Returns a string naming the original class of
the receiver's fault and giving _aFault_'s id,
and also noting that it's a fault; for example: "<Employee
(Fault 0x3a07)>". (The fault must be passed as _aFault_ because EOFaultHandlers
don't store back pointers to their faults.)

---

### extraData

`- (void *)extraData`

Returns the bytes replaced by the receiver's __id__ in
the original object's state, as a pointer to __void__.
When the receiver's EOFault is reverted to its original state,
both its __isa__ pointer and this data are
replaced.

---

### extraRefCount

`- (unsigned int)extraRefCount`

Returns the receiver's current reference count.
This method is used by EOFaultHandler's internal reference counting
mechanism and functions as the Foundation function NSExtraRefCount()
for the receiver's EOFault.

---

### faultWillFire:

`- (void)faultWillFire:(id)aFault`

Informs the receiver that _aFault_ is
about to be reverted to its original state. EOFaultHandler's implementation
does nothing. This method is invoked by EOFault's [clearFault:](EOFault.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c6y3mmvqxertbovwhioq) method.

---

### incrementExtraRefCount

`- (void)incrementExtraRefCount`

Increments the reference count for the receiver's
fault. An object's reference count is the number of objects that
are accessing it. Newly created objects have a reference count of
one. If another object is referencing an object, the object is said
to have an extra reference count.

This method is used by EOFaultHandler's
internal reference counting mechanism and functions as the Foundation
function NSIncrementExtraRefCount() for the receiver's EOFault.

__See
Also:__  [- extraRefCount](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwk6duojqvezlginxxk3tu)

---

### isKindOfClass:forFault:

`- (BOOL)isKindOfClass:(Class)aClass
forFault:(id)aFault`

Returns YES if the target class of the receiver's
fault is _aClass_ or a subclass of _aClass_.
The fault must be passed in as _aFault_ in
case the receiver needs to fire it (EOFaultHandlers don't store
back pointers to their faults). For example, to support entity inheritance,
the Access layer fires faults for entities with subentities to confirm
their precise class membership.

__See Also:__  [- completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du)

---

### isMemberOfClass:forFault:

`- (BOOL)isMemberOfClass:(Class)aClass
forFault:(id)aFault`

Returns YES if the target class of the receiver's
fault is _aClass_. This fault must
be passed as _aFault_ in case the receiver
needs to fire it (EOFaultHandlers don't store back pointers to
their faults). For example, to support entity inheritance, the Access
layer fires faults for entities with subentities to confirm their precise
class membership.

__See Also:__  [- completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du)

---

### methodSignatureForSelector:forFault:

`- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
forFault:(id)aFault`

Returns the NSMethodSignature for _aSelector_ in
the target class of the receiver's EOFault, which must be passed
as _aFault_ in case the receiver needs
to fire it (EOFaultHandlers don't store back pointers to their
faults). For example, to support entity inheritance, the Access
layer fires faults for entities with subentities to confirm their
precise class membership.

__See Also:__  [- completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du)

---

### respondsToSelector:forFault:

`- (BOOL)respondsToSelector:(SEL)aSelector
forFault:(id)aFault`

Returns YES if the target class of the receiver's
fault responds to _aSelector_. This
fault must be passed as _aFault_ in
case the receiver needs to fire it (EOFaultHandlers don't store back
pointers to their faults). For example, to support entity inheritance,
the Access layer fires faults for entities with subentities to confirm
their precise class membership.

__See Also:__  [- completeInitializationOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2gmf2wy5cimfxgi3dfoixwg33nobwgk5dfjfxgs5djmfwgs6tboruw63spmzhwe2tfmn2du)

---

### setTargetClass:extraData:

`- (void)setTargetClass:(Class)targetClass
extraData:(void *)extraData`

Stores _targetClass_ and _extraData_ as
state of the original object overwritten when an EOFault is created by
EOFault's [makeObjectIntoFault:withHandler:](EOFault.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhumylvnr2c63lbnnsu6ytkmvrxisloorxumylvnr2du53jorueqylomrwgk4r2) method,
which replaces _targetClass_ with the
EOFault class, and _extraData_ with
the EOFaultHandler's `id`.

---

### shouldPerformInvocation:

`- (BOOL)shouldPerformInvocation:(NSInvocation
*)anInvocation`

Overridden by subclasses to circumvent reversion
of an EOFault to its original state. Returns YES if the EOFault
should revert and perform _anInvocation_,
NO if it shouldn't. If this method returns NO, the receiver should
set _anInvocation_'s return value
appropriately. EOFaultHandler's implementation returns YES.

__See
Also:__  __- setReturnValue:__ (NSInvocation
class of the Foundation Framework)

---

### targetClass

`- (Class)targetClass`

Returns the target class of the receiver's
fault. The fault may, however, be converted to a member of this class
or of a subclass of this class. For example, to support entity inheritance,
the Access layer fires faults for entities with subentities into
the appropriate class on fetching their data.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
