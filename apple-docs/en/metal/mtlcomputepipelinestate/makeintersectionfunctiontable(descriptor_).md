---
title: 'makeIntersectionFunctionTable(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputepipelinestate/makeintersectionfunctiontable(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/makeintersectionfunctiontable(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/makeintersectionfunctiontable%28descriptor%3A%29.json'
content_hash: 'sha256:5735759e32fff978'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# makeIntersectionFunctionTable(descriptor:)

<sub>Instance Method</sub>

Creates a new intersection function table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor) -> (any MTLIntersectionFunctionTable)?
```

## Parameters

- `descriptor` — An [MTLIntersectionFunctionTableDescriptor](../mtlintersectionfunctiontabledescriptor.md) instance that configures the created table.

## Return Value

A new intersection function table, or `nil` if an error occurred in creation.

## See Also

### Creating function tables

- [- newVisibleFunctionTableWithDescriptor:](<makevisiblefunctiontable(descriptor_).md>) — Creates a new visible function table.
