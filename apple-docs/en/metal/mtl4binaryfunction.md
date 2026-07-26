---
title: MTL4BinaryFunction
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4binaryfunction
source_url: 'https://developer.apple.com/documentation/metal/mtl4binaryfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4binaryfunction.json'
content_hash: 'sha256:864dfb31ac865c4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4BinaryFunction

<sub>Protocol</sub>

Represents a binary function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4BinaryFunction : NSObjectProtocol, Sendable
```

## Overview

A binary function is a shader that you precompile from Metal IR to GPU machine code.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [functionType](mtl4binaryfunction/functiontype.md) — Describes the type of this binary function.
- [name](mtl4binaryfunction/name.md) — Obtains the optional name of this binary function.

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
- [MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md) — Base interface for other function-derived interfaces.
- [MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md) — Options for configuring the creation of binary functions.
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — Groups together properties to drive the dynamic linking process of a pipeline stage.
