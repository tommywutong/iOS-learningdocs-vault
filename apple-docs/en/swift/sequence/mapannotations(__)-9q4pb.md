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
doc_path: '/documentation/swift/sequence/mapannotations(_:)-9q4pb'
source_url: 'https://developer.apple.com/documentation/swift/sequence/mapannotations(_:)-9q4pb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/mapannotations%28_%3A%29-9q4pb.json'
content_hash: 'sha256:64b407c64371695c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# mapAnnotations(_:)

<sub>Instance Method</sub>

Returns an array containing the results of mapping the given closure over the sequence’s annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mapAnnotations<Feature, Input, Output>(_ transform: (Input) throws -> Output) rethrows -> [AnnotatedFeature<Feature, Output>] where Self.Element == AnnotatedFeature<Feature, Input>
```
