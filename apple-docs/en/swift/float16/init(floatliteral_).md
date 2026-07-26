---
title: 'init(floatLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(floatliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(floatliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28floatliteral%3A%29.json'
content_hash: 'sha256:8f62075627b044cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(floatLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the specified floating-point value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(floatLiteral value: Float16)
```

## Parameters

- `value` — The value to create.

## Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using a floating-point literal. For example:

```swift
let x = 21.5
```

In this example, the assignment to the `x` constant calls this floating-point literal initializer behind the scenes.
