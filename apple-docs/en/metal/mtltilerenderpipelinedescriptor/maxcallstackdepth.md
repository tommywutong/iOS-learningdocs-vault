---
title: maxCallStackDepth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltilerenderpipelinedescriptor/maxcallstackdepth
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/maxcallstackdepth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinedescriptor/maxcallstackdepth.json'
content_hash: 'sha256:5e8fd82b4ec3bc54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)

# maxCallStackDepth

<sub>Instance Property</sub>

The maximum call stack depth for indirect function calls in tile shaders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxCallStackDepth: Int { get set }
```

## Discussion

The property’s default value is `1`. Change its value if you use recursive functions in your tile dispatch.

The maximum call stack depth applies only to indirect function calls in your shader, and affects the upper bound of stack memory for each thread. Indirect function calls include those to visible functions, intersection functions, and to dynamic libraries.

> [!tip] Tip
> To avoid a runtime performance impact, keep this value as small as possible because the framework reserves a large call stack.

## See Also

### Specifying graphics functions and associated data

- [tileFunction](tilefunction.md) — The compute kernel or fragment function the pipeline calls.
- [tileBuffers](tilebuffers.md) — An array that contains the buffer mutability options for a render pipeline’s tile function.
