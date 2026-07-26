---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/device
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/device.json'
content_hash: 'sha256:3585f57f5f887fa2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# device

<sub>Instance Property</sub>

The device object that created the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

A heap is always associated with the [MTLDevice](../mtldevice.md) that created it and can be used only with that device.

## See Also

### Checking a heap’s permanent configuration

- [type](type.md) — The heap’s type.
- [storageMode](storagemode.md) — The heap’s storage mode.
- [cpuCacheMode](cpucachemode.md) — The heap’s CPU cache mode.
- [hazardTrackingMode](hazardtrackingmode.md) — The heap’s hazard tracking mode.
- [resourceOptions](resourceoptions.md) — The options for resources created by the heap.
