---
title: popFirst()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anybidirectionalcollection/popfirst()
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/popfirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/popfirst%28%29.json'
content_hash: 'sha256:5ce4aa2464c2a19b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# popFirst()

<sub>Instance Method</sub>

Removes and returns the first element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func popFirst() -> Self.Element?
```

## Return Value

The first element of the collection if the collection is not empty; otherwise, `nil`.

## Discussion

> [!abstract] Complexity
> O(1)
