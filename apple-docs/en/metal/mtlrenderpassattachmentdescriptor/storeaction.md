---
title: storeAction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/storeaction
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/storeaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/storeaction.json'
content_hash: 'sha256:da10852864e6660d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# storeAction

<sub>Instance Property</sub>

The action performed by this attachment at the end of a rendering pass for a render command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var storeAction: MTLStoreAction { get set }
```

## Discussion

If your app doesn’t need the data in the texture after completing the rendering pass, use the [MTLStoreActionDontCare](../mtlstoreaction/dontcare.md) action. Otherwise, use the [MTLStoreActionStore](../mtlstoreaction/store.md) action if the texture is directly stored or the [MTLStoreActionMultisampleResolve](../mtlstoreaction/multisampleresolve.md) action if the texture is a multisampled texture. In some feature sets, you can use the [MTLStoreActionStoreAndMultisampleResolve](../mtlstoreaction/storeandmultisampleresolve.md) action to store and resolve the texture in a single rendering pass. For more information, see:

- [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [Metal feature set tables (Numbers)](https://developer.apple.com/metal/metal-feature-set-tables.zip)

When the store action is either [MTLStoreActionMultisampleResolve](../mtlstoreaction/multisampleresolve.md) or [MTLStoreActionStoreAndMultisampleResolve](../mtlstoreaction/storeandmultisampleresolve.md), the [resolveTexture](resolvetexture.md) property needs to be set to the texture to use as the target for the resolve action. Use the [resolveLevel](resolvelevel.md), [resolveSlice](resolveslice.md), and [resolveDepthPlane](resolvedepthplane.md) properties to specify the mipmap level, cube slice, and depth plane of the resolve texture, respectively.

For color render targets, the default value is [MTLStoreActionStore](../mtlstoreaction/store.md). For depth or stencil render targets, the default value is [MTLStoreActionDontCare](../mtlstoreaction/dontcare.md).

## See Also

### Specifying rendering pass actions

- [loadAction](loadaction.md) — The action performed by this attachment at the start of a rendering pass for a render command encoder.
- [storeActionOptions](storeactionoptions.md) — The options that modify the store action performed by this attachment. _(deprecated)_
