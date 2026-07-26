---
title: 'setColorStoreAction(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setcolorstoreaction(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setcolorstoreaction(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setcolorstoreaction%28_%3Aindex%3A%29.json'
content_hash: 'sha256:0fb224f9d831631a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setColorStoreAction(_:index:)

<sub>Instance Method</sub>

Configures the store action for a color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setColorStoreAction(_ storeAction: MTLStoreAction, index colorAttachmentIndex: Int)
```

## Parameters

- `storeAction` — A store action for the color attachment that can’t be [MTLStoreActionUnknown](../mtlstoreaction/unknown.md).

- `colorAttachmentIndex` — The index of a color attachment.

## Discussion

This method changes the render command encoder’s store action for a color attachment. You can assign the default store action for a color attachment by configuring the [storeAction](../mtlrenderpassattachmentdescriptor/storeaction.md) property of its [MTLRenderPassColorAttachmentDescriptor](../mtlrenderpasscolorattachmentdescriptor.md) (see [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) and its [colorAttachments](../mtlrenderpassdescriptor/colorattachments.md) property).

> [!important] Important
> You need to call this method before calling the encoder’s [- endEncoding](<../mtlcommandencoder/endencoding().md>) method, but only for color attachments with a [storeAction](../mtlrenderpassattachmentdescriptor/storeaction.md) property equal to [MTLStoreActionUnknown](../mtlstoreaction/unknown.md).

## See Also

### Configuring the actions for attachments

- [- setColorStoreActionOptions:atIndex:](<setcolorstoreactionoptions(__index_).md>) — Configures the store action options for a color attachment. _(deprecated)_
- [- setDepthStoreAction:](<setdepthstoreaction(__).md>) — Configures the store action for the depth attachment.
- [- setDepthStoreActionOptions:](<setdepthstoreactionoptions(__).md>) — Configures the store action options for the depth attachment. _(deprecated)_
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Configures the store action for the stencil attachment.
- [- setStencilStoreActionOptions:](<setstencilstoreactionoptions(__).md>) — Configures the store action options for the stencil attachment. _(deprecated)_
