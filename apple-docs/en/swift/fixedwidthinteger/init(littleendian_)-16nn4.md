---
title: 'init(littleEndian:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/fixedwidthinteger/init(littleendian:)-16nn4'
source_url: 'https://developer.apple.com/documentation/swift/fixedwidthinteger/init(littleendian:)-16nn4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fixedwidthinteger/init%28littleendian%3A%29-16nn4.json'
content_hash: 'sha256:fc10f7db165862c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FixedWidthInteger](../fixedwidthinteger.md)

# init(littleEndian:)

<sub>Initializer</sub>

Creates an integer from its little-endian representation, changing the byte order if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(littleEndian value: Self)
```

## Parameters

- `value` — A value to use as the little-endian representation of the new integer.
