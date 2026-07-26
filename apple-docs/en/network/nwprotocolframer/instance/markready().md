---
title: markReady()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/instance/markready()
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/markready()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/markready%28%29.json'
content_hash: 'sha256:f9ca0fe46c2546ad'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# markReady()

<sub>Instance Method</sub>

Indicates to a connection that your protocol’s handshake is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func markReady()
```

## See Also

### Related Documentation

- [NWProtocolFramer.StartResult.willMarkReady](../startresult/willmarkready.md) — The protocol will perform a handshake, preventing the overall connection from becoming ready until [markReady()](<markready().md>) is called.

### Managing Instance Lifetime

- [markFailed(error:)](<markfailed(error_).md>) — Indicates to a connection that your protocol has encountered an error, or has gracefully closed.
- [prependApplicationProtocol(options:)](<prependapplicationprotocol(options_).md>) — Dynamically adds another protocol that will run above your protocol after your protocol calls [markReady()](<markready().md>).
