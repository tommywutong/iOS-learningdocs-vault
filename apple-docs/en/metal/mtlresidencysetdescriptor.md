---
title: MTLResidencySetDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresidencysetdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlresidencysetdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresidencysetdescriptor.json'
content_hash: 'sha256:def59621104842df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLResidencySetDescriptor

<sub>Class</sub>

A configuration that customizes the behavior for a residency set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLResidencySetDescriptor
```

## Overview

Make an [MTLResidencySet](mtlresidencyset.md) by creating and configuring an [MTLResidencySetDescriptor](mtlresidencysetdescriptor.md) instance and pass it to the [- newResidencySetWithDescriptor:error:](<mtldevice/makeresidencyset(descriptor_).md>) method of an [MTLDevice](mtldevice.md) instance.

See [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md) for more information.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the residency set

- [label](mtlresidencysetdescriptor/label.md) — An optional name that can help you identify a residency set you create with the descriptor.
- [initialCapacity](mtlresidencysetdescriptor/initialcapacity.md) — The number of allocations a new residency set can store without reallocating memory.

## See Also

### Residency sets

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md) — Organize your resources into groups and influence when they become accessible to the GPU.
- [MTLResidencySet](mtlresidencyset.md) — A collection of resource allocations that can move in and out of resident memory.
