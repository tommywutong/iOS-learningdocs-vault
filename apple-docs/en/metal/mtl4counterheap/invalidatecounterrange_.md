---
title: 'invalidateCounterRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4counterheap/invalidatecounterrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4counterheap/invalidatecounterrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4counterheap/invalidatecounterrange%3A.json'
content_hash: 'sha256:d4fc796d4c55ef1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CounterHeap](../mtl4counterheap.md)

# invalidateCounterRange:

<sub>Instance Method</sub>

Invalidates a range of entries in this counter heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) invalidateCounterRange:(NSRange) range;
```

## Parameters

- `range` — A heap index range to invalidate.

## Discussion

The effect of this call is immediate on the CPU timeline. You are responsible for ensuring that this counter heap is not currently in use on the GPU.

> [!note] Note
> Invalidated entries produce 0 when resolved.
