---
title: 'resolveCounterRange(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4counterheap/resolvecounterrange(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4counterheap/resolvecounterrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4counterheap/resolvecounterrange%28_%3A%29.json'
content_hash: 'sha256:02b4d32327ed72aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CounterHeap](../mtl4counterheap.md)

# resolveCounterRange(_:)

<sub>Instance Method</sub>

Resolves heap data on the CPU timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resolveCounterRange(_ range: Range<Int>) throws -> Data?
```

## Parameters

- `range` — The range in the heap to resolve.

## Discussion

This method resolves heap data in the CPU timeline. Your app needs to ensure the GPU work has completed in order to retrieve the data correctly. You can alternatively resolve the heap data in the GPU timeline by calling `MTL4CommandBuffer/resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:`.

- Returns a newly allocated autoreleased NSData containing tightly packed resolved heap counter values.

> [!note] Note
> When resolving counters in the CPU timeline, signaling an instance of [MTLSharedEvent](../mtlsharedevent.md) after any workloads write counters (and waiting on that signal on the CPU) is sufficient to ensure synchronization.
