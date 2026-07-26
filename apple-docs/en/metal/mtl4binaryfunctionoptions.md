---
title: MTL4BinaryFunctionOptions
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4binaryfunctionoptions
source_url: 'https://developer.apple.com/documentation/metal/mtl4binaryfunctionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4binaryfunctionoptions.json'
content_hash: 'sha256:3d43fcc9da245774'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4BinaryFunctionOptions

<sub>Structure</sub>

Options for configuring the creation of binary functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTL4BinaryFunctionOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<mtl4binaryfunctionoptions/init(rawvalue_).md>)

### Type Properties

- [MTL4BinaryFunctionOptionPipelineIndependent](mtl4binaryfunctionoptions/pipelineindependent.md) — Compiles the function to have its function handles return a constant MTLResourceID across all pipeline states. The function needs to be linked to the pipeline that will use this function.

## See Also

### Shader compilation

- [Metal libraries](metal-libraries.md) — Compile and manage Metal libraries from the command line.
- [Metal dynamic libraries](metal-dynamic-libraries.md) — Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal binary archives](metal-binary-archives.md) — Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
- [MTL4Compiler](mtl4compiler.md) — A abstraction for a pipeline state and shader function compiler.
- [MTL4CompilerDescriptor](mtl4compilerdescriptor.md) — Groups together properties for creating a compiler context.
- [MTL4CompilerTaskOptions](mtl4compilertaskoptions.md) — The configuration options that control the behavior of a compilation task for a Metal 4 compiler instance.
- [MTL4CompilerTaskStatus](mtl4compilertaskstatus.md) — Represents the status of a compiler task.
- [MTL4Archive](mtl4archive.md) — A read-only container that stores pipeline states from a shader compiler.
- [MTL4BinaryFunction](mtl4binaryfunction.md) — Represents a binary function.
- [MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md) — Base interface for other function-derived interfaces.
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — Groups together properties to drive the dynamic linking process of a pipeline stage.
