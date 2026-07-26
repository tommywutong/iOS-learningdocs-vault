---
title: NSAttributeType.compositeAttributeType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributetype/compositeattributetype
source_url: 'https://developer.apple.com/documentation/coredata/nsattributetype/compositeattributetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributetype/compositeattributetype.json'
content_hash: 'sha256:0ef326748b3e33f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeType](../nsattributetype.md)

# NSAttributeType.compositeAttributeType

<sub>Case</sub>

An attribute that derives its value by composing other attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case compositeAttributeType
```

## Discussion

Composite attributes support all attribute types except the following:

- [NSUndefinedAttributeType](undefinedattributetype.md)
- [NSObjectIDAttributeType](objectidattributetype.md)
- [NSBinaryDataAttributeType](binarydataattributetype.md) (when [allowsExternalBinaryDataStorage](../nsattributedescription/allowsexternalbinarydatastorage.md) is [true](../../swift/true.md))

For more information, see [NSCompositeAttributeDescription](../nscompositeattributedescription.md).

## See Also

### Attribute types

- [NSBinaryDataAttributeType](binarydataattributetype.md) — An attribute that stores binary data.
- [NSBooleanAttributeType](booleanattributetype.md) — An attribute that stores a Boolean value.
- [NSDateAttributeType](dateattributetype.md) — An attribute that stores a date.
- [NSDecimalAttributeType](decimalattributetype.md) — An attribute that stores a decimal value.
- [NSDoubleAttributeType](doubleattributetype.md) — An attribute that stores a double value.
- [NSFloatAttributeType](floatattributetype.md) — An attribute that stores a float value.
- [NSInteger16AttributeType](integer16attributetype.md) — An attribute that stores a 16-bit signed integer value.
- [NSInteger32AttributeType](integer32attributetype.md) — An attribute that stores a 32-bit signed integer value.
- [NSInteger64AttributeType](integer64attributetype.md) — An attribute that stores a 64-bit signed integer value.
- [NSObjectIDAttributeType](objectidattributetype.md) — An attribute that stores a managed object’s ID.
- [NSStringAttributeType](stringattributetype.md) — An attribute that stores a string.
- [NSTransformableAttributeType](transformableattributetype.md) — An attribute that uses a value transformer to derive its value.
- [NSUndefinedAttributeType](undefinedattributetype.md) — An attribute that doesn’t have an explicit type.
- [NSURIAttributeType](uriattributetype.md) — An attribute that stores a uniform resource identifier.
- [NSUUIDAttributeType](uuidattributetype.md) — An attribute that stores a universally unique identifier.
