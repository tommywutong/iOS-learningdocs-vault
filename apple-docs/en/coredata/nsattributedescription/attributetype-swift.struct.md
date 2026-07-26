---
title: NSAttributeDescription.AttributeType
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/attributetype-swift.struct
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/attributetype-swift.struct.json'
content_hash: 'sha256:6feb9edd03ebbd7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# NSAttributeDescription.AttributeType

<sub>Structure</sub>

The types of attributes that Core Data supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AttributeType
```

## Overview

Core Data attribute types explicitly distinguish between bit size. This allows their values to exist independent of the persistent store that contains them. A scalar option is available for a number of attribute types, in some cases by default.

| **Attribute type** | **Type** | **Scalar type** | **Scalar by default** |
|---|---|---|---|
| Integer 16 | [NSNumber](../../foundation/nsnumber.md) | [Int16](../../swift/int16.md) | Yes |
| Integer 32 | [NSNumber](../../foundation/nsnumber.md) | [Int32](../../swift/int32.md) | Yes |
| Integer 64 | [NSNumber](../../foundation/nsnumber.md) | [Int64](../../swift/int64.md) | Yes |
| Double | [NSNumber](../../foundation/nsnumber.md) | [Double](../../swift/double.md) | Yes |
| Float | [NSNumber](../../foundation/nsnumber.md) | [Float](../../swift/float.md) | Yes |
| Boolean | [NSNumber](../../foundation/nsnumber.md) | [Bool](../../swift/bool.md) | Yes |
| Date | [NSDate](../../foundation/nsdate.md) | [TimeInterval](../../foundation/timeinterval.md) | No |
| Decimal | [NSDecimalNumber](../../foundation/nsdecimalnumber.md) | [NSDecimalNumber](../../foundation/nsdecimalnumber.md) | No |
| UUID | [UUID](../../foundation/uuid.md) | [UUID](../../foundation/uuid.md) | No |
| URI | [URL](../../foundation/url.md) | — | — |
| String | [String](../../swift/string.md) | — | — |
| Binary data | [Data](../../foundation/data.md) | — | — |
| Transformable | [NSObject](../../objectivec/nsobject-swift.class.md) | — | — |
| Composite | — | — | — |
| Undefined | — | — | — |

> [!note] Note
> If your application uses BLOBs (binary large objects), such as image and sound files, you can choose to store their data in a location that’s external to the persistent store.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md)

## Topics

### Attribute Types

- [binaryData](attributetype-swift.struct/binarydata.md) — An attribute that stores binary data.
- [boolean](attributetype-swift.struct/boolean.md) — An attribute that stores a Boolean value.
- [composite](attributetype-swift.struct/composite.md) — An attribute that derives its value by composing other attributes.
- [date](attributetype-swift.struct/date.md) — An attribute that stores a date.
- [decimal](attributetype-swift.struct/decimal.md) — An attribute that stores a decimal value.
- [double](attributetype-swift.struct/double.md) — An attribute that stores a double value.
- [float](attributetype-swift.struct/float.md) — An attribute that stores a float value.
- [integer16](attributetype-swift.struct/integer16.md) — An attribute that stores a 16-bit signed integer value.
- [integer32](attributetype-swift.struct/integer32.md) — An attribute that stores a 32-bit signed integer value.
- [integer64](attributetype-swift.struct/integer64.md) — An attribute that stores a 64-bit signed integer value.
- [objectID](attributetype-swift.struct/objectid.md) — An attribute that stores a managed object’s ID.
- [string](attributetype-swift.struct/string.md) — An attribute that stores a string.
- [transformable](attributetype-swift.struct/transformable.md) — An attribute that uses a value transformer to derive its value.
- [undefined](attributetype-swift.struct/undefined.md) — An attribute that doesn’t have an explicit type.
- [uri](attributetype-swift.struct/uri.md) — An attribute that stores a uniform resource identifier.
- [uuid](attributetype-swift.struct/uuid.md) — An attribute that stores a universally unique identifier.

## See Also

### Managing the type

- [attributeValueClassName](attributevalueclassname.md) — The class name that represents the attribute’s value.
- [type](type.md) — The attribute’s type.
- [attributeType](attributetype-swift.property.md) — The attribute’s type. _(deprecated)_
- [NSAttributeType](../nsattributetype.md) — The types of attribute that Core Data supports.
