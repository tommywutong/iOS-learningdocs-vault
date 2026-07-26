---
title: 'init(floatLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/expressiblebyfloatliteral/init(floatliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyfloatliteral/init(floatliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyfloatliteral/init%28floatliteral%3A%29.json'
content_hash: 'sha256:a141cd10b538f2d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExpressibleByFloatLiteral](../expressiblebyfloatliteral.md)

# init(floatLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the specified floating-point value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(floatLiteral value: Self.FloatLiteralType)
```

## Parameters

- `value` — The value to create.

## Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using a floating-point literal. For example:

```swift
let x = 21.5
```

In this example, the assignment to the `x` constant calls this floating-point literal initializer behind the scenes.
