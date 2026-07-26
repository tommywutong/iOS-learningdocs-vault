---
title: 'init(arrayLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/init(arrayliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/array/init(arrayliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/init%28arrayliteral%3A%29.json'
content_hash: 'sha256:fb89152042628d73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# init(arrayLiteral:)

<sub>Initializer</sub>

Creates an array from the given array literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(arrayLiteral elements: Element...)
```

## Parameters

- `elements` — A variadic list of elements of the new array.

## Discussion

Do not call this initializer directly. It is used by the compiler when you use an array literal. Instead, create a new array by using an array literal as its value. To do this, enclose a comma-separated list of values in square brackets.

Here, an array of strings is created from an array literal holding only strings.

```swift
let ingredients = ["cocoa beans", "sugar", "cocoa butter", "salt"]
```

## See Also

### Infrequently Used Functionality

- [hashValue](hashvalue.md) — The hash value.
