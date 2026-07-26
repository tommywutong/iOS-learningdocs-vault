---
title: Metal dynamic libraries
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/metal-dynamic-libraries
source_url: 'https://developer.apple.com/documentation/metal/metal-dynamic-libraries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/metal-dynamic-libraries.json'
content_hash: 'sha256:9b00a05bef9a5855'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Shader libraries](shader-libraries.md)

# Metal dynamic libraries

Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.

## Overview

As shaders grow in size, complexity, and scope, they often end up sharing utility functions. Under the default compilation model in Metal, linking embeds libraries, similar to static linking with the LLVM linker. For Metal, embedding libraries in this manner has two consequences: an increase in binary size, and an increase in compilation time. As each library loads, it compiles its own version of any utility functions, meaning Metal compiles and duplicates your utility functions multiple times.

To avoid this problem, Metal offers dynamic libraries, similar to an LLVM dynamically shared library. Your app loads and compiles dynamic libraries for the device GPU once, the first time a shader requests them. Subsequent shader calls use these compiled utility functions instead of compiling a separate version of the same shader binary.

To support Metal dynamic libraries in your app, call [- newDynamicLibrary:error:](<mtldevice/makedynamiclibrary(library_).md>) with a dynamic library that you bundle as part of your app. Then add it to a pipeline descriptor’s dynamic library information through a property like [preloadedLibraries](mtlcomputepipelinedescriptor/preloadedlibraries.md).

## Topics

### Working with Metal dynamic libraries

- [Compiling and linking Metal dynamic libraries](compiling-and-linking-metal-dynamic-libraries.md) — Build a Metal dynamic library from the command line, allowing for runtime loading of shared shaders.
- [Creating a Metal dynamic library](creating-a-metal-dynamic-library.md) — Compile a library of shaders and write it to a file as a dynamically linked library.

## See Also

### Shader compilation

- [Metal libraries](metal-libraries.md) — Compile and manage Metal libraries from the command line.
- [Metal binary archives](metal-binary-archives.md) — Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
- [MTL4Compiler](mtl4compiler.md) — A abstraction for a pipeline state and shader function compiler.
- [MTL4CompilerDescriptor](mtl4compilerdescriptor.md) — Groups together properties for creating a compiler context.
- [MTL4CompilerTaskOptions](mtl4compilertaskoptions.md) — The configuration options that control the behavior of a compilation task for a Metal 4 compiler instance.
- [MTL4CompilerTaskStatus](mtl4compilertaskstatus.md) — Represents the status of a compiler task.
- [MTL4Archive](mtl4archive.md) — A read-only container that stores pipeline states from a shader compiler.
- [MTL4BinaryFunction](mtl4binaryfunction.md) — Represents a binary function.
- [MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md) — Base interface for other function-derived interfaces.
- [MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md) — Options for configuring the creation of binary functions.
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — Groups together properties to drive the dynamic linking process of a pipeline stage.
