---
title: 'dropFirst(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncdropfirstsequence/dropfirst(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncdropfirstsequence/dropfirst(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncdropfirstsequence/dropfirst%28_%3A%29.json'
content_hash: 'sha256:d41a0f38e439e891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncDropFirstSequence](../asyncdropfirstsequence.md)

# dropFirst(_:)

<sub>Instance Method</sub>

Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropFirst(_ count: Int = 1) -> AsyncDropFirstSequence<Base>
```

## Discussion

When you call `dropFirst(_:)` on an asynchronous sequence that is already an `AsyncDropFirstSequence`, the returned sequence simply adds the new drop count to the current drop count.
