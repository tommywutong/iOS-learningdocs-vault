---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOFault.html
archived_at: '2026-07-18T01:28:35.867700Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEditingContext-4.md)
[!](EOFaultHandler-2.md)

---

# EOFault

__Inherits From:__
none _(EOFault is a root class)_

__Declared in:__ EOControl/EOFault.h

EOFault and EOFaultHandler form a general mechanism for substituting placeholder objects that convert themselves into regular objects. An EOFault is most commonly used by the Access Layer to represent an object not yet fetched from the database, but that must nonetheless exist as an instance in the application-typically because it's the destination of a relationship. EOFault is a completely general class; there's no need to create subclasses to customize fault handling. Instead, you create subclasses of EOFaultHandler to accommodate different means of converting faults into regular objects.

The faulting mechanism provides for continuity of an object's __id__ even when that object's state isn't yet available. An EOFault simply holds the place for an ultimate "real" object, handling all methods that it can without causing the state to be loaded. When an EOFault receives a message that it can't handle, it calls upon its EOFaultHandler to __fire__ it, converting it into a "real" object. This often involves accessing the external, persistent state of the object.

---

### Creating an EOFault

Rather than allocating and initializing an EOFault, you turn an existing object into one using EOFault's __makeObjectIntoFault:withHandler:__ class method. When you do so, you must provide an EOFaultHandler that will later help the fault to fire. __makeObjectIntoFault:withHandler:__ preserves the __id__ of the original object, overlaying its __isa__ pointer with that of the EOFault class and slipping the EOFaultHandler among its instance variables. Once this is done, the original object is an EOFault that will fire when accessed.

The EOFaultHandler should be considered completely private property of the EOFault once you've created it. You should neither retain the EOFaultHandler or send it any other messages, instead dealing exclusively with the newly created EOFault or the EOFault class itself.

---

### EOFault Behavior

EOFault implements many basic object methods in a manner that doesn't cause the receiver to fire. The following methods all behave as though normal for the original object:

| - retain | - isMemberOfClass: |
| - release | - conformsToProtocol: |
| - autorelease | - isProxy |
| - retainCount | - methodSignatureForSelector: |
| - class | - respondsToSelector: |
| - superclass | - zone |
| - isKindOfClass: | - doesNotRecognizeSelector: |

```
```

__doesNotRecognizeSelector:__ is a special case here, in that it's only invoked if the selector in question isn't found for the original class. Normally, methods not implemented by EOFault, but implemented by the original class, cause the receiver to fire as described below.

These methods don't cause the receiver to fire, but also don't hide the presence of the EOFault class:

| - description | - descriptionWithLocale: |
| - descriptionWithIndent: | - descriptionWithLocale:indent: |
| - eoDescription | - eoShallowDescription |

```
```

The following common methods, along with any others not explicitly mentioned in this section, do cause the receiving EOFault to fire.

- - dealloc
- - self
- - forwardInvocation:

When an EOFault receives one of these messages, it fires in one of a few different ways. __dealloc__ invokes the - clearFault: class method to revert the receiver back to its original state, then reinvokes __dealloc__ to clean up instance variables and deallocate the object. The other methods all send a special message, [__completeInitializationOfObject:__](EOFaultHandler-2.md), to the EOFaultHandler to transform the EOFault into a regular object, possibly different from its original state. In addition, __forwardInvocation:__ sends a [__shouldPerformInvocation:__](EOFaultHandler-2.md)to the EOFaultHandler first, which allows it to perform the method itself without causing the EOFault to be transformed. If the EOFaultHandler returns YES, though, the EOFault then sends it a [__completeInitializationOfObject:__](EOFaultHandler-2.md)message.

---

### Examining an EOFault

Three additional EOFault methods allow you to explicitly check whether an object is an EOFault without causing it to fire, and to get its original class and EOFaultHandler if it is an EOFault. These methods are:

- + isFault:
- + targetClassForFault:
- + handlerForFault:

You can use these methods to base some decisions on whether an object is an EOFault, though you should rarely need to do so.

**Creating and examining faults**

**+ makeObjectIntoFault:withHandler:

