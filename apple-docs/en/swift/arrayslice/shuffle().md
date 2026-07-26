---
title: shuffle()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/arrayslice/shuffle()
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/shuffle()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/shuffle%28%29.json'
content_hash: 'sha256:04b691834c494b1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

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
