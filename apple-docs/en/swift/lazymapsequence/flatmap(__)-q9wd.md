---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazymapsequence/flatmap(_:)-q9wd'
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/flatmap(_:)-q9wd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/flatmap%28_%3A%29-q9wd.json'
content_hash: 'sha256:5a2d2dd244158c6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyMapSequence](../lazymapsequence.md)

# flatMap(_:)

<sub>Instance Method</sub>

Returns the concatenated results of mapping the given transformation over this sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<SegmentOfResult>(_ transform: @escaping (Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>> where SegmentOfResult : Sequence
```

## Discussion

Use this method to receive a single-level sequence when your transformation produces a sequence or collection for each element. Calling `flatMap(_:)` on a sequence `s` is equivalent to calling `s.map(transform).joined()`.

> [!abstract] Complexity
> O(1)
