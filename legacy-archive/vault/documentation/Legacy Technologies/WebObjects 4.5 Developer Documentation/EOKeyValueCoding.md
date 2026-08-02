---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOKeyValueCoding.html
archived_at: '2026-07-15T08:11:38.941749Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOKeyValueCoding

> __Implemented by:__ : EOKeyValueCodingAdditions
> : EOEnterpriseObject
> : EOCustomObject
> : EOGenericRecord

> **__Implements:__**
> : (com.apple.client.eocontrol only) NSKeyValueCoding

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The EOKeyValueCoding interface defines Enterprise Objects
Framework's main data transport mechanism, in which the properties
of an object are accessed indirectly by name (or _key_),
rather than directly through invocation of an accessor method or
as instance variables. Thus, all of an object's properties can
be accessed in a consistent manner. EOCustomObject and EOGenericRecord provide default
implementations of EOKeyValueCoding, which are sufficient for most
purposes.

The basic methods for accessing an object's values are [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz),
which sets the value for the property identified by the specified
key, and [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe),
which returns the value for the property identified by the specified
key. The default implementations provided by EOCustomObject use
the accessor methods normally implemented by objects (or to access
instance variables directly if need be), so that you don't have
to write special code simply to integrate your objects into the
Enterprise Objects Framework.

