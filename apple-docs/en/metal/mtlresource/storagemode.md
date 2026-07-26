---
title: storageMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresource/storagemode
source_url: 'https://developer.apple.com/documentation/metal/mtlresource/storagemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresource/storagemode.json'
content_hash: 'sha256:8e4b8be068b07320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResource](../mtlresource.md)

# storageMode

<sub>Instance Property</sub>

The location and access permissions of the resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var storageMode: MTLStorageMode { get }
```

## Discussion

The storage mode is set when you create the resource and cannot be changed.

## See Also

### Reading memory and storage properties

- [cpuCacheMode](cpucachemode.md) — The CPU cache mode that defines the CPU mapping of the resource.
- [hazardTrackingMode](hazardtrackingmode.md) — A mode that determines whether Metal tracks and synchronizes resource access.
- [resourceOptions](resourceoptions.md) — The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [MTLCPUCacheMode](../mtlcpucachemode.md) — Options for the CPU cache mode that define the CPU mapping of the resource.
- [MTLStorageMode](../mtlstoragemode.md) — Options for the memory location and access permissions for a resource.
- [MTLHazardTrackingMode](../mtlhazardtrackingmode.md) — Options that control whether Metal automatically tracks and prevents memory hazards for resources.
