---
title: MTL4PipelineDataSetSerializerConfiguration
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelinedatasetserializerconfiguration
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializerconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelinedatasetserializerconfiguration.json'
content_hash: 'sha256:69341e7428254528'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4PipelineDataSetSerializerConfiguration

<sub>Structure</sub>

Configuration options for pipeline dataset serializer objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTL4PipelineDataSetSerializerConfiguration
```

## Overview

Use these options to enable different functionality in instances of [MTL4PipelineDataSetSerializer](mtl4pipelinedatasetserializer.md).

You can combine these values via a logical `OR` and set it to [configuration](mtl4pipelinedatasetserializerdescriptor/configuration.md) to specify desired level of serialization support for instances of [MTL4PipelineDataSetSerializer](mtl4pipelinedatasetserializer.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<mtl4pipelinedatasetserializerconfiguration/init(rawvalue_).md>)

### Type Properties

- [MTL4PipelineDataSetSerializerConfigurationCaptureBinaries](mtl4pipelinedatasetserializerconfiguration/capturebinaries.md) — Enables serializing pipeline binary functions.
- [MTL4PipelineDataSetSerializerConfigurationCaptureDescriptors](mtl4pipelinedatasetserializerconfiguration/capturedescriptors.md) — Enables serializing pipeline scripts.

## See Also

### Pipeline harvesting

- [MTL4PipelineDataSetSerializer](mtl4pipelinedatasetserializer.md) — A fast-addition container for collecting data during pipeline state creation.
- [MTL4PipelineDataSetSerializerDescriptor](mtl4pipelinedatasetserializerdescriptor.md) — Groups together properties to create a pipeline data set serializer.
- [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md) — Base type for descriptors you use for building pipeline state objects.
- [MTL4PipelineOptions](mtl4pipelineoptions.md) — Provides options controlling how to compile a pipeline state.
