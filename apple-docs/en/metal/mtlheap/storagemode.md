---
title: storageMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/storagemode
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/storagemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/storagemode.json'
content_hash: 'sha256:f7d6f2bc35b31a03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# storageMode

<sub>Instance Property</sub>

The heap’s storage mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var storageMode: MTLStorageMode { get }
```

## Discussion

Any resources you allocate on the heap have this storage mode.

## See Also

### Checking a heap’s permanent configuration

- [device](device.md) — The device object that created the heap.
- [type](type.md) — The heap’s type.
- [cpuCacheMode](cpucachemode.md) — The heap’s CPU cache mode.
- [hazardTrackingMode](hazardtrackingmode.md) — The heap’s hazard tracking mode.
- [resourceOptions](resourceoptions.md) — The options for resources created by the heap.
