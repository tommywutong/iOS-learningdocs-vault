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
doc_path: '/documentation/metal/mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-7dqdm'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-7dqdm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/makecomputepipelinestate%28descriptor%3Adynamiclinkingdescriptor%3Acompilertaskoptions%3A%29-7dqdm.json'
content_hash: 'sha256:f9eb0e1aefde609a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# makeComputePipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)

<sub>Instance Method</sub>

Creates a new compute pipeline state object synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor? = nil, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) throws -> any MTLComputePipelineState
```

## Parameters

- `descriptor` — A compute pipeline state descriptor describing the pipeline this compiler creates.

- `compilerTaskOptions` — A description of the compilation process itself, providing parameters that influence execution of the compilation process.

## Return Value

A new compute pipeline state object upon success, otherwise this method throws.
