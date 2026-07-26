---
title: 'init(integerLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(integerliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(integerliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28integerliteral%3A%29.json'
content_hash: 'sha256:2a8cafed15e84ae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(integerLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the specified integer value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

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
