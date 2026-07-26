---
title: shuffle()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/shuffle()
source_url: 'https://developer.apple.com/documentation/swift/array/shuffle()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/shuffle%28%29.json'
content_hash: 'sha256:7f68c3047c3e13a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# shuffle()

<sub>Instance Method</sub>

Shuffles the collection in place.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func shuffle()
```

## Discussion

Use the `shuffle()` method to randomly reorder the elements of an array.

```swift
var names = ["Alejandro", "Camila", "Diego", "Luciana", "Luis", "Sofía"]
names.shuffle()
// names == ["Luis", "Camila", "Luciana", "Sofía", "Alejandro", "Diego"]
```

This method is equivalent to calling `shuffle(using:)`, passing in the system’s default random generator.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

## See Also

### Reordering an Array’s Elements

- [sort()](<sort().md>) — Sorts the collection in place.
- [sort(by:)](<sort(by_).md>) — Sorts the collection in place, using the given predicate as the comparison between elements.
- [sorted()](<sorted().md>) — Returns the elements of the sequence, sorted.
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [reverse()](<reverse().md>) — Reverses the elements of the collection in place.
- [reversed()](<reversed().md>) — Returns a view presenting the elements of the collection in reverse order.
- [shuffle(using:)](<shuffle(using_).md>) — Shuffles the collection in place, using the given generator as a source for randomness.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [partition(by:)](<partition(by_)-90po8.md>) — Reorders the elements of the collection such that all the elements that match the given predicate are after all the elements that don’t match.
- [swapAt(_:_:)](<swapat(____).md>) — Exchanges the values at the specified indices of the collection.
