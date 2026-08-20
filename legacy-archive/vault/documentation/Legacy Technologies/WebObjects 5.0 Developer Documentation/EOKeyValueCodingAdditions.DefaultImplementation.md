---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOKVCAdditionsDftlImpl.html
archived_at: '2026-07-15T08:13:46.957484Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyValueCodingAdditions.DefaultImplementation

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

The EOKeyValueCodingAdditions.DefaultImplementation class provides default implementations of the EOKeyValueCodingAdditions interface.

An EOCustomObject uses EOKeyValueCodingAdditions.DefaultImplementation's default implementations. EOKeyValueCodingAdditions.Support also enables you to put non-enterprise objects into the interface layer by declaring that your class conforms to key-value coding.

The methods in the DefaultImplementation class are just like the methods defined by the EOKeyValueCodingAdditions interface, except they are all static methods and they take an extra argument-the enterprise object on which the default implementation should operate. For example, suppose you want to implement an Employee enterprise object class that doesn't inherit from EOCustomObject but that uses DefaultImplementation's default implementations. Employee's valuesForKeys method would look like this:

> ```
> public abstract NSDictionary valuesForKeys(NSArray keys)
>     return EOKeyValueCodingAdditions.Support.valuesForKeys(this, keys);
> }
> ```

## Static Methods

---

### takeValueForKeyPath

`public static void takeValueForKeyPath( NSKeyValueCoding anObject, Object value, String keyPath)`

Sets _anObject_'s property identified by _keyPath_ to _value_. A key path has the form _relationship.property_ (with one or more relationships). Support's implementation gets the destination object for each relationship using valueForKey, and sends the final object a takeValueForKeymessage with _value_ and _property_.

---

### takeValuesFromDictionary

`public static void takeValuesFromDictionary( NSKeyValueCoding anObject, NSDictionary aDictionary)`

Sets properties of _anObject_ with values from _aDictionary_, using its keys to identify the properties. Support's implementation invokes takeValueForKey for each key-value pair, substituting __null__ for EONullValues in _aDictionary_.

__See Also:__ takeValuesFromDictionary (EOKeyValueCodingAdditions)

---

### valueForKeyPath

`public static Object valueForKeyPath( NSKeyValueCoding anObject, String keyPath)`

Returns _anObject_'s value for the derived property identified by _keyPath_. A key path has the form _relationship.property_ (with one or more relationships). Support's implementation of this method gets the destination object for each relationship using valueForKey, and returns the result of a __valueForKey__ message to the final object.

---

### valuesForKeys

`public static NSDictionary valuesForKeys( NSKeyValueCoding anObject, NSArray keys)`

Returns a dictionary containing _anObject_'s property values identified by each of _keys_. Support's implementation invokes valueForKey for each key in _keys_, substituting EONullValues in the dictionary for returned __null__ values.

__See Also:__ valuesForKeys (EOKeyValueCodingAdditions)

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
