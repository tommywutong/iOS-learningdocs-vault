---
title: 'encode(_:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/encodableattributedstringkey/encode(_:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/encodableattributedstringkey/encode(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/encodableattributedstringkey/encode%28_%3Ato%3A%29.json'
content_hash: 'sha256:aeaac5f3f3621769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [EncodableAttributedStringKey](../encodableattributedstringkey.md)

# encode(_:to:)

<sub>Type Method</sub>

Encodes a value to the provided encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func encode(_ value: Self.Value, to encoder: any Encoder) throws
```

## Parameters

- `value` — The value to encode.

- `encoder` — The encoder to write data to.

## Discussion

This method throws an error if writing to the encoder fails.

## Default Implementations

### EncodableAttributedStringKey Implementations

- [encode(_:to:)](<encode(__to_)-16dss.md>) — Encodes an Objective-C value to the provided encoder, using a default implementation.
- [encode(_:to:)](<encode(__to_)-47oas.md>)
