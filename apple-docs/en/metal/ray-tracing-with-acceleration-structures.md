---
title: Ray tracing with acceleration structures
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/ray-tracing-with-acceleration-structures
source_url: 'https://developer.apple.com/documentation/metal/ray-tracing-with-acceleration-structures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/ray-tracing-with-acceleration-structures.json'
content_hash: 'sha256:88f9e6cc143ca277'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# Ray tracing with acceleration structures

<sub>API Collection</sub>

Build a representation of your scene’s geometry using triangles and bounding volumes to quickly trace rays through the scene.

## Overview

Ray tracing can improve your content’s realism by more accurately modeling the behavior of light than traditional rendering. You can also use ray tracing to implement similar techniques that rely on line-of-sight, such as sound obstruction or visually based AI functions.

To apply ray tracing in your app:

1. Create acceleration structures that represent objects in a scene.
2. Define a ray’s behavior when it collides into parts of an acceleration structure by creating either intersectors or intersection queries.
3. Generate rays into the scene from a new or existing shader.

An _intersector_ uses a table of your intersection functions that define the custom behavior for each intersection type. An _intersection query_ returns to your calling function to handle the custom behavior for all intersection types.

Intersectors work with compute kernels on all GPUs, and with render shaders only on Apple silicon GPUs. Alternatively, your app can use intersection queries on non-Apple GPUs, or for porting code from other graphics APIs.

## Topics

### Ray tracing samples

- [Accelerating ray tracing using Metal](accelerating-ray-tracing-using-metal.md) — Implement ray-traced rendering using GPU-based parallel processing.
- [Control the ray tracing process using intersection queries](control-the-ray-tracing-process-using-intersection-queries.md) — Explicitly enumerate a ray’s intersections with acceleration structures by creating an intersection query object.
- [Rendering reflections in real time using ray tracing](rendering-reflections-in-real-time-using-ray-tracing.md) — Implement realistic real-time lighting by dynamically generating reflection maps by encoding a ray-tracing compute pass.
- [Rendering a curve primitive in a ray tracing scene](rendering-a-curve-primitive-in-a-ray-tracing-scene.md) — Implement ray traced rendering using GPU-based parallel processing.

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
- [MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md) — Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.
- [MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)

### Acceleration structures passes

- [MTLAccelerationStructurePassDescriptor](mtlaccelerationstructurepassdescriptor.md)
- [MTLAccelerationStructurePassSampleBufferAttachmentDescriptor](mtlaccelerationstructurepasssamplebufferattachmentdescriptor.md)
- [MTLAccelerationStructurePassSampleBufferAttachmentDescriptorArray](mtlaccelerationstructurepasssamplebufferattachmentdescriptorarray.md)

### Geometry descriptors

- [MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md) — Base class for all Metal 4 acceleration structure geometry descriptors.
- [MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md) — A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md) — Describes triangle geometry suitable for ray tracing.
- [MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md) — A description of a list of triangle primitives to turn into an acceleration structure.
- [MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md) — Describes curve geometry suitable for ray tracing.
- [MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md) — A descriptor you configure with curve geometry for building acceleration structures.
- [MTLCurveType](mtlcurvetype.md)
- [MTLCurveBasis](mtlcurvebasis.md)
- [MTLCurveEndCaps](mtlcurveendcaps.md)
- [MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md) — Describes bounding-box geometry suitable for ray tracing.
- [MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes to turn into an acceleration structure.

### Motion geometry descriptors

- [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md) — Describes motion triangle geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) — A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md) — Describes motion curve geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md) — Describes motion bounding box geometry, suitable for motion ray tracing.
- [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) — A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [MTLMotionKeyframeData](mtlmotionkeyframedata.md) — Geometry data for a specific keyframe to use in a moving instance.

### Instance descriptors

- [MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure.
- [MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md) — Options for adjusting the behavior of an instanced acceleration structure.
- [MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md) — Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.

### Intersection function tables

- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md) — A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
- [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) — A specification of how to create an intersection function table.
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md) — A description of an intersection function that performs an intersection test.
- [MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature.md) — Constants for specifying different types of custom intersection functions.
- [MTLIntersectionFunctionBufferArguments](mtlintersectionfunctionbufferarguments.md)

### Supporting types

- [MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-swift.typealias.md) — The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](mtlpackedfloat3-swift.typealias.md) — }
- [MTLPackedFloat4x3](mtlpackedfloat4x3-swift.typealias.md) — A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.
- [MTLPackedFloat3Make](<mtlpackedfloat3make(______).md>) — Returns a new packed vector with three floating-point values.
- [MTL4BufferRange](mtl4bufferrange.md)
- [MTL4BufferRangeMake](<mtl4bufferrangemake(____).md>)

## See Also

### Command encoders

- [Render passes](render-passes.md) — Encode a render pass to draw graphics into an image.
- [Compute passes](compute-passes.md) — Encode a compute pass that runs computations in parallel on a thread grid, processing and manipulating Metal resource data on multiple cores of a GPU.
- [Machine learning passes](machine-learning-passes.md) — Add machine learning model inference to your Metal app’s GPU workflow.
- [Blit passes](blit-passes.md) — Encode a block information transfer pass to adjust and copy data to and from GPU resources, such as buffers and textures.
- [Indirect command encoding](indirect-command-encoding.md) — Store draw commands in Metal buffers and run them at a later time on the GPU, either once or repeatedly.
