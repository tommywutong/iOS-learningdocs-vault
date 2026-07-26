---
title: Metal libraries
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/metal-libraries
source_url: 'https://developer.apple.com/documentation/metal/metal-libraries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/metal-libraries.json'
content_hash: 'sha256:52870ce4ec9ebb71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Shader libraries](shader-libraries.md)

# Metal libraries

Compile and manage Metal libraries from the command line.

## Overview

By default, your Metal shaders compile as a format called _Metal intermediate representation_ (Metal IR), a GPU-independent bytecode. At your app’s runtime, Metal compiles this bytecode to a GPU-specific binary for the host device. If you provide your shader functions as strings, they first compile to Metal IR on device, and then go through a secondary compilation for GPU.

Metal source files you add to an app’s source compilation Build Phase compile to a Metal IR library named `default.metallib`. Load this library at runtime by calling the [- newDefaultLibrary](<mtldevice/makedefaultlibrary().md>) method of an [MTLDevice](mtldevice.md) in your app. For more complicated projects, you may want to create individual targets for Metal libraries, modify them in build scripts, or perform other optimizations.

Compilation of Metal IR completes before executing a shader function call. When your library consists of utility functions that other shaders use, use [Metal dynamic libraries](metal-dynamic-libraries.md). To distribute GPU-specific binaries and avoid runtime shader compilation, use [Metal binary archives](metal-binary-archives.md).

## Topics

### Working with Metal intermediate representation libraries

- [Building a shader library by precompiling source files](building-a-shader-library-by-precompiling-source-files.md) — Create a shader library that you can add to an Xcode project with the Metal compiler tools in a command-line environment.
- [Minimizing the binary size of a shader library](minimizing-the-binary-size-of-a-shader-library.md) — Reduce the storage footprint of your shaders, and potentially reduce their compile time, by selecting the Metal compiler’s size optimization option.
- [Generating and loading a Metal library symbol file](generating-and-loading-a-metal-library-symbol-file.md) — Debug your Metal shaders from your production apps by creating companion symbol files at compile time and loading them at debug time.

## See Also

### Shader compilation

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
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — Groups together properties to drive the dynamic linking process of a pipeline stage.
