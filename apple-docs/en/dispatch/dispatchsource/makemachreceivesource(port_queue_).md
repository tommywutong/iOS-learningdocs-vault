---
title: 'makeMachReceiveSource(port:queue:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsource/makemachreceivesource(port:queue:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/makemachreceivesource(port:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/makemachreceivesource%28port%3Aqueue%3A%29.json'
content_hash: 'sha256:de23653e035912e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# makeMachReceiveSource(port:queue:)

<sub>Type Method</sub>

Creates a new dispatch source object for monitoring a Mach port for pending messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func makeMachReceiveSource(port: mach_port_t, queue: DispatchQueue? = nil) -> any DispatchSourceMachReceive
```

## Parameters

- `port` — A Mach port with a receive right.

- `queue` — The dispatch queue to use when executing the installed handlers.

## Return Value

A dispatch source object that conforms to the [DispatchSourceMachReceive](../dispatchsourcemachreceive.md) protocol.

## Discussion

After creating the dispatch source, use the methods of the [DispatchSourceProtocol](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [dispatch_activate](<../dispatchobject/activate().md>) method.

## See Also

### Creating a Mach Port Source

- [makeMachSendSource(port:eventMask:queue:)](<makemachsendsource(port_eventmask_queue_).md>) — A dispatch source that monitors a Mach port for dead name notifications.
- [DispatchSourceMachReceive](../dispatchsourcemachreceive.md) — A dispatch source that monitors a Mach port for pending messages.
- [DispatchSourceMachSend](../dispatchsourcemachsend.md) — A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.
- [MachSendEvent](machsendevent.md) — Mach-related events.
