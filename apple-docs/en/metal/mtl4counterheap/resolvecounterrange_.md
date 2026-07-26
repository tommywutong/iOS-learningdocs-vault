---
title: 'resolveCounterRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4counterheap/resolvecounterrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4counterheap/resolvecounterrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4counterheap/resolvecounterrange%3A.json'
content_hash: 'sha256:03879238f6cab096'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CounterHeap](../mtl4counterheap.md)

# resolveCounterRange:

<sub>Instance Method</sub>

Resolves heap data on the CPU timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (NSData *) resolveCounterRange:(NSRange) range;
```

## Parameters

- `range` — The range in the heap to resolve.

## Discussion

This method resolves heap data in the CPU timeline. Your app needs to ensure the GPU work has completed in order to retrieve the data correctly. You can alternatively resolve the heap data in the GPU timeline by calling [resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:](../mtl4commandbuffer/resolvecounterheap_withrange_intobuffer_waitfence_updatefence_.md).

- Returns a newly allocated autoreleased NSData containing tightly packed resolved heap counter values.

> [!note] Note
> When resolving counters in the CPU timeline, signaling an instance of [MTLSharedEvent](../mtlsharedevent.md) after any workloads write counters (and waiting on that signal on the CPU) is sufficient to ensure synchronization.
