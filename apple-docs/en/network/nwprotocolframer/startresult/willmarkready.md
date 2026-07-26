---
title: NWProtocolFramer.StartResult.willMarkReady
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/startresult/willmarkready
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/startresult/willmarkready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/startresult/willmarkready.json'
content_hash: 'sha256:a8646eadce43f40a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [StartResult](../startresult.md)

# NWProtocolFramer.StartResult.willMarkReady

<sub>Case</sub>

The protocol will perform a handshake, preventing the overall connection from becoming ready until [markReady()](<../instance/markready().md>) is called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case willMarkReady
```

## See Also

### Related Documentation

- [markReady()](<../instance/markready().md>) — Indicates to a connection that your protocol’s handshake is complete.

### Start Results

- [NWProtocolFramer.StartResult.ready](ready.md) — The protocol is immediately ready to send and receive data.
