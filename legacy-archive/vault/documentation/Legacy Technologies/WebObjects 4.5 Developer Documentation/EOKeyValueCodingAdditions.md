---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOKeyValueCodingAdditions.html
archived_at: '2026-07-15T08:11:43.497459Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOKeyValueCodingAdditions

> __(informal protocol)__

> __Declared in:__ : EOControl/EOKeyValueCoding.h

---

## Protocol Description

---

The EOKeyValueCodingAdditions informal protocol defines extensions
to the basic EOKeyValueCoding informal protocol. One pair of methods, [takeValuesFromDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65dbnnsvmylmovsxgrtsn5wui2ldoruw63tboj4tu) and [valuesForKeys:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65tbnr2wk42gn5zewzlzom5a),
gives access to groups of properties. Another pair of methods, [takeValue:forKeyPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65dbnnsvmylmovstuztpojfwk6kqmf2gqoq) and [valueForKeyPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgoqlemruxi2lpnzzs65tbnr2wkrtpojfwk6kqmf2gqoq) give
access to properties across relationships with key paths of the
form _relationship.property_; for example,
"department.name". the Framework additions to NSObject provide
default implementations of EOKeyValueCodingAdditions, which you
rarely (if ever) need to override.

## EONull in Collections

Because collection objects such as NSArray and NSDictionary
can't contain nil as a value, nil must be represented by a special
object, EONull. EONull provides a single instance that represents
the NULL value for object attributes. The default implementations
of __takeValuesFromDictionary:__ and __valuesForKeys:__ translate EONull
and `nil` between NSDictionaries
and enterprise objects so your objects don't have to explicitly
test for EONull values.

## Instance Methods

---

### takeValue:forKeyPath:

`- (void)takeValue:(id)value
forKeyPath:(NSString *)keyPath`

Sets the value for the property identified by _keyPath_ to _value_.
A key path has the form _relationship.property_ (with
one or more relationships); for example "movieRole.roleName"
or "movieRole.Talent.lastName". NSObject's implementation
of this method gets the destination object for each relationship
using [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi), and sends the final
object a [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi)message with _value_ and _property_.

---

### takeValuesFromDictionary:

`- (void)takeValuesFromDictionary:(NSDictionary
*)aDictionary`

Sets properties of the receiver with values
from _aDictionary_, using its keys
to identify the properties. NSObject's implementation invokes [takeValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwkvtbnr2wkotgn5zewzlzhi) for each key-value
pair, substituting nil for EONull values in _aDictionary_.

---

### valueForKeyPath:

`- (id)valueForKeyPath:(NSString
*)keyPath`

Returns the value for the derived property identified
by _keyPath_. A key path has the form _relationship.property_ (with
one or more relationships); for example "movieRole.roleName"
or "movieRole.Talent.lastName". NSObject's implementation
of this method gets the destination object for each relationship
using [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi), and returns the result
of a __valueForKey:__ message to the final object.

---

### valuesForKeys:

`- (NSDictionary *)valuesForKeys:(NSArray
*)keys`

Returns a dictionary containing the property
values identified by each of _keys_. NSObject's implementation
invokes [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi) for each key in _keys_,
substituting EONull values in the dictionary for returned nil values.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
