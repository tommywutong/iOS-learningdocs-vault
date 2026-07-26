---
title: connect()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/connectablepublisher/connect()
source_url: 'https://developer.apple.com/documentation/combine/connectablepublisher/connect()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/connectablepublisher/connect%28%29.json'
content_hash: 'sha256:d62e808b8d84361a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [ConnectablePublisher](../connectablepublisher.md)

# connect()

<sub>Instance Method</sub>

Connects to the publisher, allowing it to produce elements, and returns an instance with which to cancel publishing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func connect() -> any Cancellable
```

## Return Value

A [Cancellable](../cancellable.md) instance that you use to cancel publishing.
