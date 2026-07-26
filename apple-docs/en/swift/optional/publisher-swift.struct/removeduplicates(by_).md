---
title: 'removeDuplicates(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/publisher-swift.struct/removeduplicates(by:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/removeduplicates(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/publisher-swift.struct/removeduplicates%28by%3A%29.json'
content_hash: 'sha256:5be6fc69af7e21bf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Optional](../../optional.md) · [Publisher](../publisher-swift.struct.md)

# removeDuplicates(by:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeDuplicates(by predicate: (Optional<Wrapped>.Publisher.Output, Optional<Wrapped>.Publisher.Output) -> Bool) -> Optional<Wrapped>.Publisher
```
