---
title: 'init(floatLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/init(floatliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(floatliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28floatliteral%3A%29.json'
content_hash: 'sha256:f42c4ea25be52a00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(floatLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the specified floating-point value.

<sub>macOS</sub>

```swift
init(floatLiteral value: Float80)
```

## Parameters

- `value` — The value to create.

## Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using a floating-point literal. For example:

```swift
let x = 21.5
```

In this example, the assignment to the `x` constant calls this floating-point literal initializer behind the scenes.
