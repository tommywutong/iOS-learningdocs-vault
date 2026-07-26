---
title: 'writeTimestamp(counterHeap:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandbuffer/writetimestamp(counterheap:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/writetimestamp(counterheap:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/writetimestamp%28counterheap%3Aindex%3A%29.json'
content_hash: 'sha256:bf7b92a8b7eb937a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# writeTimestamp(counterHeap:index:)

<sub>Instance Method</sub>

Writes a GPU timestamp into the given counter heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeTimestamp(counterHeap: any MTL4CounterHeap, index: Int)
```

## Parameters

- `counterHeap` — [MTL4CounterHeap](../mtl4counterheap.md) to write the timestamp into.

- `index` — The index within the [MTL4CounterHeap](../mtl4counterheap.md) that Metal writes the timestamp to.

## Discussion

This method captures a timestamp after work prior to this command in the command buffer is complete. Work after this call may or may not have started.

You are responsible for ensuring the `counterHeap` is of type [MTL4CounterHeapTypeTimestamp](../mtl4counterheaptype/timestamp.md).
