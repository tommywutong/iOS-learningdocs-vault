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
doc_path: '/documentation/swift/float80/init(exactly:)-5ggvi'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(exactly:)-5ggvi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28exactly%3A%29-5ggvi.json'
content_hash: 'sha256:5ef3b9a3f266739a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new value, if the given integer can be represented exactly.

<sub>macOS</sub>

```swift
init?<Source>(exactly value: Source) where Source : BinaryInteger
```

## Parameters

- `value` — The integer to convert to a floating-point value.

## Discussion

If the given integer cannot be represented exactly, the result is `nil`.
