---
title: computeFunctionDescriptor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4computepipelinedescriptor/computefunctiondescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor/computefunctiondescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computepipelinedescriptor/computefunctiondescriptor.json'
content_hash: 'sha256:d7f7c83d407a6a1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputePipelineDescriptor](../mtl4computepipelinedescriptor.md)

# computeFunctionDescriptor

<sub>Instance Property</sub>

A descriptor representing the compute pipeline’s function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var computeFunctionDescriptor: MTL4FunctionDescriptor? { get set }
```

## Discussion

You don’t assign instances of [MTL4FunctionDescriptor](../mtl4functiondescriptor.md) to this property directly, instead assign an instance of one of its subclasses, such as [MTL4LibraryFunctionDescriptor](../mtl4libraryfunctiondescriptor.md), which represents a function from a Metal library.
