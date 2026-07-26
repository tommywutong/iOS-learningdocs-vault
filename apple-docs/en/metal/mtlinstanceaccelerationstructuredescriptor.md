---
title: MTLInstanceAccelerationStructureDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor.json'
content_hash: 'sha256:a388c6e3d7f98083'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLInstanceAccelerationStructureDescriptor

<sub>Class</sub>

A description of an acceleration structure that derives from instances of primitive acceleration structures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLInstanceAccelerationStructureDescriptor
```

## Overview

Metal provides acceleration structures with a two-level hierarchy. The bottom layer consists of primitive acceleration structures, which instance acceleration structures in the top level reference.

## Relationships

- **Inherits From**: [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the instance structures

- [instanceDescriptorType](mtlinstanceaccelerationstructuredescriptor/instancedescriptortype.md) — The format of the instance data in the descriptor buffer.
- [instancedAccelerationStructures](mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md) — The bottom-level acceleration structures that instances use in the instance acceleration structure .
- [MTLAccelerationStructureInstanceDescriptorType](mtlaccelerationstructureinstancedescriptortype.md) — Options for specifying different kinds of instance types.

### Specifying the list of instances

- [instanceCount](mtlinstanceaccelerationstructuredescriptor/instancecount.md) — The number of instances in the instance descriptor buffer.
- [instanceDescriptorBuffer](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md) — A buffer that contains descriptions of each instance in the acceleration structure.
- [instanceDescriptorBufferOffset](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset.md) — The offset, in bytes, to the descripton of the first instance.
- [instanceDescriptorStride](mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride.md) — The stride, in bytes, between instance descriptions.

### Specifying motion data

- [motionTransformCount](mtlinstanceaccelerationstructuredescriptor/motiontransformcount.md) — The number of motion transforms in the motion transform buffer.
- [motionTransformBuffer](mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer.md) — A buffer that contains descriptions of each motion transform in the acceleration structure.
- [motionTransformBufferOffset](mtlinstanceaccelerationstructuredescriptor/motiontransformbufferoffset.md) — The offset, in bytes, to the descripton of the first motion transform.

### Instance Properties

- [instanceTransformationMatrixLayout](mtlinstanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.md)
- [motionTransformStride](mtlinstanceaccelerationstructuredescriptor/motiontransformstride.md)
- [motionTransformType](mtlinstanceaccelerationstructuredescriptor/motiontransformtype.md)

## See Also

### Acceleration structures

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md) — Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
- [MTLAccelerationStructure](mtlaccelerationstructure.md) — A collection of model data for GPU-accelerated intersection of rays with the model.
- [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md) — Base class for Metal 4 acceleration structure descriptors.
- [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md) — A base class for classes that define the configuration for a new acceleration structure.
- [MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md) — Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md) — A description of an acceleration structure that contains geometry primitives.
- [MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md) — Descriptor for an instance acceleration structure.
- [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md) — Encodes commands that build and refit acceleration structures for a single pass.
- [MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md) — Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.
- [MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)
