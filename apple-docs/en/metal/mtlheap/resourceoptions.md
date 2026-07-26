---
title: resourceOptions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/resourceoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/resourceoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/resourceoptions.json'
content_hash: 'sha256:6320bed0dd6f3b7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# resourceOptions

<sub>Instance Property</sub>

The options for resources created by the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var resourceOptions: MTLResourceOptions { get }
```

## Discussion

The value of this property aggregates the values of [storageMode](storagemode.md), [cpuCacheMode](cpucachemode.md), and [hazardTrackingMode](hazardtrackingmode.md).

## See Also

### Checking a heap’s permanent configuration

- [device](device.md) — The device object that created the heap.
- [type](type.md) — The heap’s type.
- [storageMode](storagemode.md) — The heap’s storage mode.
- [cpuCacheMode](cpucachemode.md) — The heap’s CPU cache mode.
- [hazardTrackingMode](hazardtrackingmode.md) — The heap’s hazard tracking mode.
