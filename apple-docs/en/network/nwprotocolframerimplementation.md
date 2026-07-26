---
title: NWProtocolFramerImplementation
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframerimplementation
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframerimplementation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframerimplementation.json'
content_hash: 'sha256:835c76c0413b3502'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWProtocolFramerImplementation

<sub>Protocol</sub>

A protocol to which your classes can conform in order to implement a custom framing protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NWProtocolFramerImplementation : AnyObject
```

## Topics

### Handling Instance Lifetime

- [init(framer:)](<nwprotocolframerimplementation/init(framer_).md>) — Initializes your custom framing protocol for use in one connection attempt.
- [start(framer:)](<nwprotocolframerimplementation/start(framer_).md>) — Requests that your protocol set up its state and begin a handshake, if necessary.
- [StartResult](nwprotocolframer/startresult.md) — Results that you send to indicate the disposition of your protocol after receiving the call to start.
- [wakeup(framer:)](<nwprotocolframerimplementation/wakeup(framer_).md>) — Delivers a scheduled wakeup event.
- [stop(framer:)](<nwprotocolframerimplementation/stop(framer_).md>) — Requests that your protocol send any final messages to close the connection.
- [cleanup(framer:)](<nwprotocolframerimplementation/cleanup(framer_).md>) — Indicates that your protocol should clean up all allocations before being deallocated.
- [label](nwprotocolframerimplementation/label.md) — A label defined by your custom protocol for use in debugging.

### Handling Data

- [handleOutput(framer:message:messageLength:isComplete:)](<nwprotocolframerimplementation/handleoutput(framer_message_messagelength_iscomplete_).md>) — Notifies your protocol about a new outbound message.
- [handleInput(framer:)](<nwprotocolframerimplementation/handleinput(framer_).md>) — Notifies your protocol that new inbound data is available to parse.

## See Also

### Implementing Framer Protocols

- [Instance](nwprotocolframer/instance.md) — An object that represents a single instance of your custom protocol running in a connection.
