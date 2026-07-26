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
doc_path: '/documentation/metal/mtlparallelrendercommandencoder/setcolorstoreaction(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/setcolorstoreaction(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlparallelrendercommandencoder/setcolorstoreaction%28_%3Aindex%3A%29.json'
content_hash: 'sha256:2a64154fc1de3274'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLParallelRenderCommandEncoder](../mtlparallelrendercommandencoder.md)

# setColorStoreAction(_:index:)

<sub>Instance Method</sub>

Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setColorStoreAction(_ storeAction: MTLStoreAction, index colorAttachmentIndex: Int)
```

## Parameters

- `storeAction` — The desired store action for the color attachment. This value can’t be [MTLStoreActionUnknown](../mtlstoreaction/unknown.md).

- `colorAttachmentIndex` — The index of the color attachment.

## Discussion

If the store action for the given color attachment was set to [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) when the parallel render command encoder was created, you need to call this method to specify another store action before you call the [- endEncoding](<../mtlcommandencoder/endencoding().md>) method.

## See Also

### Setting render pass state

- [- setColorStoreActionOptions:atIndex:](<setcolorstoreactionoptions(__index_).md>) — Specifies known store action options for a given color attachment. _(deprecated)_
- [- setDepthStoreAction:](<setdepthstoreaction(__).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [- setDepthStoreActionOptions:](<setdepthstoreactionoptions(__).md>) — Specifies known store action options for a given depth attachment. _(deprecated)_
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given stencil attachment.
- [- setStencilStoreActionOptions:](<setstencilstoreactionoptions(__).md>) — Specifies known store action options for a given stencil attachment. _(deprecated)_
