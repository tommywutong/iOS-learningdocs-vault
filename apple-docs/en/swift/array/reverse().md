---
title: reverse()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/reverse()
source_url: 'https://developer.apple.com/documentation/swift/array/reverse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/reverse%28%29.json'
content_hash: 'sha256:37d4609796daabee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# reverse()

<sub>Instance Method</sub>

Reverses the elements of the collection in place.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reverse()
```

## Discussion

The following example reverses the elements of an array of characters:

```swift
var characters: [Character] = ["C", "a", "f", "é"]
characters.reverse()
print(characters)
// Prints "["é", "f", "a", "C"]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the number of elements in the collection.

## See Also

### Reordering an Array’s Elements

- [sort()](<sort().md>) — Sorts the collection in place.
- [sort(by:)](<sort(by_).md>) — Sorts the collection in place, using the given predicate as the comparison between elements.
- [sorted()](<sorted().md>) — Returns the elements of the sequence, sorted.
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [reversed()](<reversed().md>) — Returns a view presenting the elements of the collection in reverse order.
- [shuffle()](<shuffle().md>) — Shuffles the collection in place.
- [shuffle(using:)](<shuffle(using_).md>) — Shuffles the collection in place, using the given generator as a source for randomness.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [partition(by:)](<partition(by_)-90po8.md>) — Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [swapAt(_:_:)](<swapat(____).md>) — Exchanges the values at the specified indices of the collection.
