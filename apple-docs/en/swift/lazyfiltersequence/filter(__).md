---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazyfiltersequence/filter(_:)'
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/filter%28_%3A%29.json'
content_hash: 'sha256:b4474541d0a94c29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# filter(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(_ isIncluded: @escaping (LazyFilterSequence<Base>.Element) -> Bool) -> LazyFilterSequence<Base>
```
