---
title: 'removeAll(keepingCapacity:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/removeall(keepingcapacity:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/removeall(keepingcapacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/removeall%28keepingcapacity%3A%29.json'
content_hash: 'sha256:a05c1fb699bd2096'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# removeAll(keepingCapacity:)

<sub>Instance Method</sub>

Removes all key-value pairs from the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeAll(keepingCapacity keepCapacity: Bool = false)
```

## Parameters

- `keepCapacity` — Whether the dictionary should keep its underlying buffer. If you pass `true`, the operation preserves the buffer capacity that the collection has, otherwise the underlying buffer is released.  The default is `false`.

## Discussion

Calling this method invalidates all indices with respect to the dictionary.

> [!abstract] Complexity
> O(_n_), where _n_ is the number of key-value pairs in the dictionary.

## See Also

### Removing Keys and Values

- [filter(_:)](<filter(__).md>) — Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.
- [removeValue(forKey:)](<removevalue(forkey_).md>) — Removes the given key and its associated value from the dictionary.
- [remove(at:)](<remove(at_).md>) — Removes and returns the key-value pair at the specified index.
