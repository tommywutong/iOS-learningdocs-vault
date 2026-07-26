---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/publisher-swift.struct/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/publisher-swift.struct/init%28_%3A%29.json'
content_hash: 'sha256:c6c66accf25daa36'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Optional](../../optional.md) · [Publisher](../publisher-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a publisher to emit the value of the optional, or to finish immediately if the optional doesn’t have a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ output: Optional<Wrapped>.Publisher.Output?)
```

## Parameters

- `output` — The result to deliver to each subscriber.
