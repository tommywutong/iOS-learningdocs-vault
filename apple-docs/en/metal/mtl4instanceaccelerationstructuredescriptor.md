---
title: MTL4InstanceAccelerationStructureDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4instanceaccelerationstructuredescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4instanceaccelerationstructuredescriptor.json'
content_hash: 'sha256:2eebf29864c9d25d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4InstanceAccelerationStructureDescriptor

<sub>Class</sub>

Descriptor for an instance acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4InstanceAccelerationStructureDescriptor
```

## Overview

An instance acceleration structure references other acceleration structures, and provides the ability to “instantiate” them multiple times, each one with potentially a different transformation matrix.

You specify the properties of the instances in the acceleration structure this descriptor builds by providing a buffer of `structs` via its [instanceDescriptorBuffer](mtl4instanceaccelerationstructuredescriptor/instancedescriptorbuffer.md) property.

Use a [MTLResidencySet](mtlresidencyset.md) to mark residency of all buffers and acceleration structures this descriptor references when you build this acceleration structure.

## Relationships

- **Inherits From**: [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [instanceCount](mtl4instanceaccelerationstructuredescriptor/instancecount.md) — Controls the number of instance descriptors in the instance descriptor buffer references.
- [instanceDescriptorBuffer](mtl4instanceaccelerationstructuredescriptor/instancedescriptorbuffer.md) — Assigns a reference to a buffer containing instance descriptors for acceleration structures to reference.
- [instanceDescriptorStride](mtl4instanceaccelerationstructuredescriptor/instancedescriptorstride.md) — Sets the stride, in bytes, between instance descriptors the instance descriptor buffer references.
- [instanceDescriptorType](mtl4instanceaccelerationstructuredescriptor/instancedescriptortype.md) — The type of instance descriptor that the instance descriptor buffer references.
- [instanceTransformationMatrixLayout](mtl4instanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.md) — Specifies the layout for the transformation matrices in the instance descriptor buffer and the motion transformation matrix buffer.
- [motionTransformBuffer](mtl4instanceaccelerationstructuredescriptor/motiontransformbuffer.md) — A buffer containing transformation information for instance motion keyframes, formatted according to the motion transform type.
- [motionTransformCount](mtl4instanceaccelerationstructuredescriptor/motiontransformcount.md) — Controls the total number of motion transforms in the motion transform buffer.
- [motionTransformStride](mtl4instanceaccelerationstructuredescriptor/motiontransformstride.md) — Specify the stride for motion transform.
- [motionTransformType](mtl4instanceaccelerationstructuredescriptor/motiontransformtype.md) — Controls the type of motion transforms, either as a matrix or individual components.

## See Also

### Acceleration structures

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md) — Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
- [MTLAccelerationStructure](mtlaccelerationstructure.md) — A collection of model data for GPU-accelerated intersection of rays with the model.
- [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md) — Base class for Metal 4 acceleration structure descriptors.
- [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md) — A base class for classes that define the configuration for a new acceleration structure.
- [MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md) — Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md) — A description of an acceleration structure that contains geometry primitives.
- [MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md) — Encodes commands that build and refit acceleration structures for a single pass.
- [MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md) — Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.
- [MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)
