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
doc_path: /documentation/swift/dictionary/first
source_url: 'https://developer.apple.com/documentation/swift/dictionary/first'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/first.json'
content_hash: 'sha256:4c22c014cea9f85f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

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

### Accessing Keys and Values

- [subscript(_:)](<subscript(__)-8rfql.md>) — Accesses the value associated with the given key for reading and writing.
- [subscript(_:default:)](<subscript(__default_).md>) — Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [index(forKey:)](<index(forkey_).md>) — Returns the index for the given key.
- [subscript(_:)](<subscript(__)-4bhoo.md>) — Accesses the key-value pair at the specified position.
- [keys](keys-swift.property.md) — A collection containing just the keys of the dictionary.
- [values](values-swift.property.md) — A collection containing just the values of the dictionary.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
