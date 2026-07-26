---
title: 'init(_:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/asyncthrowingpublisher/init(_:)'
source_url: 'https://developer.apple.com/documentation/combine/asyncthrowingpublisher/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/asyncthrowingpublisher/init%28_%3A%29.json'
content_hash: 'sha256:256e1551cebb0b3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [AsyncThrowingPublisher](../asyncthrowingpublisher.md)

# init(_:)

<sub>Initializer</sub>

Creates a publisher that exposes elements received from an upstream publisher as a throwing asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ publisher: P)
```

## Parameters

- `publisher` — An upstream publisher. The asynchronous publisher converts elements received from this publisher into an asynchronous sequence.
