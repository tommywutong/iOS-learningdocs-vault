---
title: 'index(forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/index(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/index(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/index%28forkey%3A%29.json'
content_hash: 'sha256:162f8e6a0c513c31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# index(forKey:)

<sub>Instance Method</sub>

Returns the index for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(forKey key: Key) -> Dictionary<Key, Value>.Index?
```

## Parameters

- `key` — The key to find in the dictionary.

## Return Value

The index for `key` and its associated value if `key` is in the dictionary; otherwise, `nil`.

## Discussion

If the given key is found in the dictionary, this method returns an index into the dictionary that corresponds with the key-value pair.

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana", "JP": "Japan"]
let index = countryCodes.index(forKey: "JP")

print("Country code for \(countryCodes[index!].value): '\(countryCodes[index!].key)'.")
// Prints "Country code for Japan: 'JP'."
```

## See Also

### Accessing Keys and Values

- [subscript(_:)](<subscript(__)-8rfql.md>) — Accesses the value associated with the given key for reading and writing.
- [subscript(_:default:)](<subscript(__default_).md>) — Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [subscript(_:)](<subscript(__)-4bhoo.md>) — Accesses the key-value pair at the specified position.
- [keys](keys-swift.property.md) — A collection containing just the keys of the dictionary.
- [values](values-swift.property.md) — A collection containing just the values of the dictionary.
- [first](first.md) — The first element of the collection.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
