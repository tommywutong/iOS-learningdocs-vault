---
title: DispatchSourceMachSend
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourcemachsend
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcemachsend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcemachsend.json'
content_hash: 'sha256:b96b78906b2ab7b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceMachSend

<sub>Protocol</sub>

A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceMachSend : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeMachSendSource(port:eventMask:queue:)](<dispatchsource/makemachsendsource(port_eventmask_queue_).md>) method to create an object that adopts this protocol.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## Topics

### Getting the Mach Port Handle

- [handle](dispatchsourcemachsend/handle.md)

### Getting the Event Data

- [data](dispatchsourcemachsend/data.md)
- [mask](dispatchsourcemachsend/mask.md)

## See Also

### Creating a Mach Port Source

- [makeMachReceiveSource(port:queue:)](<dispatchsource/makemachreceivesource(port_queue_).md>) — Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [makeMachSendSource(port:eventMask:queue:)](<dispatchsource/makemachsendsource(port_eventmask_queue_).md>) — A dispatch source that monitors a Mach port for dead name notifications.
- [DispatchSourceMachReceive](dispatchsourcemachreceive.md) — A dispatch source that monitors a Mach port for pending messages.
- [MachSendEvent](dispatchsource/machsendevent.md) — Mach-related events.
