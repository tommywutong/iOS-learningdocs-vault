---
title: 'prependApplicationProtocolIgnoringReady(options:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/prependapplicationprotocolignoringready(options:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/prependapplicationprotocolignoringready(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/prependapplicationprotocolignoringready%28options%3A%29.json'
content_hash: 'sha256:74d4bfb0c7d107b8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# prependApplicationProtocolIgnoringReady(options:)

<sub>Instance Method</sub>

Dynamically add a protocol to a connection establishment attempt “above” the framer protocol. This means that the protocol above will start running once the framer becomes ready by calling markReady(). This can only be used with framers that return a value of willMarkReady to their start handlers. An example of using this functionality is adding a security protocol, like TLS, above a framer once that framer completes its initial handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func prependApplicationProtocolIgnoringReady(options: NWProtocolOptions) throws
```

## Parameters

- `options` — Protocol options for an application protocol to dynamically add “above” the framer.

## Discussion

To ensure thread safety, this function can only be called in one of the callback blocks invoked on the framer, or in a block passed to NWProtocolFramer.Instance.async().

Throws an error if the protocol could not be added.

This function differs from prependApplicationProtocol when the framer has already been marked ready. prependApplicationProtocol will throw an error if the framer was marked ready. prependApplicationProtocolIgnoringReady will still add the protocol and reset ready. The framer must markReady again.

If there is data in-flight on the connection, the behavior is undefined.
