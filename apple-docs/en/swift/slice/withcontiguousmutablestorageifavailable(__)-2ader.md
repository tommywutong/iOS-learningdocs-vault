---
title: 'withContiguousMutableStorageIfAvailable(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/withcontiguousmutablestorageifavailable(_:)-2ader'
source_url: 'https://developer.apple.com/documentation/swift/slice/withcontiguousmutablestorageifavailable(_:)-2ader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/withcontiguousmutablestorageifavailable%28_%3A%29-2ader.json'
content_hash: 'sha256:65cc4dd0d885a2f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# withContiguousMutableStorageIfAvailable(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withContiguousMutableStorageIfAvailable<R, Element>(_ body: (inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R? where Base == UnsafeMutableBufferPointer<Element>
```
