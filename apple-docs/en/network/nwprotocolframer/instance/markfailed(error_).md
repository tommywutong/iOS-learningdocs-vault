---
title: 'markFailed(error:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/markfailed(error:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/markfailed(error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/markfailed%28error%3A%29.json'
content_hash: 'sha256:46d94caa402fbec5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# markFailed(error:)

<sub>Instance Method</sub>

Indicates to a connection that your protocol has encountered an error, or has gracefully closed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func markFailed(error: NWError?)
```

## See Also

### Managing Instance Lifetime

- [markReady()](<markready().md>) — Indicates to a connection that your protocol’s handshake is complete.
- [prependApplicationProtocol(options:)](<prependapplicationprotocol(options_).md>) — Dynamically adds another protocol that will run above your protocol after your protocol calls [markReady()](<markready().md>).
