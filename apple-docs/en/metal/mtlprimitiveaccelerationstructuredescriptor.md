---
title: MTLPrimitiveAccelerationStructureDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlprimitiveaccelerationstructuredescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlprimitiveaccelerationstructuredescriptor.json'
content_hash: 'sha256:dc1944671428e28e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPrimitiveAccelerationStructureDescriptor

<sub>Class</sub>

A description of an acceleration structure that contains geometry primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLPrimitiveAccelerationStructureDescriptor
```

## Overview

Metal provides acceleration structures with a two-level hierarchy. The bottom layer consists of primitive acceleration structures, which instance acceleration structures in the top level reference.

## Relationships

- **Inherits From**: [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying geometry

- [geometryDescriptors](mtlprimitiveaccelerationstructuredescriptor/geometrydescriptors.md) — An array that contains the individual pieces of geometry that compose the acceleration structure.

### Specifying motion behavior

- [motionKeyframeCount](mtlprimitiveaccelerationstructuredescriptor/motionkeyframecount.md) — The number of keyframes in the geometry data.
- [motionStartTime](mtlprimitiveaccelerationstructuredescriptor/motionstarttime.md) — The start time for the range of motion that the keyframe data describes.
- [motionEndTime](mtlprimitiveaccelerationstructuredescriptor/motionendtime.md) — The end time for the range of motion that the keyframe data describes.
- [motionStartBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionstartbordermode.md) — The mode to use when handling timestamps before the start time.
- [motionEndBorderMode](mtlprimitiveaccelerationstructuredescriptor/motionendbordermode.md) — The mode to use when handling timestamps after the end time.
- [MTLMotionBorderMode](mtlmotionbordermode.md) — Options for specifying how the acceleration structure handles timestamps that are outside the specified range.

## See Also

### Acceleration structures

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md) — Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
- [MTLAccelerationStructure](mtlaccelerationstructure.md) — A collection of model data for GPU-accelerated intersection of rays with the model.
- [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md) — Base class for Metal 4 acceleration structure descriptors.
- [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md) — A base class for classes that define the configuration for a new acceleration structure.
- [MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md) — Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md) — Descriptor for an instance acceleration structure.
- [MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md) — Encodes commands that build and refit acceleration structures for a single pass.
- [MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md) — Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.
- [MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)
