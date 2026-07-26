---
title: 'mapFeatures(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazysequence/mapfeatures(_:)'
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/mapfeatures(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/mapfeatures%28_%3A%29.json'
content_hash: 'sha256:9dd810abab3c0258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequence](../lazysequence.md)

# mapFeatures(_:)

<sub>Instance Method</sub>

Returns a lazy sequence where the elements of the result are computed each time they are read by calling transform function on the feature of an annotated feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mapFeatures<Input, Output, Annotation>(_ transform: @escaping (Input) -> Output) -> LazyMapSequence<Base, AnnotatedFeature<Output, Annotation>> where Base.Element == AnnotatedFeature<Input, Annotation>
```
