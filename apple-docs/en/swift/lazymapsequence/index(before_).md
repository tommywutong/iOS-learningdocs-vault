---
title: 'index(before:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazymapsequence/index(before:)'
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/index(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/index%28before%3A%29.json'
content_hash: 'sha256:015686542f271f93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyMapSequence](../lazymapsequence.md)

# index(before:)

<sub>Instance Method</sub>

A value less than or equal to the number of elements in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(before i: LazyMapSequence<Base, Element>.Index) -> LazyMapSequence<Base, Element>.Index
```

## Discussion

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.
