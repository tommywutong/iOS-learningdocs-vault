---
title: NWProtocolFramer.StartResult.ready
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/startresult/ready
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/startresult/ready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/startresult/ready.json'
content_hash: 'sha256:74690ff04f4851b6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [StartResult](../startresult.md)

# NWProtocolFramer.StartResult.ready

<sub>Case</sub>

The protocol is immediately ready to send and receive data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case ready
```

## See Also

### Start Results

- [NWProtocolFramer.StartResult.willMarkReady](willmarkready.md) — The protocol will perform a handshake, preventing the overall connection from becoming ready until [markReady()](<../instance/markready().md>) is called.
