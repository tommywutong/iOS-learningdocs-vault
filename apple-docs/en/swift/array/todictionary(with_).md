---
title: 'toDictionary(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/todictionary(with:)'
source_url: 'https://developer.apple.com/documentation/swift/array/todictionary(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/todictionary%28with%3A%29.json'
content_hash: 'sha256:ca08a1a3d1c30d53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# toDictionary(with:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func toDictionary<Key>(with selectKey: (Element) -> Key) -> [Key : Element] where Key : Hashable
```
