---
title: MTL4Archive
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4archive
source_url: 'https://developer.apple.com/documentation/metal/mtl4archive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4archive.json'
content_hash: 'sha256:90c61a65883a608a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4Archive

<sub>Protocol</sub>

A read-only container that stores pipeline states from a shader compiler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4Archive : NSObjectProtocol, Sendable
```

## Overview

The pipeline states can have intermediate representation (IR) binaries, GPU- and system-specific binaries, or a combination.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the archive

- [label](mtl4archive/label.md) — A label that you can associate with this archive.

### Instance Methods

- [- newBinaryFunctionWithDescriptor:error:](<mtl4archive/makebinaryfunction(descriptor_).md>) — Synchronously creates a binary version of a GPU visible function or GPU intersection function.
- [makeComputePipelineState(descriptor:dynamicLinkingDescriptor:)](<mtl4archive/makecomputepipelinestate(descriptor_dynamiclinkingdescriptor_).md>) — Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.
- [makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:)](<mtl4archive/makerenderpipelinestate(descriptor_dynamiclinkingdescriptor_).md>) — Creates a render pipeline state from the archive with a render descriptor and a dynamic linking descriptor.

## See Also

### Shader compilation

- [Metal libraries](metal-libraries.md) — Compile and manage Metal libraries from the command line.
- [Metal dynamic libraries](metal-dynamic-libraries.md) — Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal binary archives](metal-binary-archives.md) — Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
- [MTL4Compiler](mtl4compiler.md) — A abstraction for a pipeline state and shader function compiler.
- [MTL4CompilerDescriptor](mtl4compilerdescriptor.md) — Groups together properties for creating a compiler context.
- [MTL4CompilerTaskOptions](mtl4compilertaskoptions.md) — The configuration options that control the behavior of a compilation task for a Metal 4 compiler instance.
- [MTL4CompilerTaskStatus](mtl4compilertaskstatus.md) — Represents the status of a compiler task.
- [MTL4BinaryFunction](mtl4binaryfunction.md) — Represents a binary function.
- [MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md) — Base interface for other function-derived interfaces.
- [MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md) — Options for configuring the creation of binary functions.
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — Groups together properties to drive the dynamic linking process of a pipeline stage.
