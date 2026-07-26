---
title: JSONEncoder.OutputFormatting
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/outputformatting-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/outputformatting-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/outputformatting-swift.struct.json'
content_hash: 'sha256:0409bcb6c1488a13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# JSONEncoder.OutputFormatting

<sub>Structure</sub>

The output formatting options that determine the readability, size, and element order of an encoded JSON object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OutputFormatting
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Formatting Output

- [prettyPrinted](outputformatting-swift.struct/prettyprinted.md) — The output formatting option that uses ample white space and indentation to make output easy to read.
- [sortedKeys](outputformatting-swift.struct/sortedkeys.md) — The output formatting option that sorts keys in lexicographic order.
- [withoutEscapingSlashes](outputformatting-swift.struct/withoutescapingslashes.md) — The output formatting option specifies that the output doesn’t prefix slash characters with escape characters.

### Creating Options

- [init(rawValue:)](<outputformatting-swift.struct/init(rawvalue_).md>) — Creates an OutputFormatting value with the given raw value.
- [rawValue](outputformatting-swift.struct/rawvalue.md) — The format’s default value.
- [init()](<init().md>) — Creates a new, reusable JSON encoder with the default formatting settings and encoding strategies.

## See Also

### Customizing Encoding

- [outputFormatting](outputformatting-swift.property.md) — A value that determines the readability, size, and element order of the encoded JSON object.
- [keyEncodingStrategy](keyencodingstrategy-swift.property.md) — A value that determines how to encode a  type’s coding keys as JSON keys.
- [KeyEncodingStrategy](keyencodingstrategy-swift.enum.md) — The values that determine how to encode a type’s coding keys as JSON keys.
- [userInfo](userinfo.md) — A dictionary you use to customize the encoding process by providing contextual information.
