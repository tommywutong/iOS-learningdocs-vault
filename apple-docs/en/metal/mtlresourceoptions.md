---
title: MTLResourceOptions
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceoptions.json'
content_hash: 'sha256:762bb479e6c4dc75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLResourceOptions

<sub>Structure</sub>

Optional arguments used to set the behavior of a resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLResourceOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializing resource options

- [init(rawValue:)](<mtlresourceoptions/init(rawvalue_).md>)

### Specifying CPU cache modes

- [MTLResourceCPUCacheModeWriteCombined](mtlresourceoptions/cpucachemodewritecombined.md) — A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.

### Specifying storage modes

- [MTLResourceStorageModeShared](mtlresourceoptions/storagemodeshared.md) — The CPU and GPU share access to the resource, allocated in system memory.
- [MTLResourceStorageModeManaged](mtlresourceoptions/storagemodemanaged.md) — The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized. _(deprecated)_
- [MTLResourceStorageModePrivate](mtlresourceoptions/storagemodeprivate.md) — The resource is only available to the GPU.
- [MTLResourceStorageModeMemoryless](mtlresourceoptions/storagemodememoryless.md) — The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.

### Specifying hazard tracking

- [MTLResourceHazardTrackingModeTracked](mtlresourceoptions/hazardtrackingmodetracked.md) — An option that instructs Metal to apply safeguards for a resource at runtime to avoid memory hazards for the applicable commands.
- [MTLResourceHazardTrackingModeUntracked](mtlresourceoptions/hazardtrackingmodeuntracked.md) — A resource option that instructs Metal to ignore memory hazards for a resource at runtime.

### Deprecated options

- [MTLResourceOptionCPUCacheModeWriteCombined](mtlresourceoptions/optioncpucachemodewritecombined.md) — This constant was deprecated in iOS 9.0 and macOS 10.11. _(deprecated)_

## See Also

### Common resource functionality

- [MTLGPUAddress](mtlgpuaddress.md) — A 64-bit unsigned integer type appropriate for storing GPU addresses.
- [MTLAllocation](mtlallocation.md) — A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [MTLResource](mtlresource.md) — An allocation of memory accessible to a GPU.
- [MTLResourceUsage](mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.
- [MTLResourceID](mtlresourceid.md)
