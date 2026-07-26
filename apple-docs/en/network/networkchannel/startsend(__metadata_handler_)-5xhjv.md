---
title: 'startSend(_:metadata:handler:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/startsend(_:metadata:handler:)-5xhjv'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/startsend(_:metadata:handler:)-5xhjv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/startsend%28_%3Ametadata%3Ahandler%3A%29-5xhjv.json'
content_hash: 'sha256:b458ab98475058f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# startSend(_:metadata:handler:)

<sub>Instance Method</sub>

Send partial binary data on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func startSend<Content>(_ content: Content, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}, handler: ((Content, Bool) async throws -> Void) async throws -> Void) async throws where Content : DataProtocol
```

## Parameters

- `content` — The binary data to send.

- `builder` — A builder for specifying metadata about the content to send.

- `handler` — A handler that will be invoked immediately, and will be passed a closure that should be called repeatedly until all binary data is sent. Intermediate invocations of the send closure must be invoked with `isComplete` set to false. The last call to the send closure must be invoked with `isComplete` set to true.

## Discussion

This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.
