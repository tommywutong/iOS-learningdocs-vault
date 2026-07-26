---
title: 'makeComputePipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-19x'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-19x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makecomputepipelinestate%28descriptor%3Adynamiclinkingdescriptor%3Acompilertaskoptions%3A%29-19x.json'
content_hash: 'sha256:342d1b21fcded33b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeComputePipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)

<sub>Instance Method</sub>

Creates a new compute pipeline state asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor? = nil, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) async throws -> any MTLComputePipelineState
```

## Parameters

- `descriptor` — A compute pipeline state descriptor, describing the compute pipeline to create.

- `dynamicLinkingDescriptor` — An optional parameter that provides additional configuration for linking the pipeline state object.

- `compilerTaskOptions` — A description of the compilation process itself, providing parameters that influence execution of the compilation process.

## Return Value

A compute pipeline state upon success, otherwise this method throws.
