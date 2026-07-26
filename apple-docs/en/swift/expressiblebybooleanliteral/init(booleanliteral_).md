---
title: 'init(booleanLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/expressiblebybooleanliteral/init(booleanliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/expressiblebybooleanliteral/init(booleanliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebybooleanliteral/init%28booleanliteral%3A%29.json'
content_hash: 'sha256:0d03e94e800ad8e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExpressibleByBooleanLiteral](../expressiblebybooleanliteral.md)

# init(booleanLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the given Boolean value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(booleanLiteral value: Self.BooleanLiteralType)
```

## Parameters

- `value` — The value of the new instance.

## Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using one of the Boolean literals `true` and `false`. For example:

```swift
let twasBrillig = true
```

In this example, the assignment to the `twasBrillig` constant calls this Boolean literal initializer behind the scenes.
