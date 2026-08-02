---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOKeyValueCodingAdditions.html
archived_at: '2026-07-18T01:28:32.929151Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOKeyValueCoding-2.md)
[!](EOEditingContext.MessageHandler.md)

---

# EOKeyValueCodingAdditions

__Implemented By:__
EOEnterpriseObject
EOCustomObject
EOGenericRecord

__Implements:__
com.apple.client.foundation.NSKeyValueCoding (Java Client only)
EOKeyValueCoding

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Interface Description

The EOKeyValueCodingAdditions interface defines extensions to the basic EOKeyValueCoding interface. One pair of methods, __takeValuesFromDictionary__ and __valuesForKeys__ , gives access to groups of properties. Another pair of methods, __takeValueForKeyPath__ and __valueForKeyPath__ give access to properties across relationships with key paths of the form _relationship.property_; for example, "department.name". EOCustomObject and EOGenericRecord provide default implementations of EOKeyValueCodingAdditions, which you rarely (if ever) need to override.

---

### EONullValue in Collections

Because collection objects such as NSArray and NSDictionary can't contain __null__ as a value, __null__ must be represented by a special object, EONullValue. EONullValue provides a single instance that represents the NULL value for object attributes. The default implementations of __takeValuesFromDictionary__ and __valuesForKeys__ translate EONullValue and __null__ between between NSDictionaries and enterprise objects so your objects don't have to explicitly test for EONullValues.

## Instance Methods

---

#### takeValueForKeyPath

public abstract void __takeValueForKeyPath__ (
java.lang.Object _value_,
java.lang.String _keyPath_)

Sets the value for the property identified by _keyPath_ to _value_. A key path has the form _relationship.property_ (with one or more relationships); for example "movieRole.roleName" or "movieRole.Talent.lastName". EOCustomObject's implementation of this method gets the destination object for each relationship using __[valueForKey](EOKeyValueCoding.md)__ , and sends the final object a [__takeValueForKey__](EOKeyValueCoding.md)message with _value_ and _property_.

---

#### takeValuesFromDictionary

public abstract void __takeValuesFromDictionary__ (NSDictionary _aDictionary_)

Sets properties of the receiver with values from _aDictionary_, using its keys to identify the properties. EOCustomObject's implementation invokes [__takeValueForKey__](EOKeyValueCoding.md)for each key-value pair, substituting __null__ for EONullValues in _aDictionary_.

---

#### valueForKeyPath

public abstract java.lang.Object __valueForKeyPath__ (java.lang.String _keyPath_)

Returns the value for the derived property identified by _keyPath_. A key path has the form _relationship.property_ (with one or more relationships); for example "movieRole.roleName" or "movieRole.Talent.lastName". EOCustomObject's implementation of this method gets the destination object for each relationship using __[valueForKey](EOKeyValueCoding.md)__ , and returns the result of a __[valueForKey](EOKeyValueCoding.md)__ message to the final object.

---

#### valuesForKeys

public abstract NSDictionary __valuesForKeys__ (NSArray _keys_)

Returns a dictionary containing the property values identified by each of _keys_. EOCustomObject's implementation invokes __[valueForKey](EOKeyValueCoding.md)__ for each key in _keys_, substituting EONullValues in the dictionary for returned __null__ values.

---

[!](EOKeyValueCoding-2.md)
[!](EOEditingContext.MessageHandler.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
