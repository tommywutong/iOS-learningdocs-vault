---
title: 'prependApplicationProtocol(options:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/prependapplicationprotocol(options:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/prependapplicationprotocol(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/prependapplicationprotocol%28options%3A%29.json'
content_hash: 'sha256:0db73ac13fe7f425'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# prependApplicationProtocol(options:)

<sub>Instance Method</sub>

Dynamically adds another protocol that will run above your protocol after your protocol calls [markReady()](<markready().md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func prependApplicationProtocol(options: NWProtocolOptions) throws
```

## See Also

### Managing Instance Lifetime

- [markReady()](<markready().md>) — Indicates to a connection that your protocol’s handshake is complete.
- [markFailed(error:)](<markfailed(error_).md>) — Indicates to a connection that your protocol has encountered an error, or has gracefully closed.
