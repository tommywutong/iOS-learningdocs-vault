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
doc_path: '/documentation/swift/float16/init(exactly:)-d42j'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(exactly:)-d42j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28exactly%3A%29-d42j.json'
content_hash: 'sha256:b0380e47c8efbd24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance from the given value, if it can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<Source>(exactly value: Source) where Source : BinaryFloatingPoint
```

## Parameters

- `value` — A floating-point value to be converted.

## Discussion

If the given floating-point value cannot be represented exactly, the result is `nil`.
