---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOKeyValueCodingDftlImpl.html
archived_at: '2026-07-15T08:13:47.025655Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyValueCoding.DefaultImplementation

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOKeyValueCoding.Support provides default implementations of the EOKeyValueCoding interface.

An EOCustomObject uses EOKeyValueCoding.Support's default implementations. Typically your custom enterprise object classes inherit from EOCustomObject and inherit the default implementations. EOKeyValueCoding.Support also enables you to put non-enterprise objects into the interface layer by declaring that your class conforms to key-value coding.

The methods in the Support class are just like the methods defined by the EOKeyValueCoding interface, except they are all static methods and they take an extra argument-the enterprise object on which the default implementation should operate. For example, suppose you want to implement an Employee enterprise object class that doesn't inherit from EOCustomObject but that uses Support's default implementations. Employee's valueForKey method would look like this:

> ```
> public Object valueForKey(String key)
>     return EOKeyValueCoding.Support.valueForKey(this, key);
> }
> ```

## Method Types

---

> **Accessing values**
> : storedValueForKey: takeStoredValueForKey
>
> **Handling error conditions**
> : handleQueryWithUnboundKey

## Static Methods

---

### handleQueryWithUnboundKey

`public static Object handleQueryWithUnboundKey( Object anObject, String key)`

Throws an IllegalArgumentException.

---

### storedValueForKey

`public static Object storedValueForKey( Object anObject, String key)`

Returns _anObject_'s property identified by _key_. Similar to the implementation of valueForKey, but __storedValueForKey__ resolves _key_ with a different method-instance variable search order:

1. Searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __storedValueForKey__ looks for a method named _getLastName or _lastName.
2. If a private accessor isn't found, searches for an instance variable based on _key_ and returns its value directly. For example, with a key of "lastName", __storedValueForKey__ looks for an instance variable named ___lastName__ or __lastName__.
3. If neither a private accessor or an instance variable is found, __storedValueForKey__ searches for a public accessor method based on _key_. For the key "lastName", this would be getLastName or lastName.

__See Also:__ storedValueForKey (EOKeyValueCoding)

---

### takeStoredValueForKey

`public static void takeStoredValueForKey( Object anObject, Object value, String key)`

Sets _anObject_'s property identified by _key_ to _value_. Similar to the implementation of takeValueForKey, but it resolves _key_ with a different method-instance variable search order:

1. Searches for a private accessor method based on _key_ (a method preceded by an underbar). For example, with a key of "lastName", __takeStoredValueForKey__ looks for a method named _setLastName.
2. If a private accessor isn't found, searches for an instance variable based on _key_ and sets its value directly. For example, with a key of "lastName", __takeStoredValueForKey__ looks for an instance variable named ___lastName__ or __lastName__.
3. If neither a private accessor or an instance variable is found, __takeStoredValueForKey__ searches for a public accessor method based on _key_. For the key "lastName", this would be setLastName.

__See Also:__ takeStoredValueForKey (EOKeyValueCoding)

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
