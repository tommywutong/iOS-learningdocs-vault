---
title: 'init(integerLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/init(integerliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(integerliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28integerliteral%3A%29.json'
content_hash: 'sha256:b856fe5ca96f3d0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(integerLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the specified integer value.

<sub>macOS</sub>

```swift
init(integerLiteral value: Int64)
```

## Parameters

- `value` — The value to create.

## Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using an integer literal. For example:

```swift
let x = 23
```

In this example, the assignment to the `x` constant calls this integer literal initializer behind the scenes.
