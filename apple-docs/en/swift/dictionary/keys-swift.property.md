---
title: keys
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift 4.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/keys-swift.property
source_url: 'https://developer.apple.com/documentation/swift/dictionary/keys-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/keys-swift.property.json'
content_hash: 'sha256:5be4c0f11bf64723'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# keys

<sub>Instance Property</sub>

A collection containing just the keys of the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keys: Dictionary<Key, Value>.Keys { get }
```

## Discussion

When iterated over, keys appear in this collection in the same order as they occur in the dictionary’s key-value pairs. Each key in the keys collection has a unique value.

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana", "JP": "Japan"]
print(countryCodes)
// Prints "["BR": "Brazil", "JP": "Japan", "GH": "Ghana"]"

for k in countryCodes.keys {
    print(k)
}
// Prints "BR"
// Prints "JP"
// Prints "GH"
```

## See Also

### Accessing Keys and Values

- [subscript(_:)](<subscript(__)-8rfql.md>) — Accesses the value associated with the given key for reading and writing.
- [subscript(_:default:)](<subscript(__default_).md>) — Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [index(forKey:)](<index(forkey_).md>) — Returns the index for the given key.
- [subscript(_:)](<subscript(__)-4bhoo.md>) — Accesses the key-value pair at the specified position.
- [values](values-swift.property.md) — A collection containing just the values of the dictionary.
- [first](first.md) — The first element of the collection.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
