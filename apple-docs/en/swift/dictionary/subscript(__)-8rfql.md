---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/subscript(_:)-8rfql'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/subscript(_:)-8rfql'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/subscript%28_%3A%29-8rfql.json'
content_hash: 'sha256:81208b21adc46027'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the value associated with the given key for reading and writing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(key: Key) -> Value? { get set }
```

## Parameters

- `key` — The key to find in the dictionary.

## Return Value

The value associated with `key` if `key` is in the dictionary; otherwise, `nil`.

## Overview

This _key-based_ subscript returns the value for the given key if the key is found in the dictionary, or `nil` if the key is not found.

The following example creates a new dictionary and prints the value of a key found in the dictionary (`"Coral"`) and a key not found in the dictionary (`"Cerise"`).

```swift
var hues = ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156]
print(hues["Coral"])
// Prints "Optional(16)"
print(hues["Cerise"])
// Prints "nil"
```

When you assign a value for a key and that key already exists, the dictionary overwrites the existing value. If the dictionary doesn’t contain the key, the key and value are added as a new key-value pair.

Here, the value for the key `"Coral"` is updated from `16` to `18` and a new key-value pair is added for the key `"Cerise"`.

```swift
hues["Coral"] = 18
print(hues["Coral"])
// Prints "Optional(18)"

hues["Cerise"] = 330
print(hues["Cerise"])
// Prints "Optional(330)"
```

If you assign `nil` as the value for the given key, the dictionary removes that key and its associated value.

In the following example, the key-value pair for the key `"Aquamarine"` is removed from the dictionary by assigning `nil` to the key-based subscript.

```swift
hues["Aquamarine"] = nil
print(hues)
// Prints "["Coral": 18, "Heliotrope": 296, "Cerise": 330]"
```

## See Also

### Accessing Keys and Values

- [subscript(_:default:)](<subscript(__default_).md>) — Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [index(forKey:)](<index(forkey_).md>) — Returns the index for the given key.
- [subscript(_:)](<subscript(__)-4bhoo.md>) — Accesses the key-value pair at the specified position.
- [keys](keys-swift.property.md) — A collection containing just the keys of the dictionary.
- [values](values-swift.property.md) — A collection containing just the values of the dictionary.
- [first](first.md) — The first element of the collection.
- [randomElement()](<randomelement().md>) — Returns a random element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
