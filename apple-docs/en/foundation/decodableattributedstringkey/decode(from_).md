---
title: 'decode(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decodableattributedstringkey/decode(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/decodableattributedstringkey/decode(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decodableattributedstringkey/decode%28from%3A%29.json'
content_hash: 'sha256:20caaa26f2820b86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DecodableAttributedStringKey](../decodableattributedstringkey.md)

# decode(from:)

<sub>Type Method</sub>

Decodes a value from the provided decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decode(from decoder: any Decoder) throws -> Self.Value
```

## Parameters

- `decoder` — The decoder to read data from.

## Return Value

The decoded value.

## Discussion

This method throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Default Implementations

### DecodableAttributedStringKey Implementations

- [decode(from:)](<decode(from_)-1n7im.md>) — Decodes a Swift value from the provided decoder, using a default implementation.
- [decode(from:)](<decode(from_)-3yywq.md>) — Decodes an Objective-C value from the provided decoder, using a default implementation.
