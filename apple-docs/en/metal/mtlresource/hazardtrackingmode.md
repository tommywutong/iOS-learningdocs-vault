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
doc_path: /documentation/metal/mtlresource/hazardtrackingmode
source_url: 'https://developer.apple.com/documentation/metal/mtlresource/hazardtrackingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresource/hazardtrackingmode.json'
content_hash: 'sha256:639016def3bee5f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResource](../mtlresource.md)

# hazardTrackingMode

<sub>Instance Property</sub>

A mode that determines whether Metal tracks and synchronizes resource access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var hazardTrackingMode: MTLHazardTrackingMode { get }
```

## Discussion

This value can be either [MTLHazardTrackingModeUntracked](../mtlhazardtrackingmode/untracked.md) or [MTLHazardTrackingModeTracked](../mtlhazardtrackingmode/tracked.md).

## See Also

### Reading memory and storage properties

- [cpuCacheMode](cpucachemode.md) — The CPU cache mode that defines the CPU mapping of the resource.
- [storageMode](storagemode.md) — The location and access permissions of the resource.
- [resourceOptions](resourceoptions.md) — The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [MTLCPUCacheMode](../mtlcpucachemode.md) — Options for the CPU cache mode that define the CPU mapping of the resource.
- [MTLStorageMode](../mtlstoragemode.md) — Options for the memory location and access permissions for a resource.
- [MTLHazardTrackingMode](../mtlhazardtrackingmode.md) — Options that control whether Metal automatically tracks and prevents memory hazards for resources.