**+ isFault:

**+ clearFault:

**+ handlerForFault:

**+ targetClassForFault:

**+ respondsToSelector:************

**Checking class informatio**

**- class

**- isKindOfClass:

**- isMemberOfClass:

**- respondsToSelector:

**- conformsToProtocol:

**- methodSignatureForSelector:************

**Run-time support**

**- forwardInvocation:

**- doesNotRecognizeSelector:****

**Getting a fault's description**

**- description

**- descriptionWithIndent:

**- descriptionWithLocale:

**- descriptionWithLocale:indent:

**- eoDescription

**- eoShallowDescription************

**Reference-counting**

**- retain

**- release

**- retainCount

**- autorelease

**- dealloc**********

**Miscellaneous object methods**

**- self

**- isProxy

**- superclass

**- zone********

---

#### clearFault:

+ (void)__clearFault:__ (id)_aFault_

Restores _aFault_ to its status prior to the __makeObjectIntoFault:withHandler:__ message that created it. Raises an NSInvalidArgumentException if _aFault_ isn't an EOFault.

You rarely use this method. Faults typically fire automatically when accessed, using EOFaultHandler's [__completeInitializationOfObject:__](EOFaultHandler-2.md)method. See the EOFaultHandler class specification for more information.

---

#### handlerForFault:

+ (EOFaultHandler \*)__handlerForFault:__ (id)_aFault_

Returns the EOFaultHandler that will help _aFault_ to fire. Returns __nil__ if _aFault_ isn't an EOFault.

---

#### isFault:

+ (BOOL)__isFault:__ (id)_anObject_

Returns YES if _anObject_ is an EOFault, NO otherwise.

---

#### makeObjectIntoFault:withHandler:

+ (void)__makeObjectIntoFault:__ (id)_anObject_ __withHandler:__ (EOFaultHandler \*)_aFaultHandler_

Converts _anObject_ into an EOFault, assigning _aFaultHandler_ as the object that stores its original state and later converts the EOFault back into a normal object (typically by fetching data from an external repository). The new EOFault becomes the owner of _aFaultHandler_; you shouldn't assign it to another object.

---

#### respondsToSelector:

+ (BOOL)__respondsToSelector:__ (SEL)_aSelector_

Returns YES if the receiving class responds to _aSelector_, NO otherwise.

---

#### targetClassForFault:

+ (Class)__targetClassForFault:__ (id)_aFault_

Returns the original class of the object that was turned into _aFault_, or __nil__ if _aFault_ isn't an EOFault. When the EOFault fires, it's guaranteed to be an instance of this class or possibly of a subclass. To get the actual class, you must send a __class__ message to the EOFault, which may fire to determine its actual class membership.

---

#### autorelease

- (id)__autorelease__

Performs as NSObject's __autorelease__ method.

---

#### class

- (Class)__class__

Returns the class of the object that the receiving EOFault will become. This may cause the EOFault to fire in order to determine its actual class membership.

__See also:__ [- __classForFault:__](EOFaultHandler-2.md)(EOFaultHandler), + __targetClassForFault:__

---

#### conformsToProtocol:

- (BOOL)__conformsToProtocol:__ (Protocol \*)_aProtocol_

Returns YES if the object that the receiving EOFault will become conforms to _aProtocol_, NO if it doesn't. This may cause the EOFault to fire in order to determine its actual class membership.

__See also:__ [- __conformsToProtocol:forFault:__](EOFaultHandler-2.md)(EOFaultHandler)

---

#### dealloc

- (void)__dealloc__

Invokes the __clearFault:__ class method to revert the receiving EOFault to its original class membership and state, then reinvokes __dealloc__ .

---

#### description

- (NSString \*)__description__

Sends [__descriptionForObject:__](EOFaultHandler-2.md)to the receiver's EOFaultHandler and returns the result.

---

#### descriptionWithIndent:

- (NSString \*)__descriptionWithIndent:__ (unsigned int)_indentLevel_

Invokes __description__ and returns the result.

---

#### descriptionWithLocale:

