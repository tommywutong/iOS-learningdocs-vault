---
title: 'init(createPublisher:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/deferred/init(createpublisher:)'
source_url: 'https://developer.apple.com/documentation/combine/deferred/init(createpublisher:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/deferred/init%28createpublisher%3A%29.json'
content_hash: 'sha256:06c369f11ea04169'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Deferred](../deferred.md)

# init(createPublisher:)

<sub>Initializer</sub>

Creates a deferred publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(createPublisher: @escaping () -> DeferredPublisher)
```

## Parameters

- `createPublisher` — The closure to execute when calling `subscribe(_:)`.
