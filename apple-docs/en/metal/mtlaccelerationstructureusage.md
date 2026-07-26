---
title: MTLAccelerationStructureUsage
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureusage
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureusage.json'
content_hash: 'sha256:5ef6e785c3418531'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureUsage

<sub>Structure</sub>

Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLAccelerationStructureUsage
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Applying options

- [MTLAccelerationStructureUsageRefit](mtlaccelerationstructureusage/refit.md) — An option that lets you update an acceleration structure after creating it.
- [MTLAccelerationStructureUsagePreferFastBuild](mtlaccelerationstructureusage/preferfastbuild.md) — An option that instructs Metal to build an acceleration structure quickly.
- [MTLAccelerationStructureUsagePreferFastIntersection](mtlaccelerationstructureusage/preferfastintersection.md) — An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [MTLAccelerationStructureUsageMinimizeMemory](mtlaccelerationstructureusage/minimizememory.md) — An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [MTLAccelerationStructureUsageExtendedLimits](mtlaccelerationstructureusage/extendedlimits.md) — An option that increases an acceleration structure’s storage capacity.

### Swift support

- [init(rawValue:)](<mtlaccelerationstructureusage/init(rawvalue_).md>) — Creates new usage options instance from a raw integer value.

## See Also

### Acceleration structures

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md) — Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
- [MTLAccelerationStructure](mtlaccelerationstructure.md) — A collection of model data for GPU-accelerated intersection of rays with the model.
- [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md) — Base class for Metal 4 acceleration structure descriptors.
- [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md) — A base class for classes that define the configuration for a new acceleration structure.
- [MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md) — Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md) — A description of an acceleration structure that contains geometry primitives.
- [MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md) — Descriptor for an instance acceleration structure.
- [MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md) — Encodes commands that build and refit acceleration structures for a single pass.
- [MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)
