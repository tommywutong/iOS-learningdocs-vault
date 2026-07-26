---
title: 'encode(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/encode(to:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/encode%28to%3A%29.json'
content_hash: 'sha256:67f1c0af6ad03864'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# encode(to:)

<sub>Instance Method</sub>

Encodes the contents of this dictionary into the given encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## Parameters

- `encoder` — The encoder to write data to.

## Discussion

If the dictionary uses keys that are `String`, `Int`, or a type conforming to `CodingKeyRepresentable`, the contents are encoded in a keyed container. Otherwise, the contents are encoded as alternating key-value pairs in an unkeyed container.

This function throws an error if any values are invalid for the given encoder’s format.

## See Also

### Encoding and Decoding

- [init(from:)](<init(from_)-6e6js.md>) — Creates a new dictionary by decoding from the given decoder.
