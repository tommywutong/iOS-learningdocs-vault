---
title: 'signalEvent(_:value:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/signalevent(_:value:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/signalevent(_:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/signalevent%28_%3Avalue%3A%29.json'
content_hash: 'sha256:442fe79016a309fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# signalEvent(_:value:)

<sub>Instance Method</sub>

Schedules an operation to signal a GPU event with a specific value after all GPU work prior to this point is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func signalEvent(_ event: any MTLEvent, value: UInt64)
```

## Parameters

- `event` — [MTLEvent](../mtlevent.md) to signal.

- `value` — The value to signal the [MTLEvent](../mtlevent.md) with.
