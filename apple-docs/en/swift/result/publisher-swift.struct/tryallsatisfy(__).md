---
title: 'tryAllSatisfy(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/publisher-swift.struct/tryallsatisfy(_:)'
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct/tryallsatisfy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct/tryallsatisfy%28_%3A%29.json'
content_hash: 'sha256:44dc31b2495d9d3d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Result](../../result.md) · [Publisher](../publisher-swift.struct.md)

# tryAllSatisfy(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryAllSatisfy(_ predicate: (Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher
```
