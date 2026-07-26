---
title: 'init(from:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/init(from:)'
source_url: 'https://developer.apple.com/documentation/swift/int128/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/init%28from%3A%29.json'
content_hash: 'sha256:36e18300c20ab0cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# init(from:)

<sub>Initializer</sub>

Creates a new instance by decoding from the given decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — The decoder to read data from.

## Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.
