---
title: 'mapAnnotations(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazysequence/mapannotations(_:)'
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/mapannotations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/mapannotations%28_%3A%29.json'
content_hash: 'sha256:dc5c9ae77fbfe21c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequence](../lazysequence.md)

# mapAnnotations(_:)

<sub>Instance Method</sub>

Returns a lazy sequence where the elements of the result are computed each time they are read by calling transform function on the annotation of an annotated feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mapAnnotations<Feature, Input, Output>(_ transform: @escaping (Input) -> Output) -> LazyMapSequence<Base, AnnotatedFeature<Feature, Output>> where Base.Element == AnnotatedFeature<Feature, Input>
```
