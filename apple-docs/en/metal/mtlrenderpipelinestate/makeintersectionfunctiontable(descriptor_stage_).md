---
title: 'makeIntersectionFunctionTable(descriptor:stage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinestate/makeintersectionfunctiontable(descriptor:stage:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makeintersectionfunctiontable(descriptor:stage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/makeintersectionfunctiontable%28descriptor%3Astage%3A%29.json'
content_hash: 'sha256:4c749b5bf260ac4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# makeIntersectionFunctionTable(descriptor:stage:)

<sub>Instance Method</sub>

Creates a new intersection function table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLIntersectionFunctionTable)?
```

## Parameters

- `descriptor` — An [MTLIntersectionFunctionTableDescriptor](../mtlintersectionfunctiontabledescriptor.md) instance that configures the visible function table the method creates.

- `stage` — An [MTLRenderStages](../mtlrenderstages.md) instance that represents the render pass stage the intersection function table applies to.

## See Also

### Creating function handles and tables

- [- functionHandleWithFunction:stage:](<functionhandle(function_stage_)-7uvul.md>) — Creates a function handle for a shader.
- [- newVisibleFunctionTableWithDescriptor:stage:](<makevisiblefunctiontable(descriptor_stage_).md>) — Creates a new visible function table.
