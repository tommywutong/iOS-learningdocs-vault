---
title: 'functionHandle(function:stage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinestate/functionhandle(function:stage:)-7uvul'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/functionhandle(function:stage:)-7uvul'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/functionhandle%28function%3Astage%3A%29-7uvul.json'
content_hash: 'sha256:aaa4a5e716af2cf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# functionHandle(function:stage:)

<sub>Instance Method</sub>

Creates a function handle for a shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func functionHandle(function: any MTLFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?
```

## Parameters

- `function` — An [MTLFunction](../mtlfunction.md) instance that represents the shader the method creates a handle for.

- `stage` — An [MTLRenderStages](../mtlrenderstages.md) instance that represents the rendering stage that invokes the shader that `function` represents.

## See Also

### Creating function handles and tables

- [- newVisibleFunctionTableWithDescriptor:stage:](<makevisiblefunctiontable(descriptor_stage_).md>) — Creates a new visible function table.
- [- newIntersectionFunctionTableWithDescriptor:stage:](<makeintersectionfunctiontable(descriptor_stage_).md>) — Creates a new intersection function table.
