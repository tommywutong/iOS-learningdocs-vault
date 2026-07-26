---
title: removeFirst()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/emptycollection/removefirst()
source_url: 'https://developer.apple.com/documentation/swift/emptycollection/removefirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/emptycollection/removefirst%28%29.json'
content_hash: 'sha256:60e794b4defc3ab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EmptyCollection](../emptycollection.md)

# removeFirst()

<sub>Instance Method</sub>

Removes and returns the first element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeFirst() -> Self.Element
```

## Return Value

The first element of the collection.

## Discussion

The collection must not be empty.

> [!abstract] Complexity
> O(1)
