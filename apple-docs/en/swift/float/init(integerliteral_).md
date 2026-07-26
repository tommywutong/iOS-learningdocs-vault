---
title: 'init(integerLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/init(integerliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/float/init(integerliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28integerliteral%3A%29.json'
content_hash: 'sha256:9d95fa992f986950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

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

## See Also

### Infrequently Used Functionality

- [init()](<init().md>)
- [init(floatLiteral:)](<init(floatliteral_).md>) — Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral:)](<init(integerliteral_)-6hc7h.md>)
- [advanced(by:)](<advanced(by_).md>) — Returns a value that is offset the specified distance from this value.
- [distance(to:)](<distance(to_).md>) — Returns the distance from this value to the given value, expressed as a stride.
- [write(to:)](<write(to_).md>) — Writes a textual representation of this instance into the given output stream.
