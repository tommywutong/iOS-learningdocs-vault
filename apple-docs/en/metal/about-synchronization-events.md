---
title: About synchronization events
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/about-synchronization-events
source_url: 'https://developer.apple.com/documentation/metal/about-synchronization-events'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/about-synchronization-events.json'
content_hash: 'sha256:22d8c71e78270214'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Resource synchronization](resource-synchronization.md)

# About synchronization events

<sub>Article</sub>

Synchronize access to resources in your app by signaling events.

## Overview

Use events to specify synchronization points in your app. For example, you might use an event to synchronize graphics rendering commands running on one command queue with compute processing being performed on another command queue.

Metal provides two different kinds of events:

- Nonshareable. [MTLEvent](mtlevent.md) objects synchronize events within a single device object.
- Shareable. [MTLSharedEvent](mtlsharedevent.md) objects synchronize events across multiple device objects, processors, or processes.

Shareable events have a higher overhead than nonshareable events. Don’t use [MTLSharedEvent](mtlsharedevent.md) to synchronize events within a single device object; use [MTLEvent](mtlevent.md) instead.

### Event signaling and waiting

An event contains a monotonically increasing unsigned 64-bit integer. An event starts with a value of `0`. You can either update the event’s value by _signaling_ it, or block further execution by _waiting_ on the event. Typically, you keep an integer value in your app for each event and increase its value each time you need to synchronize on the event. For example, you might increment the number each time you render a new frame of animation.

To signal a change to the event, call [- encodeSignalEvent:value:](<mtlcommandbuffer/encodesignalevent(__value_).md>) on a command buffer, passing in the new value for this event. Metal signals the event after all scheduled commands prior to the event have finished, updating the event’s value if the new value is larger than its current value.

To wait for an event to be signaled, call [- encodeWaitForEvent:value:](<mtlcommandbuffer/encodewaitforevent(__value_).md>) on a command buffer, passing in the value to wait for. Commands that are after this event on the queue don’t run until the event’s value is at least as large as the value you provide.

> [!note] Note
> You can only encode events outside command encoder boundaries, not between encoded commands of a command encoder.

## See Also

### Synchronizing with events

- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [Synchronizing events within a single device](synchronizing-events-within-a-single-device.md) — Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing events across multiple devices or processes](synchronizing-events-across-multiple-devices-or-processes.md) — Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing events between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md) — Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [MTLEvent](mtlevent.md) — A type that synchronizes memory operations to one or more resources within a single Metal device.
- [MTLSharedEvent](mtlsharedevent.md) — A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.
- [MTLSharedEventHandle](mtlsharedeventhandle.md) — An instance you use to recreate a shareable event.
- [MTLSharedEventListener](mtlsharedeventlistener.md) — A listener for shareable event notifications.
- [MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md) — A block of code invoked after a shareable event’s signal value equals or exceeds a given value.
