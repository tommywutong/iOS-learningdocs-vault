---
title: reversed()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectionofone/reversed()
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/reversed()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/reversed%28%29.json'
content_hash: 'sha256:c70217ceb20d4c1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionOfOne](../collectionofone.md)

# reversed()

<sub>Instance Method</sub>

Returns a view presenting the elements of the collection in reverse order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reversed() -> ReversedCollection<Self>
```

## Discussion

You can reverse a collection without allocating new space for its elements by calling this `reversed()` method. A `ReversedCollection` instance wraps an underlying collection and provides access to its elements in reverse order. This example prints the characters of a string in reverse order:

```swift
let word = "Backwards"
for char in word.reversed() {
    print(char, terminator: "")
}
// Prints "sdrawkcaB"
```

If you need a reversed collection of the same type, you may be able to use the collection’s sequence-based or collection-based initializer. For example, to get the reversed version of a string, reverse its characters and initialize a new `String` instance from the result.

```swift
let reversedWord = String(word.reversed())
print(reversedWord)
// Prints "sdrawkcaB"
```

> [!abstract] Complexity
> O(1)
