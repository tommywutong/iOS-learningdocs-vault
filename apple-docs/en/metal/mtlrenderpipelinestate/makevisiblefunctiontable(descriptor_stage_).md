---
title: 'makeVisibleFunctionTable(descriptor:stage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinestate/makevisiblefunctiontable(descriptor:stage:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makevisiblefunctiontable(descriptor:stage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/makevisiblefunctiontable%28descriptor%3Astage%3A%29.json'
content_hash: 'sha256:3204a11beca976c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# makeVisibleFunctionTable(descriptor:stage:)

<sub>Instance Method</sub>

Creates a new visible function table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLVisibleFunctionTable)?
```

## Parameters

- `descriptor` — An [MTLVisibleFunctionTableDescriptor](../mtlvisiblefunctiontabledescriptor.md) instance that configures the visible function table the method creates.

- `stage` — An [MTLRenderStages](../mtlrenderstages.md) instance that represents the render pass stage the visible function table applies to.

## See Also

### Creating function handles and tables

- [- functionHandleWithFunction:stage:](<functionhandle(function_stage_)-7uvul.md>) — Creates a function handle for a shader.
- [- newIntersectionFunctionTableWithDescriptor:stage:](<makeintersectionfunctiontable(descriptor_stage_).md>) — Creates a new intersection function table.
