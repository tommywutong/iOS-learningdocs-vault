---
title: stencilFailureOperation
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstencildescriptor/stencilfailureoperation
source_url: 'https://developer.apple.com/documentation/metal/mtlstencildescriptor/stencilfailureoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstencildescriptor/stencilfailureoperation.json'
content_hash: 'sha256:f84cac5f1ad771d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilDescriptor](../mtlstencildescriptor.md)

# stencilFailureOperation

<sub>Instance Property</sub>

The operation that is performed to update the values in the stencil attachment when the stencil test fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stencilFailureOperation: MTLStencilOperation { get set }
```

## Discussion

The default value is [MTLStencilOperationKeep](../mtlstenciloperation/keep.md), which does not change the current stencil value. For more information on possible values, see [MTLStencilOperation](../mtlstenciloperation.md).

When the stencil test fails for a pixel, its incoming color, depth, or stencil values are discarded.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Configuring stencil functions and operations

- [depthFailureOperation](depthfailureoperation.md) — The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [depthStencilPassOperation](depthstencilpassoperation.md) — The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.
- [stencilCompareFunction](stencilcomparefunction.md) — The comparison that is performed between the masked reference value and a masked value in the stencil attachment.
- [MTLStencilOperation](../mtlstenciloperation.md) — The operation performed on a currently stored stencil value when a comparison test passes or fails.
