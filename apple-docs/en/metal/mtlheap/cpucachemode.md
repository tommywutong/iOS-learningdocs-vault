---
title: cpuCacheMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/cpucachemode
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/cpucachemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/cpucachemode.json'
content_hash: 'sha256:32d22a108da9a343'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# cpuCacheMode

<sub>Instance Property</sub>

The heap’s CPU cache mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cpuCacheMode: MTLCPUCacheMode { get }
```

## Discussion

Any resources you allocate on the heap have this CPU cache mode.

## See Also

### Checking a heap’s permanent configuration

- [device](device.md) — The device object that created the heap.
- [type](type.md) — The heap’s type.
- [storageMode](storagemode.md) — The heap’s storage mode.
- [hazardTrackingMode](hazardtrackingmode.md) — The heap’s hazard tracking mode.
- [resourceOptions](resourceoptions.md) — The options for resources created by the heap.
