---
title: 'encodeWaitForEvent(_:value:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/encodewaitforevent(_:value:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/encodewaitforevent(_:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/encodewaitforevent%28_%3Avalue%3A%29.json'
content_hash: 'sha256:d980ef84b502a233'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# encodeWaitForEvent(_:value:)

<sub>Instance Method</sub>

Encodes a command into the command buffer that pauses the GPU from running the buffer’s subsequent passes until the event equals or exceeds a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func encodeWaitForEvent(_ event: any MTLEvent, value: UInt64)
```

## Parameters

- `event` — An [MTLEvent](../mtlevent.md) instance the GPU driver waits for between passes as it runs the command buffer. If `event` is an [MTLSharedEvent](../mtlsharedevent.md) instance, a command buffer from any GPU device can signal this command buffer. Otherwise, only command buffers from the same GPU device can signal this command buffer.

- `value` — The event’s smallest value that allows the GPU to continue running the remaining passes in the command buffer.

## Discussion

This method prevents the GPU from starting the next pass in the command buffer until another command buffer signals `event` (see [- encodeSignalEvent:value:](<encodesignalevent(__value_).md>).

A command buffer can instruct the GPU to wait for an event only between passes, not within a pass. If a command buffer has an active encoder, finish using the encoder, call its [- endEncoding](<../mtlcommandencoder/endencoding().md>) method, and then call this method before creating another encoder.

When the GPU device reaches the wait command that this method encodes into the buffer, it checks the event’s current value. If the event’s value — which increases monotonically — is less than the `value` parameter, the GPU waits before running the next pass in the buffer. The GPU starts the next pass when the event signals a value that’s equal to or greater than the `value` parameter (see [- encodeSignalEvent:value:](<encodesignalevent(__value_).md>)). However, If the event’s value is already greater than or equal to the `value` parameter, the GPU immediately starts the next pass without waiting.

## See Also

### Synchronizing passes with events

- [- encodeSignalEvent:value:](<encodesignalevent(__value_).md>) — Encodes a command that updates an event’s value, which can clear the GPU to run passes from other command buffers waiting for the event.
