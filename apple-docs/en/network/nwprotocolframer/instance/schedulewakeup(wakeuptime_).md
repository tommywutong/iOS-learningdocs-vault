---
title: 'scheduleWakeup(wakeupTime:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/schedulewakeup(wakeuptime:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/schedulewakeup(wakeuptime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/schedulewakeup%28wakeuptime%3A%29.json'
content_hash: 'sha256:4285f21e6592824f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# scheduleWakeup(wakeupTime:)

<sub>Instance Method</sub>

Requests that [wakeup(framer:)](<../../nwprotocolframerimplementation/wakeup(framer_).md>) be called on your protocol at a specific time in the future.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func scheduleWakeup(wakeupTime: NWProtocolFramer.Instance.WakeupTime)
```

## See Also

### Handling Asynchronous Events

- [async(execute:)](<async(execute_).md>) — Requests that a block be executed on the connection’s internal scheduling context.
- [WakeupTime](wakeuptime.md) — Times at which to schedule a protocol wakeup.
