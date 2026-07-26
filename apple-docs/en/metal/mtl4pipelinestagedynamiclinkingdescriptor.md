---
title: MTL4PipelineStageDynamicLinkingDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor.json'
content_hash: 'sha256:f4ceba34a9de322c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4PipelineStageDynamicLinkingDescriptor

<sub>Class</sub>

Groups together properties to drive the dynamic linking process of a pipeline stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4PipelineStageDynamicLinkingDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [binaryLinkedFunctions](mtl4pipelinestagedynamiclinkingdescriptor/binarylinkedfunctions.md) — Provides the array of binary functions to link.
- [maxCallStackDepth](mtl4pipelinestagedynamiclinkingdescriptor/maxcallstackdepth.md) — Limits the maximum depth of the call stack for indirect function calls in the pipeline stage function.
- [preloadedLibraries](mtl4pipelinestagedynamiclinkingdescriptor/preloadedlibraries.md) — Provides an array of dynamic libraries the compiler loads when it builds the pipeline.

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
- [MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md) — Options for configuring the creation of binary functions.
