---
title: loadAction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/loadaction
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/loadaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/loadaction.json'
content_hash: 'sha256:6b8d25285413d6a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# loadAction

<sub>Instance Property</sub>

The action performed by this attachment at the start of a rendering pass for a render command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var loadAction: MTLLoadAction { get set }
```

## Discussion

If your app renders all pixels of the render target for a given frame, use the [MTLLoadActionDontCare](../mtlloadaction/dontcare.md) action, which allows the GPU to avoid loading the existing contents of the texture. Otherwise, use the [MTLLoadActionClear](../mtlloadaction/clear.md) action to clear the previous contents of the render target or the [MTLLoadActionLoad](../mtlloadaction/load.md) action to preserve them. The [MTLLoadActionClear](../mtlloadaction/clear.md) action also avoids the cost of loading the existing texture contents, but it still incurs the cost of filling the destination with a clear color.

For color render targets, the default value is [MTLLoadActionDontCare](../mtlloadaction/dontcare.md). For depth or stencil render targets, the default value is [MTLLoadActionClear](../mtlloadaction/clear.md).

## See Also

### Specifying rendering pass actions

- [storeAction](storeaction.md) — The action performed by this attachment at the end of a rendering pass for a render command encoder.
- [storeActionOptions](storeactionoptions.md) — The options that modify the store action performed by this attachment. _(deprecated)_
