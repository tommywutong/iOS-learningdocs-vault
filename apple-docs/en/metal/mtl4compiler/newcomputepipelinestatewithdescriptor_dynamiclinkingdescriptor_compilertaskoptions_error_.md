---
title: 'newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor:dynamiclinkingdescriptor:compilertaskoptions:error:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor:dynamiclinkingdescriptor:compilertaskoptions:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor%3Adynamiclinkingdescriptor%3Acompilertaskoptions%3Aerror%3A.json'
content_hash: 'sha256:a8d1684187d94be7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4Compiler](../mtl4compiler.md)

# newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:

<sub>Instance Method</sub>

Creates a new compute pipeline state synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTLComputePipelineState>) newComputePipelineStateWithDescriptor:(MTL4ComputePipelineDescriptor *) descriptor dynamicLinkingDescriptor:(MTL4PipelineStageDynamicLinkingDescriptor *) dynamicLinkingDescriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions error:(NSError **) error;
```

## Parameters

- `descriptor` — A compute pipeline state descriptor describing the pipeline this compiler creates.

- `dynamicLinkingDescriptor` — An optional parameter that provides additional configuration for linking the pipeline state object.

- `compilerTaskOptions` — A description of the compilation process itself, providing parameters that influence execution of the compilation process.

- `error` — An optional parameter into which Metal stores information in case of an error.

## Return Value

A new compute pipeline state object upon success, `nil` otherwise.
