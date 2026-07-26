---
title: composite
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/attributetype-swift.struct/composite
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.struct/composite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/attributetype-swift.struct/composite.json'
content_hash: 'sha256:351ac6291d3f2a3f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Data](../../../coredata.md) · [NSAttributeDescription](../../nsattributedescription.md) · [AttributeType](../attributetype-swift.struct.md)

# composite

<sub>Type Property</sub>

An attribute that derives its value by composing other attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let composite: NSAttributeDescription.AttributeType
```

## Discussion

Composite attributes support all attribute types except the following:

- [undefined](undefined.md)
- [objectID](objectid.md)
- [binaryData](binarydata.md) (when [allowsExternalBinaryDataStorage](../allowsexternalbinarydatastorage.md) is [true](../../../swift/true.md))

For more information, see [NSCompositeAttributeDescription](../../nscompositeattributedescription.md).

## See Also

### Attribute Types

- [binaryData](binarydata.md) — An attribute that stores binary data.
- [boolean](boolean.md) — An attribute that stores a Boolean value.
- [date](date.md) — An attribute that stores a date.
- [decimal](decimal.md) — An attribute that stores a decimal value.
- [double](double.md) — An attribute that stores a double value.
- [float](float.md) — An attribute that stores a float value.
- [integer16](integer16.md) — An attribute that stores a 16-bit signed integer value.
- [integer32](integer32.md) — An attribute that stores a 32-bit signed integer value.
- [integer64](integer64.md) — An attribute that stores a 64-bit signed integer value.
- [objectID](objectid.md) — An attribute that stores a managed object’s ID.
- [string](string.md) — An attribute that stores a string.
- [transformable](transformable.md) — An attribute that uses a value transformer to derive its value.
- [undefined](undefined.md) — An attribute that doesn’t have an explicit type.
- [uri](uri.md) — An attribute that stores a uniform resource identifier.
- [uuid](uuid.md) — An attribute that stores a universally unique identifier.
