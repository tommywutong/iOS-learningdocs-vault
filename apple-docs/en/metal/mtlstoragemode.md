---
title: MTLStorageMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstoragemode
source_url: 'https://developer.apple.com/documentation/metal/mtlstoragemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoragemode.json'
content_hash: 'sha256:614494f14ad1e913'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStorageMode

<sub>Enumeration</sub>

Options for the memory location and access permissions for a resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLStorageMode
```

## Overview

For more guidance on how to choose storage modes, see [Setting resource storage modes](setting-resource-storage-modes.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Storage mode options

- [MTLStorageModeShared](mtlstoragemode/shared.md) — The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageModeManaged](mtlstoragemode/managed.md) — The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized. _(deprecated)_
- [MTLStorageModePrivate](mtlstoragemode/private.md) — The resource is only available to the GPU.
- [MTLStorageModeMemoryless](mtlstoragemode/memoryless.md) — The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.

### Initializers

- [init(rawValue:)](<mtlstoragemode/init(rawvalue_).md>)

## See Also

### Reading memory and storage properties

- [cpuCacheMode](mtlresource/cpucachemode.md) — The CPU cache mode that defines the CPU mapping of the resource.
- [storageMode](mtlresource/storagemode.md) — The location and access permissions of the resource.
- [hazardTrackingMode](mtlresource/hazardtrackingmode.md) — A mode that determines whether Metal tracks and synchronizes resource access.
- [resourceOptions](mtlresource/resourceoptions.md) — The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [MTLCPUCacheMode](mtlcpucachemode.md) — Options for the CPU cache mode that define the CPU mapping of the resource.
- [MTLHazardTrackingMode](mtlhazardtrackingmode.md) — Options that control whether Metal automatically tracks and prevents memory hazards for resources.
