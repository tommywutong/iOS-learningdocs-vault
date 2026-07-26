---
title: 'min(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/publisher-swift.struct/min(by:)'
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct/min(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct/min%28by%3A%29.json'
content_hash: 'sha256:28d274f4b0bf049e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Result](../../result.md) · [Publisher](../publisher-swift.struct.md)

# min(by:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func min(by areInIncreasingOrder: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher
```
