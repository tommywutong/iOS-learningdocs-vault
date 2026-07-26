---
title: 'makeCounterHeap(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makecounterheap(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecounterheap(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecounterheap%28descriptor%3A%29.json'
content_hash: 'sha256:d1bde03ceda923f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCounterHeap(descriptor:)

<sub>Instance Method</sub>

Creates a new counter heap configured from a counter heap descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCounterHeap(descriptor: MTL4CounterHeapDescriptor) throws -> any MTL4CounterHeap
```

## Parameters

- `descriptor` — [MTL4CounterHeapDescriptor](../mtl4counterheapdescriptor.md) instance that configures the [MTL4CounterHeap](../mtl4counterheap.md) instance.

## Return Value

A [MTL4CounterHeap](../mtl4counterheap.md) instance, or `nil` if the function failed.
