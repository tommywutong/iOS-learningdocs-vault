---
title: 'receive(subscriber:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/publisher-swift.struct/receive(subscriber:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/receive(subscriber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/publisher-swift.struct/receive%28subscriber%3A%29.json'
content_hash: 'sha256:94ff2472d5091f01'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Optional](../../optional.md) · [Publisher](../publisher-swift.struct.md)

# receive(subscriber:)

<sub>Instance Method</sub>

Implements the Publisher protocol by accepting the subscriber and immediately publishing the optional’s value if it has one, or finishing normally if it doesn’t.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive<S>(subscriber: S) where Wrapped == S.Input, S : Subscriber, S.Failure == Never
```

## Parameters

- `subscriber` — The subscriber to add.
