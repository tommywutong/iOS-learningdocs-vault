---
title: 'startReceive(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/startreceive(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/startreceive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/startreceive%28_%3A%29.json'
content_hash: 'sha256:cf1e88d72731ced9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# startReceive(_:)

<sub>Instance Method</sub>

Receive partial data from a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func startReceive(_ handler: ((Int, Int) async throws -> ApplicationProtocol.Message<Data>) async throws -> Void) async throws
```

## Parameters

- `handler` — Called immediately after invoking `startReceive`. Use the receive closure to keep receiving partial data until the message is complete.

## Discussion

Use this to receive large amounts of data or data that can be processed incrementally.

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.
