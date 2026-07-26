---
title: type
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/type
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/type.json'
content_hash: 'sha256:f9d29beeec43129e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# type

<sub>Instance Property</sub>

The heap’s type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var type: MTLHeapType { get }
```

## See Also

### Checking a heap’s permanent configuration

- [device](device.md) — The device object that created the heap.
- [storageMode](storagemode.md) — The heap’s storage mode.
- [cpuCacheMode](cpucachemode.md) — The heap’s CPU cache mode.
- [hazardTrackingMode](hazardtrackingmode.md) — The heap’s hazard tracking mode.
- [resourceOptions](resourceoptions.md) — The options for resources created by the heap.
