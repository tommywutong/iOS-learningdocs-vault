---
title: receive()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkchannel/receive()-8jbul
source_url: 'https://developer.apple.com/documentation/network/networkchannel/receive()-8jbul'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/receive%28%29-8jbul.json'
content_hash: 'sha256:8b36addc30a40af4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# receive()

<sub>Instance Method</sub>

Receive data on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive<T>() async throws -> ApplicationProtocol.Message<Data> where ApplicationProtocol == Framer<T>, T : FramerProtocol
```
