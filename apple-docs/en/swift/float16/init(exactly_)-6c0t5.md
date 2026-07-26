---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(exactly:)-6c0t5'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(exactly:)-6c0t5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28exactly%3A%29-6c0t5.json'
content_hash: 'sha256:1f12e100088c6e12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new value, if the given integer can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<Source>(exactly value: Source) where Source : BinaryInteger
```

## Parameters

- `value` — The integer to convert to a floating-point value.

## Discussion

If the given integer cannot be represented exactly, the result is `nil`.
