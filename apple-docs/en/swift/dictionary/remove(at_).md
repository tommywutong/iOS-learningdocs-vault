---
title: 'remove(at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/remove(at:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/remove(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/remove%28at%3A%29.json'
content_hash: 'sha256:95fa5fd0d3b5b834'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# remove(at:)

<sub>Instance Method</sub>

Removes and returns the key-value pair at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(at index: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element
```

## Parameters

- `index` — The position of the key-value pair to remove. `index` must be a valid index of the dictionary, and must not equal the dictionary’s end index.

## Return Value

The key-value pair that correspond to `index`.

## Discussion

Calling this method invalidates any existing indices for use with this dictionary.

> [!abstract] Complexity
> O(_n_), where _n_ is the number of key-value pairs in the dictionary.

## See Also

### Removing Keys and Values

- [filter(_:)](<filter(__).md>) — Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.
- [removeValue(forKey:)](<removevalue(forkey_).md>) — Removes the given key and its associated value from the dictionary.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all key-value pairs from the dictionary.
