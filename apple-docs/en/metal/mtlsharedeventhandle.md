---
title: MTLSharedEventHandle
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsharedeventhandle
source_url: 'https://developer.apple.com/documentation/metal/mtlsharedeventhandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsharedeventhandle.json'
content_hash: 'sha256:30cb976fe1c1d0b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSharedEventHandle

<sub>Class</sub>

An instance you use to recreate a shareable event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLSharedEventHandle
```

## Overview

To create a `MTLSharedEventHandle` instance, call the [- newSharedEventHandle](<mtlsharedevent/makesharedeventhandle().md>) method on an [MTLSharedEvent](mtlsharedevent.md) instance. Use an XPC conection to pass a `MTLSharedEventHandle` instance to another process. To recreate the event, call the [- newSharedEventWithHandle:](<mtldevice/makesharedevent(handle_).md>) on an [MTLDevice](mtldevice.md) instance.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the shareable event handle

- [label](mtlsharedeventhandle/label.md) — A string that identifies the shareable event.

### Initializers

- [init(coder:)](<mtlsharedeventhandle/init(coder_).md>)

## See Also

### Synchronizing with events

- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [About synchronization events](about-synchronization-events.md) — Synchronize access to resources in your app by signaling events.
- [Synchronizing events within a single device](synchronizing-events-within-a-single-device.md) — Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing events across multiple devices or processes](synchronizing-events-across-multiple-devices-or-processes.md) — Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing events between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md) — Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [MTLEvent](mtlevent.md) — A type that synchronizes memory operations to one or more resources within a single Metal device.
- [MTLSharedEvent](mtlsharedevent.md) — A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.
- [MTLSharedEventListener](mtlsharedeventlistener.md) — A listener for shareable event notifications.
- [MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md) — A block of code invoked after a shareable event’s signal value equals or exceeds a given value.
