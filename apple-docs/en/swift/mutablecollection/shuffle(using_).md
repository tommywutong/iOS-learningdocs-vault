---
title: 'shuffle(using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablecollection/shuffle(using:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection/shuffle(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection/shuffle%28using%3A%29.json'
content_hash: 'sha256:3028bda3db8201c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableCollection](../mutablecollection.md)

# shuffle(using:)

<sub>Instance Method</sub>

Shuffles the collection in place, using the given generator as a source for randomness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func shuffle<T>(using generator: inout T) where T : RandomNumberGenerator
```

## Parameters

- `generator` — The random number generator to use when shuffling the collection.

## Discussion

You use this method to randomize the elements of a collection when you are using a custom random number generator. For example, you can use the `shuffle(using:)` method to randomly reorder the elements of an array.

```swift
var names = ["Alejandro", "Camila", "Diego", "Luciana", "Luis", "Sofía"]
names.shuffle(using: &myGenerator)
// names == ["Sofía", "Alejandro", "Camila", "Luis", "Diego", "Luciana"]
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

> [!note] Note
> The algorithm used to shuffle a collection may change in a future version of Swift. If you’re passing a generator that results in the same shuffled order each time you run your program, that sequence may change when your program is compiled using a different version of Swift.
