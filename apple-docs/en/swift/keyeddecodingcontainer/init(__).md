---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainer/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/init%28_%3A%29.json'
content_hash: 'sha256:562b19cbd595cd6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance with the given container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Container>(_ container: Container) where K == Container.Key, Container : KeyedDecodingContainerProtocol
```

## Parameters

- `container` — The container to hold.
