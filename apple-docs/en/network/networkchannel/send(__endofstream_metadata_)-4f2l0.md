---
title: 'send(_:endOfStream:metadata:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/send(_:endofstream:metadata:)-4f2l0'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/send(_:endofstream:metadata:)-4f2l0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/send%28_%3Aendofstream%3Ametadata%3A%29-4f2l0.json'
content_hash: 'sha256:1b569ceb6d20ae57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# send(_:endOfStream:metadata:)

<sub>Instance Method</sub>

Send fixed width integer on a connection. This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send<Value>(_ value: Value, endOfStream: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where Value : NetworkFixedWidthInteger
```

## Parameters

- `value` — The integer to send on the connection

- `endOfStream` — Pass true to close the write side of the connection after enqueuing the data to send, meaning that no more data can be sent

- `builder` — An optional builder for specifying metadata
