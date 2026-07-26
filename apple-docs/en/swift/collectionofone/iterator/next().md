---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectionofone/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/iterator/next%28%29.json'
content_hash: 'sha256:a6ecd44bcf6d365a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [CollectionOfOne](../../collectionofone.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Advances to the next element and returns it, or `nil` if no next element exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() -> Element?
```

## Return Value

The next element in the underlying sequence, if a next element exists; otherwise, `nil`.

## Discussion

Once `nil` has been returned, all subsequent calls return `nil`.
