---
title: 'signalEvent(_:value:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocommandbuffer/signalevent(_:value:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/signalevent(_:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/signalevent%28_%3Avalue%3A%29.json'
content_hash: 'sha256:727c3e991f34aa7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# signalEvent(_:value:)

<sub>Instance Method</sub>

Encodes a command that signals a shared event to other parts of your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func signalEvent(_ event: any MTLSharedEvent, value: UInt64)
```

## Parameters

- `event` — A shared event instance the method waits for.

- `value` — A value the command uses to signal for the event to other parts of your app.

## See Also

### Synchronizing a command buffer

- [- waitForEvent:value:](<waitforevent(__value_).md>) — Encodes a command that pauses the command buffer’s execution until another part of your app signals a shared event.
