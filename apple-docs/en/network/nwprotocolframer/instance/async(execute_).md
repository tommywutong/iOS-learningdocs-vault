---
title: 'async(execute:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/async(execute:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/async(execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/async%28execute%3A%29.json'
content_hash: 'sha256:2def7813197c0270'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# async(execute:)

<sub>Instance Method</sub>

Requests that a block be executed on the connection’s internal scheduling context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func async(execute: @escaping () -> Void)
```

## Discussion

You should call this if you need to call any framer functions but are in another scheduling context.

## See Also

### Handling Asynchronous Events

- [scheduleWakeup(wakeupTime:)](<schedulewakeup(wakeuptime_).md>) — Requests that [wakeup(framer:)](<../../nwprotocolframerimplementation/wakeup(framer_).md>) be called on your protocol at a specific time in the future.
- [WakeupTime](wakeuptime.md) — Times at which to schedule a protocol wakeup.
