---
title: Schema.Version
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schema/version-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/version-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/version-swift.struct.json'
content_hash: 'sha256:19888512cabbba87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Schema](../schema.md)

# Schema.Version

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Version
```

## Relationships

- **Conforms To**: [Comparable](../../swift/comparable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<version-swift.struct/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<version-swift.struct/_(____).md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

### Initializers

- [init(_:_:_:)](<version-swift.struct/init(______).md>) — Initializes a version struct with the provided components of a semantic version.

### Instance Properties

- [description](version-swift.struct/description.md) — A textual description of the version object.
- [major](version-swift.struct/major.md) — The major version according to the semantic versioning standard.
- [minor](version-swift.struct/minor.md) — The minor version according to the semantic versioning standard.
- [patch](version-swift.struct/patch.md) — The patch version according to the semantic versioning standard.
