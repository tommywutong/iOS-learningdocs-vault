---
title: 'encodeSignalEvent(_:value:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/encodesignalevent(_:value:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/encodesignalevent(_:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/encodesignalevent%28_%3Avalue%3A%29.json'
content_hash: 'sha256:a53685d9b36e14e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# encodeSignalEvent(_:value:)

<sub>Instance Method</sub>

Encodes a command that updates an event’s value, which can clear the GPU to run passes from other command buffers waiting for the event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func encodeSignalEvent(_ event: any MTLEvent, value: UInt64)
```

## Parameters

- `event` — An [MTLEvent](../mtlevent.md) instance the GPU driver signals between passes as it runs the command buffer. If `event` is an [MTLSharedEvent](../mtlsharedevent.md) instance, the update: - Signals any command buffers waiting for the shared event, including those on other GPU devices - Invokes any notification handlers waiting for the shared event (see [- notifyListener:atValue:block:](<../mtlsharedevent/notify(__atvalue_block_).md>)) Otherwise, the method can signal only command buffers from the same GPU device.

- `value` — A value that’s greater than or equal to the event’s current value; otherwise, the command has no effect.

## Discussion

The method can unblock one or more command buffers that are waiting for `event`, including those in other command queues (see [- encodeWaitForEvent:value:](<encodewaitforevent(__value_).md>)).

A command buffer can signal an event only between passes, not within a pass. If a command buffer has an active encoder, finish using the encoder, call its [- endEncoding](<../mtlcommandencoder/endencoding().md>) method, and then call this method before creating another encoder.

When the GPU device reaches the signal command that this method encodes, Metal updates the event after the GPU finishes the buffer’s prior commands. Updating the event’s value can signal any command buffer that’s waiting for a value equal to or less than the `value` parameter.

## See Also

### Synchronizing passes with events

- [- encodeWaitForEvent:value:](<encodewaitforevent(__value_).md>) — Encodes a command into the command buffer that pauses the GPU from running the buffer’s subsequent passes until the event equals or exceeds a value.
