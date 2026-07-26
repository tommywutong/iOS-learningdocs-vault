---
title: 'makeMachSendSource(port:eventMask:queue:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsource/makemachsendsource(port:eventmask:queue:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/makemachsendsource(port:eventmask:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/makemachsendsource%28port%3Aeventmask%3Aqueue%3A%29.json'
content_hash: 'sha256:9ba459fb292c4ddd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# makeMachSendSource(port:eventMask:queue:)

<sub>Type Method</sub>

A dispatch source that monitors a Mach port for dead name notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func makeMachSendSource(port: mach_port_t, eventMask: DispatchSource.MachSendEvent, queue: DispatchQueue? = nil) -> any DispatchSourceMachSend
```

## Parameters

- `port` — A Mach port with a send or send-once right.

- `eventMask` — The events you want to monitor. For a list of possible values, see [MachSendEvent](machsendevent.md).

- `queue` — The dispatch queue to use when executing the installed handlers.

## Return Value

A dispatch source object that conforms to the [DispatchSourceMachSend](../dispatchsourcemachsend.md) protocol.

## Discussion

After creating the dispatch source, use the methods of the [DispatchSourceProtocol](../dispatchsourceprotocol.md) protocol to install the event handlers you need. The returned dispatch source is in the inactive state initially. When you are ready to begin processing events, call its [dispatch_activate](<../dispatchobject/activate().md>) method.

## See Also

### Creating a Mach Port Source

- [makeMachReceiveSource(port:queue:)](<makemachreceivesource(port_queue_).md>) — Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [DispatchSourceMachReceive](../dispatchsourcemachreceive.md) — A dispatch source that monitors a Mach port for pending messages.
- [DispatchSourceMachSend](../dispatchsourcemachsend.md) — A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.
- [MachSendEvent](machsendevent.md) — Mach-related events.
