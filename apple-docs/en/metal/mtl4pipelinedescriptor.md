---
title: MTL4PipelineDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelinedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelinedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelinedescriptor.json'
content_hash: 'sha256:9b99cab8cadf9e67'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4PipelineDescriptor

<sub>Class</sub>

Base type for descriptors you use for building pipeline state objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4PipelineDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md), [MTL4MachineLearningPipelineDescriptor](mtl4machinelearningpipelinedescriptor.md), [MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md), [MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md), [MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [label](mtl4pipelinedescriptor/label.md) — Assigns an optional string that uniquely identifies a pipeline descriptor.
- [options](mtl4pipelinedescriptor/options.md) — Provides compile-time options when you build the pipeline.

## See Also

### Pipeline harvesting

- [MTL4PipelineDataSetSerializer](mtl4pipelinedatasetserializer.md) — A fast-addition container for collecting data during pipeline state creation.
- [MTL4PipelineDataSetSerializerConfiguration](mtl4pipelinedatasetserializerconfiguration.md) — Configuration options for pipeline dataset serializer objects.
- [MTL4PipelineDataSetSerializerDescriptor](mtl4pipelinedatasetserializerdescriptor.md) — Groups together properties to create a pipeline data set serializer.
- [MTL4PipelineOptions](mtl4pipelineoptions.md) — Provides options controlling how to compile a pipeline state.
