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
doc_path: /documentation/swift/lazymapsequence/iterator/next()
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/iterator/next%28%29.json'
content_hash: 'sha256:4eb46687eda923fd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [LazyMapSequence](../../lazymapsequence.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Advances to the next element and returns it, or `nil` if no next element exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() -> Element?
```

## Discussion

Once `nil` has been returned, all subsequent calls return `nil`.

> [!info] Precondition
> `next()` has not been applied to a copy of `self` since the copy was made.
