---
title: 'replaceError(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/publisher-swift.struct/replaceerror(with:)'
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct/replaceerror(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct/replaceerror%28with%3A%29.json'
content_hash: 'sha256:936f4ddb413fcd55'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Result](../../result.md) · [Publisher](../publisher-swift.struct.md)

# replaceError(with:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceError(with output: Result<Success, Failure>.Publisher.Output) -> Result<Result<Success, Failure>.Publisher.Output, Never>.Publisher
```
