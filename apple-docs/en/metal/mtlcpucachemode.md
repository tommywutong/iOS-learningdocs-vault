---
title: MTLCPUCacheMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcpucachemode
source_url: 'https://developer.apple.com/documentation/metal/mtlcpucachemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcpucachemode.json'
content_hash: 'sha256:053e10957c15308f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCPUCacheMode

<sub>Enumeration</sub>

Options for the CPU cache mode that define the CPU mapping of the resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLCPUCacheMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying the cache mode

- [MTLCPUCacheModeDefaultCache](mtlcpucachemode/defaultcache.md) — The default CPU cache mode for the resource, which guarantees that read and write operations are executed in the expected order.
- [MTLCPUCacheModeWriteCombined](mtlcpucachemode/writecombined.md) — A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.

### Initializers

- [init(rawValue:)](<mtlcpucachemode/init(rawvalue_).md>)

## See Also

### Reading memory and storage properties

- [cpuCacheMode](mtlresource/cpucachemode.md) — The CPU cache mode that defines the CPU mapping of the resource.
- [storageMode](mtlresource/storagemode.md) — The location and access permissions of the resource.
- [hazardTrackingMode](mtlresource/hazardtrackingmode.md) — A mode that determines whether Metal tracks and synchronizes resource access.
- [resourceOptions](mtlresource/resourceoptions.md) — The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [MTLStorageMode](mtlstoragemode.md) — Options for the memory location and access permissions for a resource.
- [MTLHazardTrackingMode](mtlhazardtrackingmode.md) — Options that control whether Metal automatically tracks and prevents memory hazards for resources.
