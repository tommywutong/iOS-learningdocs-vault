---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazymapsequence/map(_:)-2qa3r'
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/map(_:)-2qa3r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/map%28_%3A%29-2qa3r.json'
content_hash: 'sha256:5897167c5fc70a08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyMapSequence](../lazymapsequence.md)

# map(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<ElementOfResult>(_ transform: @escaping (Element) -> ElementOfResult) -> LazyMapSequence<Base, ElementOfResult>
```
