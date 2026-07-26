---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/subscript(_:)-4bhoo'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/subscript(_:)-4bhoo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/subscript%28_%3A%29-4bhoo.json'
content_hash: 'sha256:bb7a6c5d8434a023'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the key-value pair at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element { get }
```

## Parameters

- `position` — The position of the key-value pair to access. `position` must be a valid index of the dictionary and not equal to `endIndex`.

## Return Value

A two-element tuple with the key and value corresponding to `position`.

## Overview

This subscript takes an index into the dictionary, instead of a key, and returns the corresponding key-value pair as a tuple. When performing collection-based operations that return an index into a dictionary, use this subscript with the resulting value.

For example, to find the key for a particular value in a dictionary, use the `firstIndex(where:)` method.

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana", "JP": "Japan"]
if let index = countryCodes.firstIndex(where: { $0.value == "Japan" }) {
    print(countryCodes[index])
    print("Japan's country code is '\(countryCodes[index].key)'.")
} else {
    print("Didn't find 'Japan' as a value in the dictionary.")
}
// Prints "(key: "JP", value: "Japan")"
// Prints "Japan's country code is 'JP'."
```

## See Also

### Accessing Keys and Values

- [subscript(_:)](<subscript(__)-8rfql.md>) — Accesses the value associated with the given key for reading and writing.
- [subscript(_:default:)](<subscript(__default_).md>) — Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [index(forKey:)](<index(forkey_).md>) — Returns the index for the given key.
- [keys](keys-swift.property.md) — A collection containing just the keys of the dictionary.
- [values](values-swift.property.md) — A collection containing just the values of the dictionary.
- [first](first.md) — The first element of the collection.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
