---
title: MTLSharedEvent
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsharedevent
source_url: 'https://developer.apple.com/documentation/metal/mtlsharedevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsharedevent.json'
content_hash: 'sha256:fe9b30bb2c3a5b9d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSharedEvent

<sub>Protocol</sub>

A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLSharedEvent : MTLEvent
```

## Overview

The [MTLSharedEvent](mtlsharedevent.md) protocol inherits the [MTLEvent](mtlevent.md) protocol. An event can only synchronize memory operations that run on a single Metal device. A shared event can synchronize memory operations across multiple Metal devices and the CPU. Shared events work anywhere you can work with a regular event.

> [!tip] Tip
> Start with an [MTLEvent](mtlevent.md) instance until you need to synchronize work with a task that runs on the CPU or another Metal device, because an [MTLSharedEvent](mtlsharedevent.md) can add overhead that may affect your app’s performance.

Create an [MTLSharedEvent](mtlsharedevent.md) by calling the [- newSharedEvent](<mtldevice/makesharedevent().md>) method of an [MTLDevice](mtldevice.md) instance.

To pass this event to another process:

1. Create a handle to the shared event by calling the [- newSharedEventHandle](<mtlsharedevent/makesharedeventhandle().md>) method.
2. Transfer the handle to another process with XPC.
3. From the other process, call the [- newSharedEventWithHandle:](<mtldevice/makesharedevent(handle_).md>) method.

For more information about shared events and synchronizing memory operations to resources, see:

- [Synchronizing events across multiple devices or processes](synchronizing-events-across-multiple-devices-or-processes.md)
- [Synchronizing events between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md).
- [Resource synchronization](resource-synchronization.md)

## Relationships

- **Inherits From**: [MTLEvent](mtlevent.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Synchronizing a shareable event

- [signaledValue](mtlsharedevent/signaledvalue.md) — The current signal value for the shareable event.
- [- notifyListener:atValue:block:](<mtlsharedevent/notify(__atvalue_block_).md>) — Schedules a notification handler to be called after the shareable event’s signal value equals or exceeds a given value.

### Creating a shared event handle

- [- newSharedEventHandle](<mtlsharedevent/makesharedeventhandle().md>) — Creates a new shareable event handle.

### Instance Methods

- [valueSignaled(_:)](<mtlsharedevent/valuesignaled(__).md>)
- [- waitUntilSignaledValue:timeoutMS:](<mtlsharedevent/wait(untilsignaledvalue_timeoutms_).md>)

## See Also

### Synchronizing with events

- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [About synchronization events](about-synchronization-events.md) — Synchronize access to resources in your app by signaling events.
- [Synchronizing events within a single device](synchronizing-events-within-a-single-device.md) — Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing events across multiple devices or processes](synchronizing-events-across-multiple-devices-or-processes.md) — Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing events between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md) — Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [MTLEvent](mtlevent.md) — A type that synchronizes memory operations to one or more resources within a single Metal device.
- [MTLSharedEventHandle](mtlsharedeventhandle.md) — An instance you use to recreate a shareable event.
- [MTLSharedEventListener](mtlsharedeventlistener.md) — A listener for shareable event notifications.
- [MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md) — A block of code invoked after a shareable event’s signal value equals or exceeds a given value.
