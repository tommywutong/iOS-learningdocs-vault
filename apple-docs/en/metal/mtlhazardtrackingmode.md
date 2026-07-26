---
title: MTLHazardTrackingMode
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlhazardtrackingmode
source_url: 'https://developer.apple.com/documentation/metal/mtlhazardtrackingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlhazardtrackingmode.json'
content_hash: 'sha256:8c2d80f06e68fb6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLHazardTrackingMode

<sub>Enumeration</sub>

Options that control whether Metal automatically tracks and prevents memory hazards for resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLHazardTrackingMode
```

## Overview

Hazard tracking helps prevent race conditions by managing memory dependencies between commands. When you enable tracking for a resource, Metal automatically delays write operations until previous read operations finish, and prevents subsequent commands from running until write operations complete.

Metal applies hazard tracking to resources you create with [MTLHazardTrackingModeTracked](mtlhazardtrackingmode/tracked.md), but only when you submit commands that use those resources to an [MTLCommandQueue](mtlcommandqueue.md). Metal doesn’t track resources you create with [MTLHazardTrackingModeUntracked](mtlhazardtrackingmode/untracked.md).

Metal doesn’t apply hazard tracking to commands you submit to an [MTL4CommandQueue](mtl4commandqueue.md), even when those commands use tracked resources.

### Enable hazard tracking for a resource

You can create individual resources with tracking by calling the appropriate [MTLDevice](mtldevice.md) factory method (see [Resource creation](resource-creation.md)), or a factory method of an [MTLHeap](mtlheap.md) instance that you create with hazard tracking. Enable hazard tracking for an individual resource or heap by adding [MTLHazardTrackingModeTracked](mtlhazardtrackingmode/tracked.md) to an [MTLResourceOptions](mtlresourceoptions.md) instance.

Some factory methods have a parameter for resource options, such as [- newBufferWithLength:options:](<mtldevice/makebuffer(length_options_).md>). Other factory methods have a parameter for a descriptor type, which has an [MTLResourceOptions](mtlresourceoptions.md) property. For example, to create an [MTLTexture](mtltexture.md) instance with hazard tracking:

1. Create an [MTLTextureDescriptor](mtltexturedescriptor.md) instance.
2. Add the [MTLHazardTrackingModeTracked](mtlhazardtrackingmode/tracked.md) option to that descriptor’s [resourceOptions](mtltexturedescriptor/resourceoptions.md) property.

### Choose between automatic safety and manual optimization

Hazard tracking provides automatic safety at the cost of some runtime overhead. You can improve the runtime performance of commands you send to an [MTLCommandQueue](mtlcommandqueue.md) by creating resources with [MTLHazardTrackingModeUntracked](mtlhazardtrackingmode/untracked.md) and synchronizing access to those resources yourself.

For more information about synchronizing resources, see [Resource synchronization](resource-synchronization.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Selecting the tracking mode

- [MTLHazardTrackingModeDefault](mtlhazardtrackingmode/default.md) — An option that applies the default tracking behavior in Metal based on the resource or heap type you’re creating.
- [MTLHazardTrackingModeUntracked](mtlhazardtrackingmode/untracked.md) — An option that disables automatic memory hazard tracking in Metal for a resource at runtime.
- [MTLHazardTrackingModeTracked](mtlhazardtrackingmode/tracked.md) — An option that directs Metal to apply runtime safeguards that prevent memory hazards when commands access a resource.

### Initializers

- [init(rawValue:)](<mtlhazardtrackingmode/init(rawvalue_).md>)

## See Also

### Reading memory and storage properties

- [cpuCacheMode](mtlresource/cpucachemode.md) — The CPU cache mode that defines the CPU mapping of the resource.
- [storageMode](mtlresource/storagemode.md) — The location and access permissions of the resource.
- [hazardTrackingMode](mtlresource/hazardtrackingmode.md) — A mode that determines whether Metal tracks and synchronizes resource access.
- [resourceOptions](mtlresource/resourceoptions.md) — The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [MTLCPUCacheMode](mtlcpucachemode.md) — Options for the CPU cache mode that define the CPU mapping of the resource.
- [MTLStorageMode](mtlstoragemode.md) — Options for the memory location and access permissions for a resource.
