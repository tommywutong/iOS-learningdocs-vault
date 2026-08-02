---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOKeyValueCoding.html
archived_at: '2026-07-15T08:13:48.082998Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyValueCoding

> __(informal interface)__

> __Implemented by:__ EOKeyValueCodingAdditionsEOEnterpriseObjectEOCustomObjectEOGenericRecord

> __Implements:__ NSKeyValueCodingNSKeyValueCoding.ErrorHandling

> __Package:__ com.webobjects.eocontrol

---

## Interface Description

---

The EOKeyValueCoding interface defines Enterprise Objects Framework's main data transport mechanism, in which the properties of an object are accessed indirectly by name (or _key_), rather than directly through invocation of an accessor method or as instance variables. Thus, all of an object's properties can be accessed in a consistent manner. EOCustomObject and EOGenericRecord provide default implementations of EOKeyValueCoding, which are sufficient for most purposes.

The basic methods for accessing an object's values are takeValueForKey, which sets the value for the property identified by the specified key, and takeValueForKey, which returns the value for the property identified by the specified key. The default implementations provided by EOCustomObject use the accessor methods normally implemented by objects (or to access instance variables directly if need be), so that you don't have to write special code simply to integrate your objects into the Enterprise Objects Framework.

The corresponding methods [takeStoredValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe) and [storedValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q) are similar, but they're considered to be a private API, for use by the Framework for transporting data to and from _trusted_ sources. For example, __takeStoredValueForKey__ is used to initialize an object's properties with values fetched from the database, whereas __takeValueForKey__ is used to modify an object's properties to values provided by a user or other business logic. How these methods work and how they're used by the framework is discussed in more detail in the section ["Stored Value Methods" (page 387)](EOKeyValueCoding.Concepts.md#apple-ijauiq2difeec).

The remaining methods, handleQueryWithUnboundKey, handleTakeValueForUnboundKey, and unableToSetNullForKey, are provided to handle error conditions. The default versions of handleQueryWithUnboundKey and handleTakeValueForUnboundKey throw an exception.

For more information on EOKeyValueCoding, see the sections:

- ["Stored Value Methods" (page 387)](EOKeyValueCoding.Concepts.md#apple-ijauiq2difeec)
- ["Type Checking and Type Conversion" (page 388)](EOKeyValueCoding.Concepts.md#apple-ijauiq2kjjeuq)

## Method Types

---

> Accessing Values[storedValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q)[takeStoredValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe)

## Instance Methods

---

### storedValueForKey

`public abstract Object storedValueForKey(String key)`

Returns the property identified by _key_. This method is used when the value is retrieved for storage in an object store (generally, this is ultimately in a database) or for inclusion in a snapshot. The default implementation provided by EOCustomObject is similar to the implementation of valueForKey, but it resolves _key_ with a different method-instance variable search order:

1. Searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __storedValueForKey__ looks for a method named _getLastName or _lastName.
2. If a private accessor isn't found, searches for an instance variable based on _key_ and returns its value directly. For example, with a key of "lastName", __storedValueForKey__ looks for an instance variable named ___lastName__ or __lastName__.
3. If neither a private accessor or an instance variable is found, __storedValueForKey__ searches for a public accessor method based on _key_. For the key "lastName", this would be getLastName or lastName.
4. If _key_ is unknown, __storedValueForKey__ calls handleTakeValueForUnboundKey.

This different search order allows an object to bypass processing that is performed before returning a value through public API. However, if you always want to use the search order in __valueForKey__, you can implement the static method shouldUseStoredAccessors to return false. And as with __valueForKey__, you can prevent direct access of an instance variable with the method the static method canAccessFieldsDirectly.

---

### takeStoredValueForKey

`public abstract void takeStoredValueForKey( Object value, String key)`

Sets the property identified by _key_ to _value_. This method is used to initialize the receiver with values from an object store (generally, this is ultimately from a database) or to restore a value from a snapshot. The default implementation provided by EOCustomObject is similar to the implementation of takeValueForKey, but it resolves _key_ with a different method-instance variable search order:

1. Searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __takeStoredValueForKey__ looks for a method named _setLastName:.
2. If a private accessor isn't found, searches for an instance variable based on _key_ and sets its value directly. For example, with a key of "lastName", __takeStoredValueForKey__ looks for an instance variable named ___lastName__ or __lastName__.
3. If neither a private accessor or an instance variable is found, __takeStoredValueForKey__ searches for a public accessor method based on _key_. For the key "lastName", this would be setLastName:.
4. If _key_ is unknown, __takeStoredValueForKey__ calls handleTakeValueForUnboundKey.

This different search order allows an object to bypass processing that is performed before setting a value through public API. However, if you always want to use the search order in __takeValueForKey__, you can implement the static method shouldUseStoredAccessors to return false. And as with __valueForKey__, you can prevent direct access of an instance variable with the method the static method canAccessFieldsDirectly.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
