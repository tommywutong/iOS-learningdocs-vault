---
title: 'init(arrayLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/expressiblebyarrayliteral/init(arrayliteral:)-q0d7'
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyarrayliteral/init(arrayliteral:)-q0d7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyarrayliteral/init%28arrayliteral%3A%29-q0d7.json'
content_hash: 'sha256:1ff9360aabdd8e6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExpressibleByArrayLiteral](../expressiblebyarrayliteral.md)

# init(arrayLiteral:)

<sub>Initializer</sub>

Creates a set containing the elements of the given array literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(arrayLiteral: Self.Element...)
```

## Parameters

- `arrayLiteral` — A list of elements of the new set.

## Discussion

Do not call this initializer directly. It is used by the compiler when you use an array literal. Instead, create a new set using an array literal as its value by enclosing a comma-separated list of values in square brackets. You can use an array literal anywhere a set is expected by the type context.

Here, a set of strings is created from an array literal holding only strings:

```swift
let ingredients: Set = ["cocoa beans", "sugar", "cocoa butter", "salt"]
if ingredients.isSuperset(of: ["sugar", "salt"]) {
    print("Whatever it is, it's bound to be delicious!")
}
// Prints "Whatever it is, it's bound to be delicious!"
```
