---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.1 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/int64/words-swift.struct/flatmap(_:)-5ogxw'
source_url: 'https://developer.apple.com/documentation/swift/int64/words-swift.struct/flatmap(_:)-5ogxw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int64/words-swift.struct/flatmap%28_%3A%29-5ogxw.json'
content_hash: 'sha256:baf68b58987c0443'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Int64](../../int64.md) · [Words](../words-swift.struct.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
