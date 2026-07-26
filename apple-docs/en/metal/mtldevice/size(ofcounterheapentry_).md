---
title: 'size(ofCounterHeapEntry:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/size(ofcounterheapentry:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/size(ofcounterheapentry:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/size%28ofcounterheapentry%3A%29.json'
content_hash: 'sha256:7c52e27522501396'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# size(ofCounterHeapEntry:)

<sub>Instance Method</sub>

Returns the size, in bytes, of each entry in a counter heap of a specific counter heap type when your app resolves it into a usable format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func size(ofCounterHeapEntry type: MTL4CounterHeapType) -> Int
```

## Parameters

- `type` — [MTL4CounterHeapType](../mtl4counterheaptype.md) value that represents the type of the [MTL4CounterHeap](../mtl4counterheap.md) to resolve.

## Return Value

The size of the post-transformation entry from a [MTL4CounterHeap](../mtl4counterheap.md) of type [MTL4CounterHeapType](../mtl4counterheaptype.md).

## Discussion

In order to use the data available in a [MTL4CounterHeap](../mtl4counterheap.md), your app first resolves it either in the CPU timeline or in the GPU timeline. When your app calls [resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:](../mtl4commandbuffer/resolvecounterheap_withrange_intobuffer_waitfence_updatefence_.md) to resolve counter data in the GPU timeline, Metal writes the data into a [MTLBuffer](../mtlbuffer.md).

During this process, Metal transform the data in the heap into a format consisting of entries of the size that this method advertises, based on the [MTL4CounterHeapType](../mtl4counterheaptype.md).
