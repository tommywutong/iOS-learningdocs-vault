---
title: JSONEncoder.NonConformingFloatEncodingStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/nonconformingfloatencodingstrategy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/nonconformingfloatencodingstrategy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/nonconformingfloatencodingstrategy-swift.enum.json'
content_hash: 'sha256:401664bc5d30f8cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# JSONEncoder.NonConformingFloatEncodingStrategy

<sub>Enumeration</sub>

The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NonConformingFloatEncodingStrategy
```

## Overview

The IEEE 754 floating-point specification defines exceptional values, which include [infinity](../../swift/floatingpoint/infinity.md) and [nan](../../swift/floatingpoint/nan.md).

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Exceptional Values

- [JSONEncoder.NonConformingFloatEncodingStrategy.convertToString(positiveInfinity:negativeInfinity:nan:)](<nonconformingfloatencodingstrategy-swift.enum/converttostring(positiveinfinity_negativeinfinity_nan_).md>) — The strategy that encodes exceptional floating-point values from a specified string representation.
- [JSONEncoder.NonConformingFloatEncodingStrategy.throw](nonconformingfloatencodingstrategy-swift.enum/throw.md) — The strategy that throws an error upon encoding an exceptional floating-point value.

## See Also

### Encoding Exceptional Numbers

- [nonConformingFloatEncodingStrategy](nonconformingfloatencodingstrategy-swift.property.md) — The strategy used by an encoder when it encounters exceptional floating-point values.
