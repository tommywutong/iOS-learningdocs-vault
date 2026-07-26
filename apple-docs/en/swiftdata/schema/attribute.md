---
title: Schema.Attribute
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/attribute
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/attribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/attribute.json'
content_hash: 'sha256:a74290af3ce9a506'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Schema](../schema.md)

# Schema.Attribute

<sub>Class</sub>

An object that describes the configuration and behavior of a specific property of a model class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Attribute
```

## Relationships

- **Inherited By**: [CompositeAttribute](compositeattribute.md)

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [SchemaProperty](../schemaproperty.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an attribute

- [init(_:originalName:hashModifier:)](<attribute/init(__originalname_hashmodifier_).md>)
- [init(name:originalName:options:valueType:defaultValue:hashModifier:)](<attribute/init(name_originalname_options_valuetype_defaultvalue_hashmodifier_).md>)

### Specifying value information

- [defaultValue](attribute/defaultvalue.md)

### Determining behavior

- [options](attribute/options.md)
- [isTransformable](attribute/istransformable.md)

### Versioning

- [hashModifier](attribute/hashmodifier.md)

### Structures

- [Option](attribute/option.md)

### Instance Properties

- [isCodable](attribute/iscodable.md)

## See Also

### Attributes

- [CompositeAttribute](compositeattribute.md) — An object that describes an attribute that derives its value by composing other attributes.
