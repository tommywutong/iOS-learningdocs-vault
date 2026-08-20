---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOKeyValueCodingAdditions.html
archived_at: '2026-07-18T01:28:41.306967Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOKeyValueCoding-4.md)
[!](EOMessageHandlers.md)

---

# EOKeyValueCodingAdditions

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOKeyValueCoding.h

## Protocol Description

The EOKeyValueCodingAdditions informal protocol defines extensions to the basic EOKeyValueCoding informal protocol. One pair of methods, __takeValuesFromDictionary:__ and __valuesForKeys:__ , gives access to groups of properties. Another pair of methods, __takeValue:forKeyPath:__ and __valueForKeyPath:__ give access to properties across relationships with key paths of the form _relationship.property_; for example, "department.name". the Framework additions to NSObject provide default implementations of EOKeyValueCodingAdditions, which you rarely (if ever) need to override.

---

### EONull in Collections

Because collection objects such as NSArray and NSDictionary can't contain __nil__ as a value, __nil__ must be represented by a special object, EONull. EONull provides a single instance that represents the NULL value for object attributes. The default implementations of __takeValuesFromDictionary:__ and __valuesForKeys:__ translate EONull and __nil__ between NSDictionaries and enterprise objects so your objects don't have to explicitly test for EONull values.

---

#### takeValue:forKeyPath:

- (void)__takeValue:__ (id)_value___forKeyPath:__ (NSString \*)_keyPath_

Sets the value for the property identified by _keyPath_ to _value_. A key path has the form _relationship.property_ (with one or more relationships); for example "movieRole.roleName" or "movieRole.Talent.lastName". NSObject's implementation of this method gets the destination object for each relationship using __[valueForKey:](EOKeyValueCoding-3.md)__ , and sends the final object a [__takeValue:forKey:__](EOKeyValueCoding-3.md)message with _value_ and _property_.

---

#### takeValuesFromDictionary:

- (void)__takeValuesFromDictionary:__ (NSDictionary \*)_aDictionary_

Sets properties of the receiver with values from _aDictionary_, using its keys to identify the properties. NSObject's implementation invokes [__takeValue:forKey:__](EOKeyValueCoding-3.md)for each key-value pair, substituting __nil__ for EONull values in _aDictionary_.

---

#### valueForKeyPath:

- (id)__valueForKeyPath:__ (NSString \*)_keyPath_

Returns the value for the derived property identified by _keyPath_. A key path has the form _relationship.property_ (with one or more relationships); for example "movieRole.roleName" or "movieRole.Talent.lastName". NSObject's implementation of this method gets the destination object for each relationship using __[valueForKey:](EOKeyValueCoding-3.md)__ , and returns the result of a __[valueForKey:](EOKeyValueCoding-3.md)__ message to the final object.

---

#### valuesForKeys:

- (NSDictionary \*)__valuesForKeys:__ (NSArray \*)_keys_

Returns a dictionary containing the property values identified by each of _keys_. NSObject's implementation invokes __[valueForKey:](EOKeyValueCoding-3.md)__ for each key in _keys_, substituting EONull values in the dictionary for returned __nil__ values.

---

[!](EOKeyValueCoding-4.md)
[!](EOMessageHandlers.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
