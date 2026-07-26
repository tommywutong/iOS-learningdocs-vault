---
title: 'withUnsafeTaggedBuffers(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/withunsafetaggedbuffers(_:)'
source_url: 'https://developer.apple.com/documentation/swift/array/withunsafetaggedbuffers(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/withunsafetaggedbuffers%28_%3A%29.json'
content_hash: 'sha256:8c58e7196b023ee5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# withUnsafeTaggedBuffers(_:)

<sub>Instance Method</sub>

Access the underlying CMTaggedBuffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeTaggedBuffers<R>(_ body: ([CMTaggedBuffer]) throws -> sending R) rethrows -> sending R where R : ~Copyable
```
