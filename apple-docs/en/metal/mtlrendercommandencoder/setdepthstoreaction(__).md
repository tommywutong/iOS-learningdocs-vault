---
title: 'setDepthStoreAction(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setdepthstoreaction(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthstoreaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setdepthstoreaction%28_%3A%29.json'
content_hash: 'sha256:a3f96d35bd910c13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setDepthStoreAction(_:)

<sub>Instance Method</sub>

Configures the store action for the depth attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthStoreAction(_ storeAction: MTLStoreAction)
```

## Parameters

- `storeAction` — A store action for the depth attachment that can’t be [MTLStoreActionUnknown](../mtlstoreaction/unknown.md).

## Discussion

This method changes the render command encoder’s store action for the depth attachment. You can assign the default store action for the depth attachment by configuring the [storeAction](../mtlrenderpassattachmentdescriptor/storeaction.md) property of its [MTLRenderPassDepthAttachmentDescriptor](../mtlrenderpassdepthattachmentdescriptor.md) (see [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) and its [depthAttachment](../mtlrenderpassdescriptor/depthattachment.md) property).

> [!important] Important
> You need to call this method before calling the encoder’s [- endEncoding](<../mtlcommandencoder/endencoding().md>) method, but only if the depth attachment’s [storeAction](../mtlrenderpassattachmentdescriptor/storeaction.md) property is equal to [MTLStoreActionUnknown](../mtlstoreaction/unknown.md).

## See Also

### Configuring the actions for attachments

- [- setColorStoreAction:atIndex:](<setcolorstoreaction(__index_).md>) — Configures the store action for a color attachment.
- [- setColorStoreActionOptions:atIndex:](<setcolorstoreactionoptions(__index_).md>) — Configures the store action options for a color attachment. _(deprecated)_
- [- setDepthStoreActionOptions:](<setdepthstoreactionoptions(__).md>) — Configures the store action options for the depth attachment. _(deprecated)_
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Configures the store action for the stencil attachment.
- [- setStencilStoreActionOptions:](<setstencilstoreactionoptions(__).md>) — Configures the store action options for the stencil attachment. _(deprecated)_
