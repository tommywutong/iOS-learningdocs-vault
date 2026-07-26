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
doc_path: /documentation/metal/mtlresource/resourceoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlresource/resourceoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresource/resourceoptions.json'
content_hash: 'sha256:766d6c480c1e942c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResource](../mtlresource.md)

# resourceOptions

<sub>Instance Property</sub>

The storage mode, CPU cache mode, and hazard tracking mode of the resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var resourceOptions: MTLResourceOptions { get }
```

## Discussion

The value of this property aggregates the values of [storageMode](storagemode.md), [cpuCacheMode](cpucachemode.md), and [hazardTrackingMode](hazardtrackingmode.md).

## See Also

### Reading memory and storage properties

- [cpuCacheMode](cpucachemode.md) — The CPU cache mode that defines the CPU mapping of the resource.
- [storageMode](storagemode.md) — The location and access permissions of the resource.
- [hazardTrackingMode](hazardtrackingmode.md) — A mode that determines whether Metal tracks and synchronizes resource access.
- [MTLCPUCacheMode](../mtlcpucachemode.md) — Options for the CPU cache mode that define the CPU mapping of the resource.
- [MTLStorageMode](../mtlstoragemode.md) — Options for the memory location and access permissions for a resource.
- [MTLHazardTrackingMode](../mtlhazardtrackingmode.md) — Options that control whether Metal automatically tracks and prevents memory hazards for resources.
