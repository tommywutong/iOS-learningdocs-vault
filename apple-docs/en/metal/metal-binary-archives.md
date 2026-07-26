---
title: Metal binary archives
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/metal-binary-archives
source_url: 'https://developer.apple.com/documentation/metal/metal-binary-archives'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/metal-binary-archives.json'
content_hash: 'sha256:6bb7b6955afef78b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Shader libraries](shader-libraries.md)

# Metal binary archives

Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.

## Overview

Metal supports the widest range of devices available by compiling to Metal intermediate representation (Metal IR), but this comes with a tradeoff. Metal IR libraries are smaller and more flexible, but your app still needs to compile shader functions for the device’s GPU at runtime. This isn’t always desirable; for example, you might want to precompile shaders you use for visual presentation while your app performs other loading or setup. When you’re ready to increase the size of your application bundle in exchange for avoiding runtime compilation, you can precompile shaders to _binary archives_. Binary archives are GPU-specific slices you ship individually or as part of a larger Metal library.

The Metal translator is part of the Metal compiler that produces binary archives from a combination of Metal IR and a JSON representation of your app’s pipeline state. You run the Metal translator with the `metal-tt` command in Terminal.

To get the most out of binary archives and the Metal translator, read the articles below in order, starting with [Creating binary archives from device-built pipeline state objects](creating-binary-archives-from-device-built-pipeline-state-objects.md).

## Topics

### Working with Metal binary archives

- [Creating binary archives from device-built pipeline state objects](creating-binary-archives-from-device-built-pipeline-state-objects.md) — Write your Metal pipeline states to a binary archive at app runtime, and build binaries for any supported GPU.
- [Manipulating Metal binary archives](manipulating-metal-binary-archives.md) — Split precompiled binaries into individual slices, and combine them back together for targeted distribution.
- [Compiling binary archives from a custom configuration script](compiling-binary-archives-from-a-custom-configuration-script.md) — Define how the Metal translator builds binary archives without precompiled binaries as a starting source.

## See Also

### Shader compilation

- [Metal libraries](metal-libraries.md) — Compile and manage Metal libraries from the command line.
- [Metal dynamic libraries](metal-dynamic-libraries.md) — Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [MTL4Compiler](mtl4compiler.md) — A abstraction for a pipeline state and shader function compiler.
- [MTL4CompilerDescriptor](mtl4compilerdescriptor.md) — Groups together properties for creating a compiler context.
- [MTL4CompilerTaskOptions](mtl4compilertaskoptions.md) — The configuration options that control the behavior of a compilation task for a Metal 4 compiler instance.
- [MTL4CompilerTaskStatus](mtl4compilertaskstatus.md) — Represents the status of a compiler task.
- [MTL4Archive](mtl4archive.md) — A read-only container that stores pipeline states from a shader compiler.
- [MTL4BinaryFunction](mtl4binaryfunction.md) — Represents a binary function.
- [MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md) — Base interface for other function-derived interfaces.
- [MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md) — Options for configuring the creation of binary functions.
- [MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md) — Groups together properties to drive the dynamic linking process of a pipeline stage.
