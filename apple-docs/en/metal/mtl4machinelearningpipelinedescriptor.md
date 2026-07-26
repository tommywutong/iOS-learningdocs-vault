---
title: MTL4MachineLearningPipelineDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4machinelearningpipelinedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningpipelinedescriptor.json'
content_hash: 'sha256:95e35931dc725324'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4MachineLearningPipelineDescriptor

<sub>Class</sub>

Description for a machine learning pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4MachineLearningPipelineDescriptor
```

## Relationships

- **Inherits From**: [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [label](mtl4machinelearningpipelinedescriptor/label.md) — Assigns an optional string that helps identify pipeline states you create from this descriptor.
- [machineLearningFunctionDescriptor](mtl4machinelearningpipelinedescriptor/machinelearningfunctiondescriptor.md) — Assigns the function that the machine learning pipeline you create from this descriptor executes.

### Instance Methods

- [- inputDimensionsAtBufferIndex:](<mtl4machinelearningpipelinedescriptor/inputdimensions(bufferindex_).md>) — Obtains the dimensions of the input tensor at `bufferIndex` if set, `nil` otherwise.
- [- reset](<mtl4machinelearningpipelinedescriptor/reset().md>) — Resets the descriptor to its default values.
- [- setInputDimensions:atBufferIndex:](<mtl4machinelearningpipelinedescriptor/setinputdimensions(__bufferindex_)-34gir.md>) — Sets the dimension of an input tensor at a buffer index.
- [setInputDimensions(_:bufferIndex:)](<mtl4machinelearningpipelinedescriptor/setinputdimensions(__bufferindex_)-8fnq7.md>) — Sets the dimensions of multiple input tensors on a range of buffer bindings.

## See Also

### Configuring a machine learning pipeline

- [MTL4MachineLearningPipelineReflection](mtl4machinelearningpipelinereflection.md) — Represents reflection information for a machine learning pipeline state.
