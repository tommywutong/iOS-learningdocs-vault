---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(exactly:)-2qxl0'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(exactly:)-2qxl0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28exactly%3A%29-2qxl0.json'
content_hash: 'sha256:a118cd62c23d7c15'
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
