---
title: signaledValue
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsharedevent/signaledvalue
source_url: 'https://developer.apple.com/documentation/metal/mtlsharedevent/signaledvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsharedevent/signaledvalue.json'
content_hash: 'sha256:c6c30d2cbe19ca7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSharedEvent](../mtlsharedevent.md)

# signaledValue

<sub>Instance Property</sub>

The current signal value for the shareable event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var signaledValue: UInt64 { get set }
```

## Discussion

When you set the value of a shared event, its value is changed only if you provide a larger value than the value currently stored in the event. Setting this property signals the event. Commands waiting on the event are allowed to run if the new value is equal to or greater than the value for which they are waiting. Similarly, setting the event’s value triggers notifications if the value is equal to or greater than the value for which they are waiting.

## See Also

### Synchronizing a shareable event

- [- notifyListener:atValue:block:](<notify(__atvalue_block_).md>) — Schedules a notification handler to be called after the shareable event’s signal value equals or exceeds a given value.
