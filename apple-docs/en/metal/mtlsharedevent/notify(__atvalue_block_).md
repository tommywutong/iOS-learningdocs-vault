---
title: 'notify(_:atValue:block:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlsharedevent/notify(_:atvalue:block:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlsharedevent/notify(_:atvalue:block:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsharedevent/notify%28_%3Aatvalue%3Ablock%3A%29.json'
content_hash: 'sha256:6bee6f1175aa9221'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSharedEvent](../mtlsharedevent.md)

# notify(_:atValue:block:)

<sub>Instance Method</sub>

Schedules a notification handler to be called after the shareable event’s signal value equals or exceeds a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func notify(_ listener: MTLSharedEventListener, atValue value: UInt64, block: @escaping MTLSharedEventNotificationBlock)
```

## Parameters

- `listener` — The listener object used to dispatch the notification.

- `value` — The minimum value that needs to be signaled before the notification handler is called.

- `block` — The notification handler to call.

## See Also

### Synchronizing a shareable event

- [signaledValue](signaledvalue.md) — The current signal value for the shareable event.
