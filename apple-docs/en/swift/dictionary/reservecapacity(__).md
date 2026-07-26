---
title: 'reserveCapacity(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/reservecapacity(_:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/reservecapacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/reservecapacity%28_%3A%29.json'
content_hash: 'sha256:8d651518ef7eec92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# reserveCapacity(_:)

<sub>Instance Method</sub>

Reserves enough space to store the specified number of key-value pairs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reserveCapacity(_ minimumCapacity: Int)
```

## Parameters

- `minimumCapacity` — The requested number of key-value pairs to store.

## Discussion

If you are adding a known number of key-value pairs to a dictionary, use this method to avoid multiple reallocations. This method ensures that the dictionary has unique, mutable, contiguous storage, with space allocated for at least the requested number of key-value pairs.

Calling the `reserveCapacity(_:)` method on a dictionary with bridged storage triggers a copy to contiguous storage even if the existing storage has room to store `minimumCapacity` key-value pairs.

## See Also

### Adding Keys and Values

- [updateValue(_:forKey:)](<updatevalue(__forkey_).md>) — Updates the value stored in the dictionary for the given key, or adds a new key-value pair if the key does not exist.
