---
title: NWProtocolFramer.Instance.WakeupTime
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolframer/instance/wakeuptime
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/wakeuptime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/wakeuptime.json'
content_hash: 'sha256:5168baa2a982f1ed'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# NWProtocolFramer.Instance.WakeupTime

<sub>Enumeration</sub>

Times at which to schedule a protocol wakeup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum WakeupTime
```

## Topics

### Time Values

- [NWProtocolFramer.Instance.WakeupTime.milliseconds(_:)](<wakeuptime/milliseconds(__).md>) — A specific number of milliseconds from now.
- [NWProtocolFramer.Instance.WakeupTime.forever](wakeuptime/forever.md) — A sentinel value to indicate that no wakeup should be delivered.

## See Also

### Handling Asynchronous Events

- [async(execute:)](<async(execute_).md>) — Requests that a block be executed on the connection’s internal scheduling context.
- [scheduleWakeup(wakeupTime:)](<schedulewakeup(wakeuptime_).md>) — Requests that [wakeup(framer:)](<../../nwprotocolframerimplementation/wakeup(framer_).md>) be called on your protocol at a specific time in the future.
