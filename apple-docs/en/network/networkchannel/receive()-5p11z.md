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
doc_path: /documentation/network/networkchannel/receive()-5p11z
source_url: 'https://developer.apple.com/documentation/network/networkchannel/receive()-5p11z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/receive%28%29-5p11z.json'
content_hash: 'sha256:ab2ce701ad4f29ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# receive()

<sub>Instance Method</sub>

Receive an object from a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive<Sending, Receiving, CoderType>() async throws -> ApplicationProtocol.Message<Receiving> where ApplicationProtocol == Coder<Sending, Receiving, CoderType>, Sending : Encodable, Receiving : Decodable, CoderType : NetworkCoder
```

## Discussion

The object will be decoded and returned. An error will be thrown if the object cannot be decoded.

This may be called before the connection is ready, in which case the receive request will be enqueued until the connection is ready.
