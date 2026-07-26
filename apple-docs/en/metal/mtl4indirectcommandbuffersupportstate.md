---
title: MTL4IndirectCommandBufferSupportState
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectcommandbuffersupportstate
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectcommandbuffersupportstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectcommandbuffersupportstate.json'
content_hash: 'sha256:8159097d9a67d106'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4IndirectCommandBufferSupportState

<sub>Enumeration</sub>

Enumeration for controlling support for [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTL4IndirectCommandBufferSupportState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTL4IndirectCommandBufferSupportStateDisabled](mtl4indirectcommandbuffersupportstate/disabled.md) — Disables support for indirect command buffers.
- [MTL4IndirectCommandBufferSupportStateEnabled](mtl4indirectcommandbuffersupportstate/enabled.md) — Enables support for indirect command buffers.

### Initializers

- [init(rawValue:)](<mtl4indirectcommandbuffersupportstate/init(rawvalue_).md>)

## See Also

### Pipeline compilation

- [MTL4BlendState](mtl4blendstate.md) — Enumeration for controlling the blend state of a pipeline state object.
- [MTL4FunctionDescriptor](mtl4functiondescriptor.md) — Base interface for describing a Metal 4 shader function.
- [MTL4LibraryDescriptor](mtl4librarydescriptor.md) — Serves as the base descriptor for creating a Metal library.
- [MTL4LibraryFunctionDescriptor](mtl4libraryfunctiondescriptor.md) — Describes a shader function from a Metal library.
- [MTL4LogicalToPhysicalColorAttachmentMappingState](mtl4logicaltophysicalcolorattachmentmappingstate.md) — Enumerates possible behaviors of how a pipeline maps its logical outputs to its color attachments.
- [MTL4NewBinaryFunctionCompletionHandler](mtl4newbinaryfunctioncompletionhandler.md) — Provides a signature for a callback block that Metal calls when the compiler finishes a build task for a binary function.
- [MTL4NewMachineLearningPipelineStateCompletionHandler](mtl4newmachinelearningpipelinestatecompletionhandler.md) — Provides a signature for a callback block that Metal calls when the compiler finishes a build task for a machine learning pipeline state.
- [MTL4ShaderReflection](mtl4shaderreflection.md) — Option mask for requesting reflection information at pipeline build time.
- [MTL4SpecializedFunctionDescriptor](mtl4specializedfunctiondescriptor.md) — Groups together properties to configure and create a specialized function by passing it to a factory method.
- [MTL4AlphaToCoverageState](mtl4alphatocoveragestate.md) — Enumeration for controlling alpha-to-coverage state of a pipeline state object.
- [MTL4AlphaToOneState](mtl4alphatoonestate.md) — Enumeration for controlling alpha-to-one state of a pipeline state object.
- [MTL4StaticLinkingDescriptor](mtl4staticlinkingdescriptor.md) — Groups together properties to drive a static linking process.
- [MTL4StitchedFunctionDescriptor](mtl4stitchedfunctiondescriptor.md) — Groups together properties that describe a shader function suitable for stitching.
- [MTLFunctionReflection](mtlfunctionreflection.md) — Represents a reflection object containing information about a function in a Metal library.
- [MTLNewDynamicLibraryCompletionHandler](mtlnewdynamiclibrarycompletionhandler.md)
