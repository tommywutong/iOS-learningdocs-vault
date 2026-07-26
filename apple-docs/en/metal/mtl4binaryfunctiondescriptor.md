---
title: MTL4BinaryFunctionDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4binaryfunctiondescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4binaryfunctiondescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4binaryfunctiondescriptor.json'
content_hash: 'sha256:56f0637a8dfe74be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4BinaryFunctionDescriptor

<sub>Class</sub>

Base interface for other function-derived interfaces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4BinaryFunctionDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [functionDescriptor](mtl4binaryfunctiondescriptor/functiondescriptor.md) — Provides the function descriptor corresponding to the function to compile into a binary function.
- [name](mtl4binaryfunctiondescriptor/name.md) — Associates a string that uniquely identifies a binary function.
- [options](mtl4binaryfunctiondescriptor/options.md) — Configure the options to use at binary function creation time.

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
- [MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md) — Options for configuring the creation of binary functions.
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — Groups together properties to drive the dynamic linking process of a pipeline stage.
