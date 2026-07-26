---
title: last
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/last
source_url: 'https://developer.apple.com/documentation/swift/string/last'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/last.json'
content_hash: 'sha256:3f0940123cf65fe6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# last

<sub>Instance Property</sub>

The last element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var last: Self.Element? { get }
```

## Discussion

If the collection is empty, the value of this property is `nil`.

```swift
let numbers = [10, 20, 30, 40, 50]
if let lastNumber = numbers.last {
    print(lastNumber)
}
// Prints "50"
```

> [!abstract] Complexity
> O(1)

## See Also

### Getting Characters and Bytes

- [subscript(_:)](<subscript(__)-lc0v.md>) — Accesses the character at the given position.
- [first](first.md) — The first element of the collection.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
