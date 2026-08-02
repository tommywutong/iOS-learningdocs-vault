---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOKeyValueCoding.html
archived_at: '2026-07-18T01:28:32.823279Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOFaulting.md)
[!](EOKeyValueCoding-2.md)

---

# EOKeyValueCoding

__Implemented By:__
EOEnterpriseObject
EOCustomObject
EOGenericRecord

__Implements:__
com.apple.client.foundation.NSKeyValueCoding (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Interface Description

The EOKeyValueCoding interface defines Enterprise Objects Framework's main data transport mechanism, in which the properties of an object are accessed indirectly by name (or _key_), rather than directly through invocation of an accessor method or as instance variables. Thus, all of an object's properties can be accessed in a consistent manner. EOCustomObject and EOGenericRecord provide default implementations of EOKeyValueCoding, which are sufficient for most purposes.

The basic methods for accessing an object's values are __takeValueForKey__ , which sets the value for the property identified by the specified key, and __valueForKey__ , which returns the value for the property identified by the specified key. The default implementations provided by EOCustomObject use the accessor methods normally implemented by objects (or to access instance variables directly if need be), so that you don't have to write special code simply to integrate your objects into the Enterprise Objects Framework.

The corresponding methods __takeStoredValueForKey__ and __storedValueForKey__ are similar, but they're considered to be a private API, for use by the Framework for transporting data to and from _trusted_ sources. For example, __takeStoredValueForKey__ is used to initialize an object's properties with values fetched from the database, whereas __takeValueForKey__ is used to modify an object's properties to values provided by a user or other business logic. How these methods work and how they're used by the framework is discussed in more detail in the section "[Stored Value Methods](EOKeyValueCoding-2.md)."

The remaining methods, __handleQueryWithUnboundKey__ , __handleTakeValueForUnboundKey__ , and __unableToSetNullForKey__ , are provided to handle error conditions. The default versions of __handleQueryWithUnboundKey__ and __handleTakeValueForUnboundKey__ throw an exception.

For more information on EOKeyValueCoding, see the sections:

- [Stored Value Methods](EOKeyValueCoding-2.md)
- [Type Checking and Type Conversion](EOKeyValueCoding-2.md)

## Interfaces Implemented

**NSKeyValueCoding (Java Client only)**

**takeValueForKey

**valueForKey****

## Method Types

**Accessing values**

**- storedValueForKey

**- takeStoredValueForKey

**- takeValueForKey

**- valueForKey********

**Handling error conditions**

**- handleQueryWithUnboundKey

**- handleTakeValueForUnboundKey

**- unableToSetNullForKey******

## Instance Methods

---

#### handleQueryWithUnboundKey

public abstract java.lang.Object __handleQueryWithUnboundKey__ (java.lang.String _key_)

Invoked from __valueForKey__ when it finds no property binding for _key_. EOCustomObject's implementation throws an exception. Subclasses can override this method to handle the query in some other way.

---

#### handleTakeValueForUnboundKey

public abstract void __handleTakeValueForUnboundKey__ (
java.lang.Object _value_,
java.lang.String _key_)

Invoked from __takeValueForKey__ when it finds no property binding for _key_. EOCustomObject's implementation throws an exception. Subclasses can override it to handle the request in some other way.

---

#### storedValueForKey

public abstract java.lang.Object __storedValueForKey__ (java.lang.String _key_)

Returns the property identified by _key_. This method is used when the value is retrieved for storage in an object store (generally, this is ultimately in a database) or for inclusion in a snapshot. The default implementation provided by EOCustomObject is similar to the implementation of __valueForKey__ , but it resolves _key_ with a different method-instance variable search order:

- Searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __storedValueForKey__ looks for a method named `_getLastName` or `_lastName.`
- If a private accessor isn't found, searches for an instance variable based on _key_ and returns its value directly. For example, with a key of "lastName", __storedValueForKey__ looks for an instance variable named ___lastName__ or __lastName__ .
- If neither a private accessor or an instance variable is found, __storedValueForKey__ searches for a public accessor method based on _key_. For the key "lastName", this would be `getLastName` or `lastName`.
- If _key_ is unknown, __storedValueForKey__ calls __handleTakeValueForUnboundKey__ .

This different search order allows an object to bypass processing that is performed before returning a value through public API. However, if you always want to use the search order in __valueForKey__ , you can implement the static method [__useStoredAccessor__](EOCustomObject.md)to return __false__ . And as with __valueForKey__ , you can prevent direct access of an instance variable with the method the static method [__accessInstanceVariablesDirectly__](EOCustomObject.md).

---

#### takeStoredValueForKey

public abstract void __takeStoredValueForKey__ (
java.lang.Object _value_,
java.lang.String _key_)

Sets the property identified by _key_ to _value_. This method is used to initialize the receiver with values from an object store (generally, this is ultimately from a database) or to restore a value from a snapshot. The default implementation provided by EOCustomObject is similar to the implementation of __takeValueForKey__ , but it resolves _key_ with a different method-instance variable search order:

- Searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __takeStoredValueForKey__ looks for a method named `_setLastName.`
- If a private accessor isn't found, searches for an instance variable based on _key_ and and sets its value directly. For example, with a key of "lastName", __takeStoredValueForKey__ looks for an instance variable named ___lastName__ or __lastName__ .
- If neither a private accessor or an instance variable is found, __takeStoredValueForKey__ searches for a public accessor method based on _key_. For the key "lastName", this would be `setLastName`.
- If _key_ is unknown, __storedValueForKey__ calls __handleTakeValueForUnboundKey__ .

This different search order allows an object to bypass processing that is performed before setting a value through public API. However, if you always want to use the search order in __takeValueForKey__ , you can implement the static method [__useStoredAccessor__](EOCustomObject.md)to return __false__ . And as with __valueForKey__ , you can prevent direct access of an instance variable with the method the static method [__accessInstanceVariablesDirectly__](EOCustomObject.md).

---

#### takeValueForKey

public abstract void __takeValueForKey__ (
java.lang.Object _value_,
java.lang.String _key_)

Sets the value for the property identified by _key_ to _value_, invoking __handleTakeValueForUnboundKey__ if the receiver doesn't recognize _key_ and __unableToSetNullForKey__ if _value_ is __null__ and _key_ identifies a scalar property.

The default implementation provided by EOCustomObject works as follows:

- Searches for a public accessor method of the form __set__ _Key_, invoking it if there is one.
- If a public accessor method isn't found, searches for a private accessor method of the form ___set__ _Key_, invoking it if there is one.
- If an accesor method isn't found and the static method [__accessInstanceVariablesDirectly__](EOCustomObject.md)returns __true__ , __takeValueForKey__ searches for an instance variable based on _key_ and sets the value directly. For the key "lastName", this would be ___lastName__ or __lastName__ .
- If neither an accessor method nor an instance variable is found, the default implementation invokes __handleTakeValueForUnboundKey__ .

---

#### unableToSetNullForKey

public abstract void __unableToSetNullForKey__ (java.lang.String _key_)

Invoked from __takeValueForKey__ (and __takeStoredValueForKey__ ) when it's given a __null__ value for a scalar property (such as an __int__ or a __float__ ). EOCustomObject's implementation throws an exception. Subclasses can override it to handle the request in some other way, such as by substituting zero or a sentinel value and invoking __takeValueForKey__ again.

---

#### valueForKey

public abstract java.lang.Object __valueForKey__ (java.lang.String _key_)

Returns the value for the property identified by _key_, invoking __handleQueryWithUnboundKey__ if the receiver doesn't recognize _key_.

The default implementation provided by EOCustomObject works as follows:

- Searches for a public accessor method based on _key_. For example, with a key of "lastName", __valueForKey__ looks for a method named `getLastName` or `lastName`.
- If a public accessor method isn't found, searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __valueForKey__ looks for a method named `_getLastName` or `_lastName.`
- If an accesor method isn't found and the static method [__accessInstanceVariablesDirectly__](EOCustomObject.md)returns __true__ , __valueForKey__ searches for an instance variable based on _key_ and returns its value directly. For the key "lastName", this would be `_lastName` or `lastName`.
- If neither an accessor method nor an instance variable is found, the default implementation invokes __handleQueryWithUnboundKey__ .

---

[!](EOFaulting.md)
[!](EOKeyValueCoding-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