- (NSString \*)__descriptionWithLocale:__ (NSDictionary \*)_locale_

Invokes __description__ and returns the result.

---

#### descriptionWithLocale:indent:

- (NSString \*)__descriptionWithLocale:__ (NSDictionary \*)_locale_ __indent:__ (unsigned int)_indentLevel_

Invokes __description__ and returns the result.

---

#### doesNotRecognizeSelector:

- (void)__doesNotRecognizeSelector:__ (SEL)_aSelector_

Raises an NSInvalidArgumentException.

---

#### eoDescription

- (NSString \*)__eoDescription__

Invokes __description__ and returns the result.

__See also:__ [- __eoDescription__](NSObject%20Additions.md)(NSObject Additions)

---

#### eoShallowDescription

- (NSString \*)__eoShallowDescription__

Invokes __description__ and returns the result.

__See also:__ [- __eoShallowDescription__](NSObject%20Additions.md)(NSObject Additions)

---

#### forwardInvocation:

- (void)__forwardInvocation:__ (NSInvocation \*)_anInvocation_

Causes the receiving EOFault to fire, if allowed by its EOFaultHandler, and forward _anInvocation_ to its new incarnation. Sends a [__shouldPerformInvocation:__](EOFaultHandler-2.md)to the receiver's EOFaultHandler first, giving it a chance to bypass the conversion. If the EOFaultHandler returns NO, returns immediately. If it returns YES, sends a [__completeInitializationOfObject:__](EOFaultHandler-2.md)message to the EOFaultHandler with __self__ as the argument. Once the receiver has fired it invokes _anInvocation_.

---

#### isKindOfClass:

- (BOOL)__isKindOfClass:__ (Class)_aClass_

Returns YES if _aClass_ is the class, or a superclass, of the object that the receiving EOFault will become, NO otherwise. This may cause the EOFault to fire in order to determine its actual class membership.

__See also:__ - __isMemberOfClass:__ , [- __isKindOfClass:forFault:__](EOFaultHandler-2.md)(EOFaultHandler)

---

#### isMemberOfClass:

- (BOOL)__isMemberOfClass:__ (Class)_aClass_

Returns YES if _aClass_ is the class of the object that the receiving EOFault will become, NO otherwise. This may cause the EOFault to fire in order to determine its actual class membership.

__See also:__ - __isKindOfClass:__ , [- __isMemberOfClass:forFault:__](EOFaultHandler-2.md)(EOFaultHandler)

---

#### isProxy

- (BOOL)__isProxy__

Returns NO.

---

#### methodSignatureForSelector:

- (NSMethodSignature \*)__methodSignatureForSelector:__ (SEL)_aSelector_

Returns a method signature for _aSelector_ for the object that the receiving EOFault will become, or __nil__ if one can't be found. This may cause the EOFault to fire in order to determine its actual class membership.

__See also:__ - __methodSignatureForSelector:__ (EOFaultHandler)

---

#### release

- (void)__release__

Performs as NSObject's __release__ method.

---

#### respondsToSelector:

- (BOOL)__respondsToSelector:__ (SEL)_aSelector_

Returns YES if the object that the receiving EOFault will become responds to _aSelector_, NO otherwise. This may cause the EOFault to fire in order to determine its actual class membership.

__See also:__ [- __respondsToSelector:forFault:__](EOFaultHandler-2.md)(EOFaultHandler)

---

#### retain

- (id)__retain__

Performs as NSObject's __retain__ method.

---

#### retainCount

- (unsigned int)__retainCount__

Performs as NSObject's __retainCount__ method.

---

#### self

- (id)__self__

Fires the receiver and returns __self__ . This is the recommended way to simply fire an EOFault.

---

#### superclass

- (Class)__superclass__

Returns the superclass of the object that the receiving EOFault will become. This may cause the EOFault to fire in order to determine its actual class membership.

__See also:__ [- __classForFault:__](EOFaultHandler-2.md)(EOFaultHandler)

---

#### zone

- (NSZone \*)__zone__

Performs as NSObject's __zone__ method.

---

[!](EOEditingContext-4.md)
[!](EOFaultHandler-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
