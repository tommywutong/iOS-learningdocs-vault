---
title: makeIterator()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/makeiterator()
source_url: 'https://developer.apple.com/documentation/swift/dictionary/makeiterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/makeiterator%28%29.json'
content_hash: 'sha256:b81e3fee46b0e520'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# makeIterator()

<sub>Instance Method</sub>

Returns an iterator over the dictionary’s key-value pairs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeIterator() -> Dictionary<Key, Value>.Iterator
```

## Return Value

An iterator over the dictionary with elements of type `(key: Key, value: Value)`.

## Discussion

Iterating over a dictionary yields the key-value pairs as two-element tuples. You can decompose the tuple in a `for`-`in` loop, which calls `makeIterator()` behind the scenes, or when calling the iterator’s `next()` method directly.

```swift
let hues = ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156]
for (name, hueValue) in hues {
    print("The hue of \(name) is \(hueValue).")
}
// Prints "The hue of Heliotrope is 296."
// Prints "The hue of Coral is 16."
// Prints "The hue of Aquamarine is 156."
```

## See Also

### Iterating over Keys and Values

- [forEach(_:)](<foreach(__).md>) — Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [enumerated()](<enumerated().md>) — Returns a sequence of pairs (_n_, _x_), where _n_ represents a consecutive integer starting at zero and _x_ represents an element of the sequence.
- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [underestimatedCount](underestimatedcount.md) — A value less than or equal to the number of elements in the collection.
