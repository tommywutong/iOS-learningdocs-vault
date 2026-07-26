---
title: 'init(integerLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/expressiblebyintegerliteral/init(integerliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyintegerliteral/init(integerliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyintegerliteral/init%28integerliteral%3A%29.json'
content_hash: 'sha256:386a98c7ab82e43c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExpressibleByIntegerLiteral](../expressiblebyintegerliteral.md)

# init(integerLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the specified integer value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(integerLiteral value: Self.IntegerLiteralType)
```

## Parameters

- `value` — The value to create.

## Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using an integer literal. For example:

```swift
let x = 23
```

In this example, the assignment to the `x` constant calls this integer literal initializer behind the scenes.

## Default Implementations

### ExpressibleByIntegerLiteral Implementations

- [init(integerLiteral:)](<init(integerliteral_)-88n2x.md>)
