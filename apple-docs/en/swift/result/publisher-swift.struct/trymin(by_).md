---
title: 'tryMin(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/publisher-swift.struct/trymin(by:)'
source_url: 'https://developer.apple.com/documentation/swift/result/publisher-swift.struct/trymin(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/publisher-swift.struct/trymin%28by%3A%29.json'
content_hash: 'sha256:aa3b04fd521e566f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Result](../../result.md) · [Publisher](../publisher-swift.struct.md)

# tryMin(by:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryMin(by areInIncreasingOrder: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, any Error>.Publisher
```
