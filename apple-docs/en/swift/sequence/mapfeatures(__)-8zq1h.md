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
doc_path: '/documentation/swift/sequence/mapfeatures(_:)-8zq1h'
source_url: 'https://developer.apple.com/documentation/swift/sequence/mapfeatures(_:)-8zq1h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/mapfeatures%28_%3A%29-8zq1h.json'
content_hash: 'sha256:b0f77de088224b1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# mapFeatures(_:)

<sub>Instance Method</sub>

Returns an array containing the results of mapping the given closure over the sequence’s features.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mapFeatures<Input, Output, Annotation>(_ transform: (Input) throws -> Output) rethrows -> [AnnotatedFeature<Output, Annotation>] where Self.Element == AnnotatedFeature<Input, Annotation>
```
