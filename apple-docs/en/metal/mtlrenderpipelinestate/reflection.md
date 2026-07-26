---
title: reflection
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/reflection
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/reflection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/reflection.json'
content_hash: 'sha256:edf6aef99e70a2f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# reflection

<sub>Instance Property</sub>

The render pipeline’s reflection information, if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var reflection: MTLRenderPipelineReflection? { get }
```

## Discussion

The property is `nil` by default to help reduce your app’s memory footprint, but you can create reflection information when your app needs it.

Create reflection information by building a pipeline from an [MTL4Compiler](../mtl4compiler.md) instance with the following steps:

1. Configure the [shaderReflection](../mtl4pipelineoptions/shaderreflection.md) property of an [MTL4PipelineOptions](../mtl4pipelineoptions.md) instance.
2. Assign that instance to the [options](../mtl4pipelinedescriptor/options.md) property of an [MTL4PipelineDescriptor](../mtl4pipelinedescriptor.md) instance.
3. Create a compute pipeline state by passing that pipeline descriptor to one of the [MTL4Compiler](../mtl4compiler.md) instance’s methods.

The property is `nil` when you create a pipeline state from an[MTLDevice](../mtldevice.md) instance, such as with its [- newRenderPipelineStateWithDescriptor:error:](<../mtldevice/makerenderpipelinestate(descriptor_).md>) method.
