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
doc_path: '/documentation/swift/float80/init(exactly:)-2t92j'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(exactly:)-2t92j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28exactly%3A%29-2t92j.json'
content_hash: 'sha256:26af23b70a62a164'
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