The corresponding methods [takeStoredValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe) and [storedValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q) are
similar, but they're considered to be a private API, for use by
the Framework for transporting data to and from _trusted_ sources.
For example, `takeStoredValueForKey` is used
to initialize an object's properties with values fetched from
the database, whereas `takeValueForKey` is
used to modify an object's properties to values provided by a
user or other business logic. How these methods work and how they're
used by the framework is discussed in more detail in the section ["Stored Value Methods"](EOKeyValueCoding-2.md#apple-ijauiq2difeec).

The remaining methods, [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvixkzlspflws5dikvxge33vnzsewzlz), [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs),
and [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpovxgcytmmvkg6u3forhhk3dmizxxes3fpe),
are provided to handle error conditions. The default versions of [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvixkzlspflws5dikvxge33vnzsewzlz) and [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs) throw an
exception.

For more information on EOKeyValueCoding, see the sections:

- ["Stored Value Methods"](EOKeyValueCoding-2.md#apple-ijauiq2difeec)
- ["Type Checking and Type Conversion"](EOKeyValueCoding-2.md#apple-ijauiq2kjjeuq)

## Constants

---

EOKeyValueCoding defines the following `int` constants to
be used as possible arguments for the [createKeyValueBindingForKey](EOKeyValueCoding.KeyBindingCreation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzojnsxsqtjnzsgs3thinzgkylunfxw4l3dojswc5dfjnsxsvtbnr2wkqtjnzsgs3thizxxes3fpe) and [keyValueBindingForKey](EOKeyValueCoding.KeyBindingCreation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzojnsxsqtjnzsgs3thinzgkylunfxw4l3lmv4vmylmovsue2lomruw4z2gn5zewzlz) methods. The
argument indicates whether the return value, a [EOKeyValueCoding.KeyBinding](EOKeyValueCoding.KeyBinding.md#apple-ineegqshjfeui) object,
binds a class/key pair to a mechanism to set the value for a key
or to retrieve it.

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| SetKeyBindingMask | Designates a binding as one responsible for setting an object's value. |
| StoredKeyBindingMask | Designates a binding as one responsible for retrieving an object's value. |

## Interfaces Implemented

---

> NSKeyValueCoding
> (com.apple.client.eocontrol only): [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz)
> : [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe)

## Method Types

---

> **Accessing values**
> : [storedValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q)
> : [takeStoredValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe)
> : [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz)
> : [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe)
>
> **Handling error conditions**
> : [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvixkzlspflws5dikvxge33vnzsewzlz)
> : [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs)
> : [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpovxgcytmmvkg6u3forhhk3dmizxxes3fpe)

## Instance Methods

---

### handleQueryWithUnboundKey

`public abstract Object handleQueryWithUnboundKey(String key)`

Invoked from [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe) when it finds no property
binding for _key._ EOCustomObject's implementation throws an exception.
Subclasses can override this method to handle the query in some other
way.

---

### handleTakeValueForUnboundKey

`public abstract void handleTakeValueForUnboundKey(
Object value,
String key)`

Invoked from [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) when it finds no
property binding for _key._ EOCustomObject's implementation throws
an exception. Subclasses can override it to handle the request in
some other way.

---

### storedValueForKey

`public abstract Object storedValueForKey(String key)`

Returns the property identified by _key._
This method is used when the value is retrieved for storage in an
object store (generally, this is ultimately in a database) or for
inclusion in a snapshot. The default implementation provided by EOCustomObject is
similar to the implementation of [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpozqwy5lfizxxes3fpe), but it resolves _key_ with
a different method-instance variable search order:

1. Searches for a private accessor method based
   on _key_ (a method preceded by an underbar).
   For example, with a key of "lastName", `storedValueForKey` looks
   for a method named _getLastName or _lastName.
2. If a private accessor isn't found, searches for an instance
   variable based on _key_ and returns
   its value directly. For example, with a key of "lastName", `storedValueForKey` looks
   for an instance variable named `_lastName` or `lastName`.
3. If neither a private accessor or an instance variable is found, `storedValueForKey` searches
   for a public accessor method based on _key._
   For the key "lastName", this would be getLastName or lastName.
4. If _key_ is unknown, `storedValueForKey` calls [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs).

This different search order allows an object to bypass processing
that is performed before returning a value through public API. However,
if you always want to use the search order in `valueForKey`,
you can implement the static method [useStoredAccessor](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf52xgzktorxxezleifrwgzltonxxe) to return false.
And as with `valueForKey`, you can prevent
direct access of an instance variable with the method the static method [accessInstanceVariablesDirectly](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5qwgy3fonzus3ttorqw4y3fkzqxe2lbmjwgk42enfzgky3unr4q).

---

### takeStoredValueForKey

`public abstract void takeStoredValueForKey(
Object value,
String key)`

Sets the property identified by _key_ to _value._
This method is used to initialize the receiver with values from
an object store (generally, this is ultimately from a database)
or to restore a value from a snapshot. The default implementation
provided by EOCustomObject is similar to the implementation of [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz),
but it resolves _key_ with a different
method-instance variable search order:

1. Searches for a private accessor method based
   on _key_ (a method preceded by an underbar).
   For example, with a key of "lastName", `takeStoredValueForKey` looks
   for a method named _setLastName.
2. If a private accessor isn't found, searches for an instance
   variable based on _key_ and sets its
   value directly. For example, with a key of "lastName", `takeStoredValueForKey` looks
   for an instance variable named `_lastName` or `lastName`.
3. If neither a private accessor or an instance variable is found, `takeStoredValueForKey` searches
   for a public accessor method based on _key._
   For the key "lastName", this would be setLastName.
4. If _key_ is unknown, `takeStoredValueForKey` calls [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs).

This different search order allows an object to bypass processing
that is performed before setting a value through public API. However,
if you always want to use the search order in `takeValueForKey`,
you can implement the static method [useStoredAccessor](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf52xgzktorxxezleifrwgzltonxxe) to return false.
And as with `valueForKey`, you can prevent
direct access of an instance variable with the method the static method [accessInstanceVariablesDirectly](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5qwgy3fonzus3ttorqw4y3fkzqxe2lbmjwgk42enfzgky3unr4q).

---

### takeValueForKey

`public abstract void takeValueForKey(
Object value,
String key)`

Sets the value for the property identified by _key_ to _value,_
invoking [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs) if
the receiver doesn't recognize _key_ and [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpovxgcytmmvkg6u3forhhk3dmizxxes3fpe) if _value_ is null and _key_ identifies
a scalar property.

The default implementation provided by EOCustomObject works
as follows:

1. Searches for a public accessor method of the
   form `set` _Key_ ,
   invoking it if there is one.
2. If a public accessor method isn't found, searches for a
   private accessor method of the form `_set` _Key_ , invoking
   it if there is one.
3. If an accessor method isn't found and the static method [accessInstanceVariablesDirectly](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5qwgy3fonzus3ttorqw4y3fkzqxe2lbmjwgk42enfzgky3unr4q) returns true, `takeValueForKey` searches
   for an instance variable based on _key_ and
   sets the value directly. For the key "lastName", this would
   be `_lastName` or `lastName`.
4. If neither an accessor method nor an instance variable is
   found, the default implementation invokes [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs).

---

### unableToSetNullForKey

`public abstract void unableToSetNullForKey(String key)`

Invoked from [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) (and [takeStoredValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe))
when it's given a null value for a scalar property (such as an `int` or
a `float`). EOCustomObject's implementation throws
an exception. Subclasses can override it to handle the request in
some other way, such as by substituting zero or a sentinel value
and invoking [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzkwmfwhkzkgn5zewzlz) again.

---

### valueForKey

`public abstract Object valueForKey(String key)`

Returns the value for the property identified
by _key,_ invoking [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvixkzlspflws5dikvxge33vnzsewzlz) if the
receiver doesn't recognize _key._

The default implementation provided by EOCustomObject works
as follows:

1. Searches for a public accessor method based on _key._
   For example, with a key of "lastName", `valueForKey`looks
   for a method named getLastName or lastName.
2. If a public accessor method isn't found, searches for a
   private accessor method based on _key_ (a method
   preceded by an underbar). For example, with a key of "lastName", `valueForKey` looks
   for a method named _getLastName or _lastName.
3. If an accessor method isn't found and the static method [accessInstanceVariablesDirectly](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3von2g63kpmjvgky3uf5qwgy3fonzus3ttorqw4y3fkzqxe2lbmjwgk42enfzgky3unr4q) returns true, `valueForKey` searches
   for an instance variable based on _key_ and
   returns its value directly. For the key "lastName", this would
   be _lastName or lastName.
4. If neither an accessor method nor an instance variable is
   found, the default implementation invokes `handleQueryWithUnboundKey`.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
