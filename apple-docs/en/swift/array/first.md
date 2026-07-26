---
title: first
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/first
source_url: 'https://developer.apple.com/documentation/swift/array/first'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/first.json'
content_hash: 'sha256:ed0bf3b1a5a921bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# first

<sub>Instance Property</sub>

The first element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var first: Self.Element? { get }
```

## Discussion

If the collection is empty, the value of this property is `nil`.

```swift
let numbers = [10, 20, 30, 40, 50]
if let firstNumber = numbers.first {
    print(firstNumber)
}
// Prints "10"
```

## See Also

### Accessing Elements

- [subscript(_:)](<subscript(__)-25iat.md>) — Accesses the element at the specified position.
- [last](last.md) — The last element of the collection.
- [subscript(_:)](<subscript(__)-53fvb.md>) — Accesses a contiguous subrange of the array’s elements.
- [subscript(_:)](<subscript(__)-3kwny.md>)
- [subscript(_:)](<subscript(__)-4h7rl.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-3pmfg.md>)
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
