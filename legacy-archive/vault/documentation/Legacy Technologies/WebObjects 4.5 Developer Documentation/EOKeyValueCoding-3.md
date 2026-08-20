---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html
archived_at: '2026-07-15T08:11:43.477226Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOKeyValueCoding

> __(informal protocol)__

> __Declared in:__ : EOControl/EOKeyValueCoding.h

---

## Protocol Description

---

The EOKeyValueCoding informal protocol defines Enterprise
Objects Framework's main data transport mechanism, in which the
properties of an object are accessed indirectly by name (or _key_), rather
than directly through invocation of an accessor method or as instance
variables. Thus, all of an object's properties can be accessed
in a consistent manner. the Framework additions to NSObject provide
default implementations of EOKeyValueCoding, which are sufficient
for most purposes.

The basic methods for accessing an object's values are [takeValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi),
which sets the value for the property identified by the specified
key, and [valueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi),
which returns the value for the property identified by the specified
key. The default implementations provided by NSObject use the accessor methods
normally implemented by objects (or to access instance variables
directly if need be), so that you don't have to write special
code simply to integrate your objects into the Enterprise Objects Framework.

The corresponding methods [takeStoredValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a) and [storedValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3torxxezlekzqwy5lfizxxes3fpe5a) are
similar, but they're considered to be a private API, for use by
the Framework for transporting data to and from _trusted_ sources.
For example, __takeStoredValue:forKey:__ is
used to initialize an object's properties with values fetched
from the database, whereas __takeValue:forKey:__ is
used to modify an object's properties to values provided by a
user or other business logic. How these methods work and how they're
used by the framework is discussed in more detail in the section ["Stored Value Methods"](EOKeyValueCoding-4.md#apple-ijauiq2difeec).

Both the basic and stored value key-value coding methods cache
attribute bindings for both accessor methods and instance variables,
making lookups efficient. The method [flushAllKeyBindings](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/flushAllKeyBindings) is provided
to clear these bindings-as you should when you add or modify a
class in the run-time system.

The the methods [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/accessInstanceVariablesDirectly) and [useStoredAccessor](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/useStoredAccessor) are
used by enterprise object classes to modify the behavior of the
default implementations of key-value coding methods. The remaining
methods, [handleQueryWithUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6j2), [handleTakeValue:forUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq),
and [unableToSetNullForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3vnzqwe3dfkrxvgzlujz2wy3cgn5zewzlzhi),
are provided to handle error conditions. The default versions of [handleQueryWithUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6j2) and [handleTakeValue:forUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq) raise EOUnknownKeyException, with
the target object (EOTargetObjectUserInfoKey) and key (EOUnknownUserInfoKey)
in the user info.

For more information on EOKeyValueCoding, see the sections:

- ["Stored Value Methods"](EOKeyValueCoding-4.md#apple-ijauiq2difeec)
- ["Type Checking and Type Conversion"](EOKeyValueCoding-4.md#apple-ijauiq2kjjeuq)

## Constants

---

In EOKeyValueCoding.h, EOControl defines
an enumeration with two constants to be used as possible arguments
for the [createKeyValueBindingForKey](EOKeyValueCoding.KeyBindingCreation-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzojnsxsqtjnzsgs3thinzgkylunfxw4l3dojswc5dfjnsxsvtbnr2wkqtjnzsgs3thizxxes3fpe) and [keyValueBindingForKey](EOKeyValueCoding.KeyBindingCreation-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzojnsxsqtjnzsgs3thinzgkylunfxw4l3lmv4vmylmovsue2lomruw4z2gn5zewzlz) methods. The
argument indicates whether the return value, a [EOKeyBinding](EOKeyBinding.md#apple-ineegqshjfeui) object, binds a class/key
pair to a mechanism to set the value for a key or to retrieve it.

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| EOSetKeyBindingMask | Designates a binding as one responsible for setting an object's value. |
| EOStoredKeyBindingMask | Designates a binding as one responsible for retrieving an object's value. |

## Method Types

---

> **Accessing values**
> : [- storedValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3torxxezlekzqwy5lfizxxes3fpe5a)
> : [- takeStoredValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a)
> : [- takeValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi)
> : [- valueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi)
>
> **Changing default behavior**
> : [+ accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/accessInstanceVariablesDirectly)
> : [+ useStoredAccessor](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/useStoredAccessor)
>
> **Flushing key bindings**
> : [+ flushAllKeyBindings](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/flushAllKeyBindings)
>
> **Handling error conditions**
> : [- handleQueryWithUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6j2)
> : [- handleTakeValue:forUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq)
> : [- unableToSetNullForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3vnzqwe3dfkrxvgzlujz2wy3cgn5zewzlzhi)

## Class Methods

---

### accessInstanceVariablesDirectly

`+ (BOOL)accessInstanceVariablesDirectly`

Returns YES if the key-value coding methods
should access the corresponding instance variable directly on finding
no accessor method for a property. Returns NO if they shouldn't.
NSObject's implementation of this method returns YES. Subclasses
can override it to return NO, in which case the key-value coding
methods won't access instance variables.

---

### flushAllKeyBindings

`+ (void)flushAllKeyBindings`

Invalidates the cached key binding information
for all classes (caches are kept of key-to-method or instance variable
bindings in order to make key-value coding efficient). This method
should be invoked whenever a class is modified in or removed from
the run-time system.

---

### useStoredAccessor

`+ (BOOL)useStoredAccessor`

Returns YES if the stored value methods ( [storedValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3torxxezlekzqwy5lfizxxes3fpe5a) and [takeStoredValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a))
should use private accessor methods in preference to public accessors.
Returning NO causes the stored value methods to use the same accessor
method-instance variable search order as the corresponding basic key-value
coding methods ( [valueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi) and [takeValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi)).
NSObject's implementation of this method returns YES.

---

## Instance Methods

---

### handleQueryWithUnboundKey:

`- (id)handleQueryWithUnboundKey:(NSString
*)key`

Invoked from [valueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi) when it finds no property
binding for _key_. NSObject's implementation raises an EOUnknownKeyException,
with the target object (EOTargetObjectUserInfoKey) and key (EOUnknownUserInfoKey)
in the user info. Subclasses can override this method to handle
the query in some other way.

---

### handleTakeValue:forUnboundKey:

`- (void)handleTakeValue:(id)value
forUnboundKey:(NSString *)key`

Invoked from [takeValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi) when it finds no
property binding for _key_. NSObject's
implementation raises an EOUnknownKeyException, with the target
object (EOTargetObjectUserInfoKey) and key (EOUnknownUserInfoKey)
in the user info. Subclasses can override it to handle the request
in some other way.

---

### storedValueForKey:

`- (id)storedValueForKey:(NSString
*)key`

Returns the property identified by _key_.
This method is used when the value is retrieved for storage in an
object store (generally, this is ultimately in a database) or for
inclusion in a snapshot. The default implementation provided by the
Framework additions to NSObject is similar to the implementation
of [valueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi), but
it resolves _key_ with a different
method-instance variable search order:

1. Searches for a private accessor method based
   on _key_ (a method preceded by an underbar).
   For example, with a key of "lastName", __storedValueForKey:__ looks
   for a method named _getLastName or _lastName.
2. If a private accessor isn't found, searches for an instance
   variable based on _key_ and returns
   its value directly. For example, with a key of "lastName", __storedValueForKey:__ looks
   for an instance variable named ___lastName__ or __lastName__.
3. If neither a private accessor or an instance variable is found, __storedValueForKey:__ searches
   for a public accessor method based on _key_.
   For the key "lastName", this would be getLastName or lastName.
4. If _key_ is unknown, __storedValueForKey:__ calls [handleTakeValue:forUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq).

This different search order allows an object to bypass processing
that is performed before returning a value through public API. However,
if you always want to use the search order in __valueForKey:__,
you can implement the class method [useStoredAccessor](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/useStoredAccessor) to
return NO. And as with __valueForKey:__, you
can prevent direct access of an instance variable with the method
the class method [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/accessInstanceVariablesDirectly).

---

### takeStoredValue:forKey:

`- (void)takeStoredValue:(id)value
forKey:(NSString *)key`

Sets the property identified by _key_ to _value_.
This method is used to initialize the receiver with values from
an object store (generally, this is ultimately from a database)
or to restore a value from a snapshot. The default implementation
provided by the Framework additions to NSObject is similar to the implementation
of [takeValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi),
but it resolves _key_ with a different
method-instance variable search order:

1. Searches for a private accessor method based
   on _key_ (a method preceded by an underbar).
   For example, with a key of "lastName", __takeStoredValue:forKey:__ looks
   for a method named _setLastName:.
2. If a private accessor isn't found, searches for an instance
   variable based on _key_ and sets its
   value directly. For example, with a key of "lastName", __takeStoredValue:forKey:__ looks
   for an instance variable named ___lastName__ or __lastName__.
3. If neither a private accessor or an instance variable is found, __takeStoredValue:forKey:__ searches
   for a public accessor method based on _key_.
   For the key "lastName", this would be setLastName:.
4. If _key_ is unknown, __takeStoredValue:forKey:__ calls [handleTakeValue:forUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq).

This different search order allows an object to bypass processing
that is performed before setting a value through public API. However,
if you always want to use the search order in __takeValue:forKey:__, you
can implement the class method [useStoredAccessor](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/useStoredAccessor) to
return NO. And as with __valueForKey:__, you
can prevent direct access of an instance variable with the method
the class method [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/accessInstanceVariablesDirectly).

---

### takeValue:forKey:

`- (void)takeValue:(id)value
forKey:(NSString *)key`

Sets the value for the property identified by _key_ to _value_,
invoking [handleTakeValue:forUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq) if the
receiver doesn't recognize _key_ and [unableToSetNullForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3vnzqwe3dfkrxvgzlujz2wy3cgn5zewzlzhi) if _value_ is nil and _key_ identifies
a scalar property.

The default implementation provided by the Framework additions
to NSObject works as follows:

1. Searches for a public accessor method of the
   form __set___Key___:__,
   invoking it if there is one.
2. If a public accessor method isn't found, searches for a
   private accessor method of the form ___set___Key___:__,
   invoking it if there is one.
3. If an accessor method isn't found and the class method [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/accessInstanceVariablesDirectly) returns YES, __takeValue:forKey:__ searches
   for an instance variable based on _key_ and
   sets the value directly, autoreleasing the old value and retaining
   the new one. For the key "lastName", this would be ___lastName__ or __lastName__.
4. If neither an accessor method nor an instance variable is
   found, the default implementation invokes [handleTakeValue:forUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq).

---

### unableToSetNullForKey:

`- (void)unableToSetNilForKey:(NSString
*)key`

Invoked from [takeValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi) (and [takeStoredValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a))
when it's given a nil value for a scalar property (such as an __int__ or
a __float__). NSObject's implementation raises
an NSInvalidArgumentException. Subclasses can override it to handle
the request in some other way, such as by substituting zero or a
sentinel value and invoking [takeValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi) again.

---

### valueForKey:

`- (id)valueForKey:(NSString
*)key`

Returns the value for the property identified
by _key_, invoking [handleQueryWithUnboundKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6j2) if the receiver
doesn't recognize _key_.

The default implementation provided by the Framework additions
to NSObject works as follows:

1. Searches for a public accessor method based on _key_.
   For example, with a key of "lastName", __valueForKey:__looks
   for a method named getLastName or lastName.
2. If a public accessor method isn't found, searches for a
   private accessor method based on _key_ (a method
   preceded by an underbar). For example, with a key of "lastName", __valueForKey:__ looks
   for a method named _getLastName or _lastName.
3. If an accessor method isn't found and the class method [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCoding.html#//apple_ref/occ/intfm/EOKeyValueCoding/accessInstanceVariablesDirectly) returns YES, __valueForKey:__ searches
   for an instance variable based on _key_ and
   returns its value directly. For the key "lastName", this would
   be _lastName or lastName.
4. If neither an accessor method nor an instance variable is
   found, the default implementation invokes __handleQueryWithUnboundKey:__.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
