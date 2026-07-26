---
title: 'init(from:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/init(from:)'
source_url: 'https://developer.apple.com/documentation/swift/array/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/init%28from%3A%29.json'
content_hash: 'sha256:0a76c982ae53e243'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# init(from:)

<sub>Initializer</sub>

Creates a new array by decoding from the given decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — The decoder to read data from.

## Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## See Also

### Encoding and Decoding

- [encode(to:)](<encode(to_).md>) — Encodes the elements of this array into the given encoder in an unkeyed container.
