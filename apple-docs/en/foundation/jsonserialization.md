---
title: JSONSerialization
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonserialization
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization.json'
content_hash: 'sha256:3f3c144ce7520729'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# JSONSerialization

<sub>Class</sub>

An object that converts between JSON and the equivalent Foundation objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class JSONSerialization
```

## Overview

You use the [JSONSerialization](jsonserialization.md) class to convert JSON to Foundation objects and convert Foundation objects to JSON.

To convert a Foundation object to JSON, the object must have the following properties:

- The top level object is an [NSArray](nsarray.md) or [NSDictionary](nsdictionary.md), unless you set the [NSJSONWritingFragmentsAllowed](jsonserialization/writingoptions/fragmentsallowed.md) option.
- All objects are instances of [NSString](nsstring.md), [NSNumber](nsnumber.md), [NSArray](nsarray.md), [NSDictionary](nsdictionary.md), or [NSNull](nsnull.md).
- All dictionary keys are instances of [NSString](nsstring.md).
- Numbers are neither `NaN` nor infinity.

Other rules may apply. Calling [+ isValidJSONObject:](<jsonserialization/isvalidjsonobject(__).md>) or attempting a conversion are the definitive ways to tell if the [JSONSerialization](jsonserialization.md) class can convert given object to JSON data.

> [!note] Note
> On iOS 7 and later and macOS 10.9 and later, [JSONSerialization](jsonserialization.md) is thread safe.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a JSON Object

- [+ JSONObjectWithData:options:error:](<jsonserialization/jsonobject(with_options_)-8demi.md>) — Returns a Foundation object from given JSON data.
- [+ JSONObjectWithStream:options:error:](<jsonserialization/jsonobject(with_options_)-3afap.md>) — Returns a Foundation object from JSON data in a given stream.
- [ReadingOptions](jsonserialization/readingoptions.md) — Options used when creating Foundation objects from JSON data.

### Creating JSON Data

- [+ dataWithJSONObject:options:error:](<jsonserialization/data(withjsonobject_options_).md>) — Returns JSON data from a Foundation object.
- [+ writeJSONObject:toStream:options:error:](<jsonserialization/writejsonobject(__to_options_error_).md>) — Writes a given JSON object to a stream.
- [WritingOptions](jsonserialization/writingoptions.md) — Options for writing JSON data.
- [+ isValidJSONObject:](<jsonserialization/isvalidjsonobject(__).md>) — Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.

## See Also

### JSON

- [Using JSON with custom types](using-json-with-custom-types.md) — Encode and decode JSON data, regardless of its structure, using Swift’s JSON support.
- [JSONEncoder](jsonencoder.md) — An object that encodes instances of a data type as JSON objects.
- [JSONDecoder](jsondecoder.md) — An object that decodes instances of a data type from JSON objects.
