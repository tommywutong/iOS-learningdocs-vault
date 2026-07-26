---
title: JSONDecoder.NonConformingFloatDecodingStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder/nonconformingfloatdecodingstrategy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/nonconformingfloatdecodingstrategy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/nonconformingfloatdecodingstrategy-swift.enum.json'
content_hash: 'sha256:baaab0d350a6a5c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# JSONDecoder.NonConformingFloatDecodingStrategy

<sub>Enumeration</sub>

The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NonConformingFloatDecodingStrategy
```

## Overview

The IEEE 754 floating-point specification defines exceptional values, which include [infinity](../../swift/floatingpoint/infinity.md) and [nan](../../swift/floatingpoint/nan.md).

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Exceptional Values

- [JSONDecoder.NonConformingFloatDecodingStrategy.convertFromString(positiveInfinity:negativeInfinity:nan:)](<nonconformingfloatdecodingstrategy-swift.enum/convertfromstring(positiveinfinity_negativeinfinity_nan_).md>) — The strategy that decodes exceptional floating-point values from a specified string representation.
- [JSONDecoder.NonConformingFloatDecodingStrategy.throw](nonconformingfloatdecodingstrategy-swift.enum/throw.md) — The strategy that throws an error upon decoding an exceptional floating-point value.

## See Also

### Decoding Exceptional Numbers

- [nonConformingFloatDecodingStrategy](nonconformingfloatdecodingstrategy-swift.property.md) — The strategy used by a decoder when it encounters exceptional floating-point values.
