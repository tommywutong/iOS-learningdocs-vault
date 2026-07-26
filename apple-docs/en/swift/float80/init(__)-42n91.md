---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/init(_:)-42n91'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(_:)-42n91'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28_%3A%29-42n91.json'
content_hash: 'sha256:bd6c19245c099d2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(_:)

<sub>Initializer</sub>

Creates a new value, rounded to the closest possible representation.

<sub>macOS</sub>

```swift
init(_ v: Int)
```

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.
