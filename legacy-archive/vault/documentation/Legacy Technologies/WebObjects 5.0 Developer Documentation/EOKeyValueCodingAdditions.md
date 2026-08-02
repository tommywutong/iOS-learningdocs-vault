---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOKeyValueCodingAdditions.html
archived_at: '2026-07-15T08:13:48.101054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOKeyValueCodingAdditions

> __(informal interface)__

> __Implemented by:__ : EOEnterpriseObject: EOCustomObject: EOGenericRecord

> **__Implements:__**
> : EOKeyValueCoding: NSKeyValueCodingAdditions

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The EOKeyValueCodingAdditions interface defines extensions to the basic EOKeyValueCoding interface. One pair of methods, [takeValuesFromDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3umfvwkvtbnr2wk42gojxw2rdjmn2gs33omfzhs) and [valuesForKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4z2bmrsgs5djn5xhgl3wmfwhkzltizxxes3fpfzq), gives access to groups of properties. Another pair of methods, takeValueForKey and valueForKey give access to properties across relationships with key paths of the form _relationship.property_; for example, "department.name". EOCustomObject and EOGenericRecord provide default implementations of EOKeyValueCodingAdditions, which you rarely (if ever) need to override.

## EONullValue in Collections

Because collection objects such as NSArray and NSDictionary can't contain null as a value, null must be represented by a special object, EONullValue. EONullValue provides a single instance that represents the NULL value for object attributes. The default implementations of __takeValuesFromDictionary__ and __valuesForKeys__ translate EONullValue and `null` between NSDictionaries and enterprise objects so your objects don't have to explicitly test for EONullValues.

## Instance Methods

---

### takeValuesFromDictionary

`public abstract void takeValuesFromDictionary(NSDictionary aDictionary)`

Sets properties of the receiver with values from _aDictionary_, using its keys to identify the properties. EOCustomObject's implementation invokes takeValueForKey for each key-value pair, substituting null for EONullValues in _aDictionary_.

---

### valuesForKeys

`public abstract NSDictionary valuesForKeys(NSArray keys)`

Returns a dictionary containing the property values identified by each of _keys_. EOCustomObject's implementation invokes valueForKey for each key in _keys_, substituting EONullValues in the dictionary for returned null values.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
