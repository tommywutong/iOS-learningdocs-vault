---
title: 'init(floatLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/init(floatliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/double/init(floatliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/init%28floatliteral%3A%29.json'
content_hash: 'sha256:5a058544d813b6e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# init(floatLiteral:)

<sub>Initializer</sub>

Creates an instance initialized to the specified floating-point value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(floatLiteral value: Double)
```

## Parameters

- `value` — The value to create.

## Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using a floating-point literal. For example:

```swift
let x = 21.5
```

In this example, the assignment to the `x` constant calls this floating-point literal initializer behind the scenes.

## See Also

### Infrequently Used Functionality

- [init()](<init().md>)
- [init(integerLiteral:)](<init(integerliteral_).md>) — Creates an instance initialized to the specified integer value.
- [init(integerLiteral:)](<init(integerliteral_)-6hc7j.md>)
- [FloatLiteralType](floatliteraltype.md) — A type that represents a floating-point literal.
- [IntegerLiteralType](integerliteraltype.md) — A type that represents an integer literal.
- [advanced(by:)](<advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [distance(to:)](<distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [Stride](stride.md) — A type that represents the distance between two values.
- [write(to:)](<write(to_).md>) — Writes a textual representation of this instance into the given output stream.
- [hashValue](hashvalue.md) — The hash value.
