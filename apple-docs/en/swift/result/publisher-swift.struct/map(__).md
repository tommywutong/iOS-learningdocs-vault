---
title: 'map(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/publisher-swift.struct/map(_:)'
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct/map(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct/map%28_%3A%29.json'
content_hash: 'sha256:077167ee012cc7aa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Result](../../result.md) · [Publisher](../publisher-swift.struct.md)

# map(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func map<T>(_ transform: (Result<Success, Failure>.Publisher.Output) -> T) -> Result<T, Failure>.Publisher
```
