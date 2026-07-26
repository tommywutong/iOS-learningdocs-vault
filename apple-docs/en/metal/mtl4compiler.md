---
title: MTL4Compiler
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4compiler
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler.json'
content_hash: 'sha256:460dddb1626dd21b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4Compiler

<sub>Protocol</sub>

A abstraction for a pipeline state and shader function compiler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4Compiler : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [device](mtl4compiler/device.md) — Returns the device that this compiler belongs to.
- [label](mtl4compiler/label.md) — Returns the optional label you specify at creation time.
- [pipelineDataSetSerializer](mtl4compiler/pipelinedatasetserializer.md) — Returns the pipeline data set serializer into which this compiler stores data for all pipelines it creates.

### Instance Methods

- [makeBinaryFunction(descriptor:compilerTaskOptions:)](<mtl4compiler/makebinaryfunction(descriptor_compilertaskoptions_)-5o46e.md>) — Creates a new binary visible or intersection function synchronously.
- [makeBinaryFunction(descriptor:compilerTaskOptions:)](<mtl4compiler/makebinaryfunction(descriptor_compilertaskoptions_)-hkc4.md>) — Creates a new binary visible or intersection function asynchronously.
- [makeComputePipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)](<mtl4compiler/makecomputepipelinestate(descriptor_dynamiclinkingdescriptor_compilertaskoptions_)-19x.md>) — Creates a new compute pipeline state asynchronously.
- [makeComputePipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)](<mtl4compiler/makecomputepipelinestate(descriptor_dynamiclinkingdescriptor_compilertaskoptions_)-7dqdm.md>) — Creates a new compute pipeline state object synchronously.
- [- newDynamicLibrary:error:](<mtl4compiler/makedynamiclibrary(library_).md>) — Creates a new dynamic library from a library containing Metal IR code synchronously.
- [- newDynamicLibraryWithURL:error:](<mtl4compiler/makedynamiclibrary(url_).md>) — Creates a new dynamic library from the contents of a file at an URL location synchronously.
- [- newLibraryWithDescriptor:error:](<mtl4compiler/makelibrary(descriptor_).md>) — Creates a new Metal library synchronously.
- [makeMachineLearningPipelineState(descriptor:)](<mtl4compiler/makemachinelearningpipelinestate(descriptor_)-36hxx.md>) — Creates a new machine learning pipeline state asynchronously.
- [makeMachineLearningPipelineState(descriptor:)](<mtl4compiler/makemachinelearningpipelinestate(descriptor_)-909v1.md>) — Creates a new ML pipeline state with descriptor.
- [makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)](<mtl4compiler/makerenderpipelinestate(descriptor_dynamiclinkingdescriptor_compilertaskoptions_)-66wsk.md>) — Creates a new render pipeline state asynchronously.
- [makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)](<mtl4compiler/makerenderpipelinestate(descriptor_dynamiclinkingdescriptor_compilertaskoptions_)-84kox.md>) — Creates a new render pipeline state synchronously.
- [makeRenderPipelineStateBySpecialization(descriptor:pipeline:)](<mtl4compiler/makerenderpipelinestatebyspecialization(descriptor_pipeline_)-2636j.md>) — Creates a new render pipeline state from another, previously unspecialized, pipeline state.
- [makeRenderPipelineStateBySpecialization(descriptor:pipeline:)](<mtl4compiler/makerenderpipelinestatebyspecialization(descriptor_pipeline_)-7s2wp.md>) — Creates a new render pipeline state from another, previously unspecialized, pipeline state

## See Also

### Shader compilation

- [Metal libraries](metal-libraries.md) — Compile and manage Metal libraries from the command line.
- [Metal dynamic libraries](metal-dynamic-libraries.md) — Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal binary archives](metal-binary-archives.md) — Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
- [MTL4CompilerDescriptor](mtl4compilerdescriptor.md) — Groups together properties for creating a compiler context.
- [MTL4CompilerTaskOptions](mtl4compilertaskoptions.md) — The configuration options that control the behavior of a compilation task for a Metal 4 compiler instance.
- [MTL4CompilerTaskStatus](mtl4compilertaskstatus.md) — Represents the status of a compiler task.
- [MTL4Archive](mtl4archive.md) — A read-only container that stores pipeline states from a shader compiler.
- [MTL4BinaryFunction](mtl4binaryfunction.md) — Represents a binary function.
- [MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md) — Base interface for other function-derived interfaces.
- [MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md) — Options for configuring the creation of binary functions.
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — Groups together properties to drive the dynamic linking process of a pipeline stage.
