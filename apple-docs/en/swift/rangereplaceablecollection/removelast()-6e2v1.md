---
title: removeLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rangereplaceablecollection/removelast()-6e2v1
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/removelast()-6e2v1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/removelast%28%29-6e2v1.json'
content_hash: 'sha256:1d695e7b631a8b5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# removeLast()

<sub>Instance Method</sub>

Removes and returns the last element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeLast() -> Self.Element
```

## Return Value

The last element of the collection.

## Discussion

The collection must not be empty.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> [!abstract] Complexity
> O(1)
