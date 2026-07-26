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
doc_path: /documentation/swift/discontiguousslice/popfirst()
source_url: 'https://developer.apple.com/documentation/swift/discontiguousslice/popfirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discontiguousslice/popfirst%28%29.json'
content_hash: 'sha256:839a9e8c3a10dcc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscontiguousSlice](../discontiguousslice.md)

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
