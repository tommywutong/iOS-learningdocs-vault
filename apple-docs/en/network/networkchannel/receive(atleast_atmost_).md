---
title: 'receive(atLeast:atMost:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/receive(atleast:atmost:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/receive(atleast:atmost:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/receive%28atleast%3Aatmost%3A%29.json'
content_hash: 'sha256:3bc8a3480954ebdd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# receive(atLeast:atMost:)

<sub>Instance Method</sub>

Receive data from a connection

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive(atLeast: Int = 1, atMost: Int) async throws -> ApplicationProtocol.Message<Data>
```

## Parameters

- `atLeast` — The minimum length to receive from the connection, until the content is complete.

- `atMost` — The maximum length to receive from the connection in a single completion.

## Discussion

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.
