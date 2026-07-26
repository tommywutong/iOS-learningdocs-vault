---
title: 'output(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/publisher-swift.struct/output(in:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/output(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/publisher-swift.struct/output%28in%3A%29.json'
content_hash: 'sha256:5e94b6a5059bdabb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Optional](../../optional.md) · [Publisher](../publisher-swift.struct.md)

# output(in:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func output<R>(in range: R) -> Optional<Wrapped>.Publisher where R : RangeExpression, R.Bound == Int
```
