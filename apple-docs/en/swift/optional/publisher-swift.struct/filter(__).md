---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/publisher-swift.struct/filter(_:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/publisher-swift.struct/filter%28_%3A%29.json'
content_hash: 'sha256:c9055a55e2adee78'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Optional](../../optional.md) · [Publisher](../publisher-swift.struct.md)

# filter(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(_ isIncluded: (Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher
```
