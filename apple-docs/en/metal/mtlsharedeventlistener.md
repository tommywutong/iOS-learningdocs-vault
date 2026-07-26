---
title: MTLSharedEventListener
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsharedeventlistener
source_url: 'https://developer.apple.com/documentation/metal/mtlsharedeventlistener'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsharedeventlistener.json'
content_hash: 'sha256:0b2210ae55af8ab9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSharedEventListener

<sub>Class</sub>

A listener for shareable event notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLSharedEventListener
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a shareable event listener

- [- init](<mtlsharedeventlistener/init().md>) — Creates a new shareable event listener.
- [- initWithDispatchQueue:](<mtlsharedeventlistener/init(dispatchqueue_).md>) — Creates a new shareable event listener with a specific dispatch queue.

### Getting the dispatch queue

- [dispatchQueue](mtlsharedeventlistener/dispatchqueue.md) — The dispatch queue used to dispatch any notifications.

### Type Methods

- [+ sharedListener](<mtlsharedeventlistener/shared().md>)

## See Also

### Synchronizing with events

- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [About synchronization events](about-synchronization-events.md) — Synchronize access to resources in your app by signaling events.
- [Synchronizing events within a single device](synchronizing-events-within-a-single-device.md) — Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing events across multiple devices or processes](synchronizing-events-across-multiple-devices-or-processes.md) — Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing events between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md) — Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [MTLEvent](mtlevent.md) — A type that synchronizes memory operations to one or more resources within a single Metal device.
- [MTLSharedEvent](mtlsharedevent.md) — A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.
- [MTLSharedEventHandle](mtlsharedeventhandle.md) — An instance you use to recreate a shareable event.
- [MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md) — A block of code invoked after a shareable event’s signal value equals or exceeds a given value.
