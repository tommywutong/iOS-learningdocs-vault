---
title: NWProtocolFramer.Instance
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/instance
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance.json'
content_hash: 'sha256:753ff4f13296641f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolFramer](../nwprotocolframer.md)

# NWProtocolFramer.Instance

<sub>Class</sub>

An object that represents a single instance of your custom protocol running in a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Instance
```

## Overview

All interaction between your protocol and the connection occurs through this object.

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Writing Output

- [parseOutput(minimumIncompleteLength:maximumLength:parse:)](<instance/parseoutput(minimumincompletelength_maximumlength_parse_).md>) — Examines the content of output data while inside your output handler.
- [writeOutput(data:)](<instance/writeoutput(data_)-ydvk.md>) — Sends arbitrary output data from your protocol to the next protocol.
- [writeOutputNoCopy(length:)](<instance/writeoutputnocopy(length_).md>) — Sends a specific number of bytes from a message while inside your output handler.
- [passThroughOutput()](<instance/passthroughoutput().md>) — Indicates that your protocol no longer needs to handle output data.

### Delivering Input

- [parseInput(minimumIncompleteLength:maximumLength:parse:)](<instance/parseinput(minimumincompletelength_maximumlength_parse_).md>) — Examines the content of input data while in your input handler.
- [deliverInput(data:message:isComplete:)](<instance/deliverinput(data_message_iscomplete_).md>) — Delivers an inbound message containing arbitrary data from your protocol to the application.
- [deliverInputNoCopy(length:message:isComplete:)](<instance/deliverinputnocopy(length_message_iscomplete_).md>) — Delivers an inbound message containing a specific number of next received bytes.
- [passThroughInput()](<instance/passthroughinput().md>) — Indicates that your protocol no longer needs to handle input data.

### Managing Instance Lifetime

- [markReady()](<instance/markready().md>) — Indicates to a connection that your protocol’s handshake is complete.
- [markFailed(error:)](<instance/markfailed(error_).md>) — Indicates to a connection that your protocol has encountered an error, or has gracefully closed.
- [prependApplicationProtocol(options:)](<instance/prependapplicationprotocol(options_).md>) — Dynamically adds another protocol that will run above your protocol after your protocol calls [markReady()](<instance/markready().md>).

### Inspecting Instance Properties

- [remote](instance/remote.md) — The remote endpoint of the connection in which your protocol is running.
- [local](instance/local.md) — The local endpoint of the connection in which your protocol is running.
- [parameters](instance/parameters.md) — The parameters of the connection in which your protocol is running.

### Handling Asynchronous Events

- [async(execute:)](<instance/async(execute_).md>) — Requests that a block be executed on the connection’s internal scheduling context.
- [scheduleWakeup(wakeupTime:)](<instance/schedulewakeup(wakeuptime_).md>) — Requests that [wakeup(framer:)](<../nwprotocolframerimplementation/wakeup(framer_).md>) be called on your protocol at a specific time in the future.
- [WakeupTime](instance/wakeuptime.md) — Times at which to schedule a protocol wakeup.

### Instance Properties

- [options](instance/options.md)

### Instance Methods

- [prependApplicationProtocolIgnoringReady(options:)](<instance/prependapplicationprotocolignoringready(options_).md>) — Dynamically add a protocol to a connection establishment attempt “above” the framer protocol. This means that the protocol above will start running once the framer becomes ready by calling markReady(). This can only be used with framers that return a value of willMarkReady to their start handlers. An example of using this functionality is adding a security protocol, like TLS, above a framer once that framer completes its initial handshake. _(beta)_
- [writeOutput(data:)](<instance/writeoutput(data_)-9axn3.md>)

## See Also

### Implementing Framer Protocols

- [NWProtocolFramerImplementation](../nwprotocolframerimplementation.md) — A protocol to which your classes can conform in order to implement a custom framing protocol.
