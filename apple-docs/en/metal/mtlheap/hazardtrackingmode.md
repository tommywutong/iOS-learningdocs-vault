---
title: hazardTrackingMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/hazardtrackingmode
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/hazardtrackingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/hazardtrackingmode.json'
content_hash: 'sha256:90977194c48a31a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# hazardTrackingMode

<sub>Instance Property</sub>

The heap’s hazard tracking mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var hazardTrackingMode: MTLHazardTrackingMode { get }
```

## Discussion

Any resources you allocate on the heap have this hazard tracking mode.

## See Also

### Checking a heap’s permanent configuration

- [device](device.md) — The device object that created the heap.
- [type](type.md) — The heap’s type.
- [storageMode](storagemode.md) — The heap’s storage mode.
- [cpuCacheMode](cpucachemode.md) — The heap’s CPU cache mode.
- [resourceOptions](resourceoptions.md) — The options for resources created by the heap.
