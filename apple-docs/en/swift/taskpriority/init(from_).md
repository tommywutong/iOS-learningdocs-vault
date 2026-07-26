---
title: 'init(from:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskpriority/init(from:)'
source_url: 'https://developer.apple.com/documentation/swift/taskpriority/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskpriority/init%28from%3A%29.json'
content_hash: 'sha256:2da962973b1c2ed6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskPriority](../taskpriority.md)

# init(from:)

<sub>Initializer</sub>

Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt8`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder` — The decoder to read data from.

## Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.
