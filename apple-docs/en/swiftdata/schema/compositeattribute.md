---
title: Schema.CompositeAttribute
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/compositeattribute
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/compositeattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/compositeattribute.json'
content_hash: 'sha256:7093a53435b80084'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Schema](../schema.md)

# Schema.CompositeAttribute

<sub>Class</sub>

An object that describes an attribute that derives its value by composing other attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class CompositeAttribute
```

## Relationships

- **Inherits From**: [Attribute](attribute.md)

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [SchemaProperty](../schemaproperty.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a composite attribute

- [init(name:originalName:options:valueType:defaultValue:hashModifier:)](<compositeattribute/init(name_originalname_options_valuetype_defaultvalue_hashmodifier_).md>)

### Composing attributes

- [properties](compositeattribute/properties.md)

### Encoding and decoding

- [encode(to:)](<compositeattribute/encode(to_).md>) — Encodes this value into the given encoder.
- [init(from:)](<compositeattribute/init(from_).md>)

### Debugging

- [debugDescription](compositeattribute/debugdescription.md) — A textual representation of this instance, suitable for debugging.

### Operators

- [==(_:_:)](<compositeattribute/==(____).md>)

## See Also

### Attributes

- [Attribute](attribute.md) — An object that describes the configuration and behavior of a specific property of a model class.
