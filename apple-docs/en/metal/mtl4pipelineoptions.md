---
title: MTL4PipelineOptions
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelineoptions
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelineoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelineoptions.json'
content_hash: 'sha256:7337bbb82bbcff90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4PipelineOptions

<sub>Class</sub>

Provides options controlling how to compile a pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4PipelineOptions
```

## Overview

You provide these options through the [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md) class at compilation time.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [shaderReflection](mtl4pipelineoptions/shaderreflection.md) — Controls whether to include Metal shader reflection in this pipeline.
- [shaderValidation](mtl4pipelineoptions/shadervalidation.md) — Controls whether to enable or disable Metal Shader Validation for the pipeline.

## See Also

### Pipeline harvesting

- [MTL4PipelineDataSetSerializer](mtl4pipelinedatasetserializer.md) — A fast-addition container for collecting data during pipeline state creation.
- [MTL4PipelineDataSetSerializerConfiguration](mtl4pipelinedatasetserializerconfiguration.md) — Configuration options for pipeline dataset serializer objects.
- [MTL4PipelineDataSetSerializerDescriptor](mtl4pipelinedatasetserializerdescriptor.md) — Groups together properties to create a pipeline data set serializer.
- [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md) — Base type for descriptors you use for building pipeline state objects.
