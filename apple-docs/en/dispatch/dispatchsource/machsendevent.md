---
title: DispatchSource.MachSendEvent
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/machsendevent
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/machsendevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/machsendevent.json'
content_hash: 'sha256:7d4a303bf5a3d546'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# DispatchSource.MachSendEvent

<sub>Structure</sub>

Mach-related events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MachSendEvent
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Mach Event Flags

- [dead](machsendevent/dead.md) — The receive right corresponding to the given send right was destroyed.

## See Also

### Creating a Mach Port Source

- [makeMachReceiveSource(port:queue:)](<makemachreceivesource(port_queue_).md>) — Creates a new dispatch source object for monitoring a Mach port for pending messages.
- [makeMachSendSource(port:eventMask:queue:)](<makemachsendsource(port_eventmask_queue_).md>) — A dispatch source that monitors a Mach port for dead name notifications.
- [DispatchSourceMachReceive](../dispatchsourcemachreceive.md) — A dispatch source that monitors a Mach port for pending messages.
- [DispatchSourceMachSend](../dispatchsourcemachsend.md) — A dispatch source that monitors a Mach port for dead name notifications, indicating that a send right no longer has a corresponding receive right.
