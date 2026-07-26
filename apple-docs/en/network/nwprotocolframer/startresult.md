---
title: NWProtocolFramer.StartResult
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/startresult
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/startresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/startresult.json'
content_hash: 'sha256:7dbfc75077101879'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolFramer](../nwprotocolframer.md)

# NWProtocolFramer.StartResult

<sub>Enumeration</sub>

Results that you send to indicate the disposition of your protocol after receiving the call to start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum StartResult
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Start Results

- [NWProtocolFramer.StartResult.ready](startresult/ready.md) — The protocol is immediately ready to send and receive data.
- [NWProtocolFramer.StartResult.willMarkReady](startresult/willmarkready.md) — The protocol will perform a handshake, preventing the overall connection from becoming ready until [markReady()](<instance/markready().md>) is called.

## See Also

### Handling Instance Lifetime

- [init(framer:)](<../nwprotocolframerimplementation/init(framer_).md>) — Initializes your custom framing protocol for use in one connection attempt.
- [start(framer:)](<../nwprotocolframerimplementation/start(framer_).md>) — Requests that your protocol set up its state and begin a handshake, if necessary.
- [wakeup(framer:)](<../nwprotocolframerimplementation/wakeup(framer_).md>) — Delivers a scheduled wakeup event.
- [stop(framer:)](<../nwprotocolframerimplementation/stop(framer_).md>) — Requests that your protocol send any final messages to close the connection.
- [cleanup(framer:)](<../nwprotocolframerimplementation/cleanup(framer_).md>) — Indicates that your protocol should clean up all allocations before being deallocated.
- [label](../nwprotocolframerimplementation/label.md) — A label defined by your custom protocol for use in debugging.
