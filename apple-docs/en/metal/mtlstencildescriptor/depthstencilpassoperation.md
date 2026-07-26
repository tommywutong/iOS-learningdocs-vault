---
title: depthStencilPassOperation
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstencildescriptor/depthstencilpassoperation
source_url: 'https://developer.apple.com/documentation/metal/mtlstencildescriptor/depthstencilpassoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstencildescriptor/depthstencilpassoperation.json'
content_hash: 'sha256:9077638771bedd66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilDescriptor](../mtlstencildescriptor.md)

# depthStencilPassOperation

<sub>Instance Property</sub>

The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var depthStencilPassOperation: MTLStencilOperation { get set }
```

## Discussion

The default value is [MTLStencilOperationKeep](../mtlstenciloperation/keep.md), which does not change the current stencil value. For more information on possible values, see [MTLStencilOperation](../mtlstenciloperation.md).

## See Also

### Related Documentation

- [depthCompareFunction](../mtldepthstencildescriptor/depthcomparefunction.md) — The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.

### Configuring stencil functions and operations

- [stencilFailureOperation](stencilfailureoperation.md) — The operation that is performed to update the values in the stencil attachment when the stencil test fails.
- [depthFailureOperation](depthfailureoperation.md) — The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [stencilCompareFunction](stencilcomparefunction.md) — The comparison that is performed between the masked reference value and a masked value in the stencil attachment.
- [MTLStencilOperation](../mtlstenciloperation.md) — The operation performed on a currently stored stencil value when a comparison test passes or fails.
