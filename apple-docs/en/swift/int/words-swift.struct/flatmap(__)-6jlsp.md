---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.1 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/int/words-swift.struct/flatmap(_:)-6jlsp'
source_url: 'https://developer.apple.com/documentation/swift/int/words-swift.struct/flatmap(_:)-6jlsp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/words-swift.struct/flatmap%28_%3A%29-6jlsp.json'
content_hash: 'sha256:d962ae2b3f684ea3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Int](../../int.md) · [Words](../words-swift.struct.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```
