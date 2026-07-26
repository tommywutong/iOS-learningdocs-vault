---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/init(exactly:)-9oml5'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(exactly:)-9oml5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28exactly%3A%29-9oml5.json'
content_hash: 'sha256:d053db58a255a042'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance from the given value, if it can be represented exactly.

<sub>macOS</sub>

```swift
init?<Source>(exactly value: Source) where Source : BinaryFloatingPoint
```

## Parameters

- `value` — A floating-point value to be converted.

## Discussion

If the given floating-point value cannot be represented exactly, the result is `nil`.
