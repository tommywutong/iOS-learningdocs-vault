---
title: randomElement()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/randomelement()
source_url: 'https://developer.apple.com/documentation/swift/dictionary/randomelement()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/randomelement%28%29.json'
content_hash: 'sha256:ec0a718a84b38d8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# randomElement()

<sub>Instance Method</sub>

Returns a random element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func randomElement() -> Self.Element?
```

## Return Value

A random element from the collection. If the collection is empty, the method returns `nil`.

## Discussion

Call `randomElement()` to select a random element from an array or another collection. This example picks a name at random from an array:

```swift
let names = ["Zoey", "Chloe", "Amani", "Amaia"]
let randomName = names.randomElement()!
// randomName == "Amani"
```

This method is equivalent to calling `randomElement(using:)`, passing in the system’s default random generator.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.

## See Also

### Accessing Keys and Values

- [subscript(_:)](<subscript(__)-8rfql.md>) — Accesses the value associated with the given key for reading and writing.
- [subscript(_:default:)](<subscript(__default_).md>) — Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [index(forKey:)](<index(forkey_).md>) — Returns the index for the given key.
- [subscript(_:)](<subscript(__)-4bhoo.md>) — Accesses the key-value pair at the specified position.
- [keys](keys-swift.property.md) — A collection containing just the keys of the dictionary.
- [values](values-swift.property.md) — A collection containing just the values of the dictionary.
- [first](first.md) — The first element of the collection.
- [randomElement(using:)](<randomelement(using_).md>) — Returns a random element of the collection, using the given generator as a source for randomness.
