---
title: MTL4LogicalToPhysicalColorAttachmentMappingState
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate
source_url: 'https://developer.apple.com/documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate.json'
content_hash: 'sha256:1e6b727b92b1a2d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4LogicalToPhysicalColorAttachmentMappingState

<sub>Enumeration</sub>

Enumerates possible behaviors of how a pipeline maps its logical outputs to its color attachments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTL4LogicalToPhysicalColorAttachmentMappingState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTL4LogicalToPhysicalColorAttachmentMappingStateIdentity](mtl4logicaltophysicalcolorattachmentmappingstate/identity.md) — Treats the logical color attachment descriptor array for render and tile render pipelines to match the physical one.
- [MTL4LogicalToPhysicalColorAttachmentMappingStateInherited](mtl4logicaltophysicalcolorattachmentmappingstate/inherited.md) — Deduces the color attachment mapping by inheriting it from the color attachment map of the current encoder.

### Initializers

- [init(rawValue:)](<mtl4logicaltophysicalcolorattachmentmappingstate/init(rawvalue_).md>)

## See Also

### Pipeline compilation

- [MTL4BlendState](mtl4blendstate.md) — Enumeration for controlling the blend state of a pipeline state object.
- [MTL4FunctionDescriptor](mtl4functiondescriptor.md) — Base interface for describing a Metal 4 shader function.
- [MTL4IndirectCommandBufferSupportState](mtl4indirectcommandbuffersupportstate.md) — Enumeration for controlling support for [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md).
- [MTL4LibraryDescriptor](mtl4librarydescriptor.md) — Serves as the base descriptor for creating a Metal library.
- [MTL4LibraryFunctionDescriptor](mtl4libraryfunctiondescriptor.md) — Describes a shader function from a Metal library.
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
