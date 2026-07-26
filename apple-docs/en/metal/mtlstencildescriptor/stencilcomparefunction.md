---
title: stencilCompareFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstencildescriptor/stencilcomparefunction
source_url: 'https://developer.apple.com/documentation/metal/mtlstencildescriptor/stencilcomparefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstencildescriptor/stencilcomparefunction.json'
content_hash: 'sha256:e5c405f8b69f02ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilDescriptor](../mtlstencildescriptor.md)

# stencilCompareFunction

<sub>Instance Property</sub>

The comparison that is performed between the masked reference value and a masked value in the stencil attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stencilCompareFunction: MTLCompareFunction { get set }
```

## Discussion

For example, if `stencilCompareFunction` is [MTLCompareFunctionLess](../mtlcomparefunction/less.md), then the stencil test passes if the masked reference value is less than the masked stored stencil value. The default value is [MTLCompareFunctionAlways](../mtlcomparefunction/always.md), which indicates that the stencil test always passes.

The stored stencil value and the reference value are both _masked_ by performing a logical AND operation with the [readMask](readmask.md) value before the comparison takes place. For more information on possible values, see [MTLCompareFunction](../mtlcomparefunction.md).

## See Also

### Related Documentation

- [- setStencilReferenceValue:](<../mtlrendercommandencoder/setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.

### Configuring stencil functions and operations

- [stencilFailureOperation](stencilfailureoperation.md) — The operation that is performed to update the values in the stencil attachment when the stencil test fails.
- [depthFailureOperation](depthfailureoperation.md) — The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [depthStencilPassOperation](depthstencilpassoperation.md) — The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.
- [MTLStencilOperation](../mtlstenciloperation.md) — The operation performed on a currently stored stencil value when a comparison test passes or fails.
