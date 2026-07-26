---
title: 'waitForEvent(_:value:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/waitforevent(_:value:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/waitforevent(_:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/waitforevent%28_%3Avalue%3A%29.json'
content_hash: 'sha256:3eeb231a4e79f669'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# waitForEvent(_:value:)

<sub>Instance Method</sub>

Schedules an operation to wait for a GPU event of a specific value before continuing to execute any future GPU work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func waitForEvent(_ event: any MTLEvent, value: UInt64)
```

## Parameters

- `event` — [MTLEvent](../mtlevent.md) to wait on.

- `value` — The specific value to wait for.
