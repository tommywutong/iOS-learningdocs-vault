---
title: 'init(nilLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/init(nilliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/init(nilliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/init%28nilliteral%3A%29.json'
content_hash: 'sha256:aece887c6a7c4afe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# init(nilLiteral:)

<sub>Initializer</sub>

Creates an instance initialized with `nil`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(nilLiteral: ())
```

## Discussion

Do not call this initializer directly. It is used by the compiler when you initialize an `Optional` instance with a `nil` literal. For example:

```swift
var i: Index? = nil
```

In this example, the assignment to the `i` variable calls this initializer behind the scenes.

## See Also

### Creating a Nil Value

- [Optional.none](none.md) — The absence of a value.
