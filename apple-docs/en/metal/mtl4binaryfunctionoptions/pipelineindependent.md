---
title: pipelineIndependent
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4binaryfunctionoptions/pipelineindependent
source_url: 'https://developer.apple.com/documentation/metal/mtl4binaryfunctionoptions/pipelineindependent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4binaryfunctionoptions/pipelineindependent.json'
content_hash: 'sha256:544b9c807dfcaea4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4BinaryFunctionOptions](../mtl4binaryfunctionoptions.md)

# pipelineIndependent

<sub>Type Property</sub>

Compiles the function to have its function handles return a constant MTLResourceID across all pipeline states. The function needs to be linked to the pipeline that will use this function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var pipelineIndependent: MTL4BinaryFunctionOptions { get }
```
