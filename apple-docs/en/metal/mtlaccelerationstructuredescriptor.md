---
title: MTLAccelerationStructureDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuredescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuredescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuredescriptor.json'
content_hash: 'sha256:45e6bb3f776eda68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureDescriptor

<sub>Class</sub>

A base class for classes that define the configuration for a new acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLAccelerationStructureDescriptor
```

## Overview

This is the base class for other acceleration structure descriptors. Don’t use this class directly. Use one of the derived classes instead, as [MTLAccelerationStructure](mtlaccelerationstructure.md) describes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md), [MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md), [MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md), [MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying usage options

- [usage](mtlaccelerationstructuredescriptor/usage.md) — The options that describe how you intend to use the acceleration structure.

## See Also

### Acceleration structures

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md) — Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
- [MTLAccelerationStructure](mtlaccelerationstructure.md) — A collection of model data for GPU-accelerated intersection of rays with the model.
- [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md) — Base class for Metal 4 acceleration structure descriptors.
- [MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md) — Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md) — A description of an acceleration structure that contains geometry primitives.
- [MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md) — Descriptor for an instance acceleration structure.
- [MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md) — Encodes commands that build and refit acceleration structures for a single pass.
- [MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md) — Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.
- [MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)
