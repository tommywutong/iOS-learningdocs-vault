---
title: 'tryContains(where:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/publisher-swift.struct/trycontains(where:)'
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct/trycontains(where:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct/trycontains%28where%3A%29.json'
content_hash: 'sha256:84af1a3274d72c16'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Result](../../result.md) · [Publisher](../publisher-swift.struct.md)

# tryContains(where:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryContains(where predicate: (Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher
```
