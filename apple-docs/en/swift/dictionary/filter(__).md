---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift 4.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/filter(_:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/filter%28_%3A%29.json'
content_hash: 'sha256:32034b0a5839b742'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# filter(_:)

<sub>Instance Method</sub>

Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func filter<E>(_ isIncluded: (Dictionary<Key, Value>.Element) throws(E) -> Bool) throws(E) -> [Key : Value] where E : Error
```

## Parameters

- `isIncluded` — A closure that takes a key-value pair as its argument and returns a Boolean value indicating whether the pair should be included in the returned dictionary.

## Return Value

A dictionary of the key-value pairs that `isIncluded` allows.

## See Also

### Removing Keys and Values

- [removeValue(forKey:)](<removevalue(forkey_).md>) — Removes the given key and its associated value from the dictionary.
- [remove(at:)](<remove(at_).md>) — Removes and returns the key-value pair at the specified index.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all key-value pairs from the dictionary.
