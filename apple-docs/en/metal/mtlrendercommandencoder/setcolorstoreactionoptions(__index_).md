---
title: 'setColorStoreActionOptions(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlrendercommandencoder/setcolorstoreactionoptions(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setcolorstoreactionoptions(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setcolorstoreactionoptions%28_%3Aindex%3A%29.json'
content_hash: 'sha256:a12a64161cc7811c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setColorStoreActionOptions(_:index:)

<sub>Instance Method</sub>

Configures the store action options for a color attachment.

> [!warning] Deprecated
> Store action options have no effect on Apple Silicon

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setColorStoreActionOptions(_ storeActionOptions: MTLStoreActionOptions, index colorAttachmentIndex: Int)
```

## Parameters

- `storeActionOptions` — Additional options for the store action of a color attachment.

- `colorAttachmentIndex` — The index of a color attachment.

## See Also

### Configuring the actions for attachments

- [- setColorStoreAction:atIndex:](<setcolorstoreaction(__index_).md>) — Configures the store action for a color attachment.
- [- setDepthStoreAction:](<setdepthstoreaction(__).md>) — Configures the store action for the depth attachment.
- [- setDepthStoreActionOptions:](<setdepthstoreactionoptions(__).md>) — Configures the store action options for the depth attachment. _(deprecated)_
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Configures the store action for the stencil attachment.
- [- setStencilStoreActionOptions:](<setstencilstoreactionoptions(__).md>) — Configures the store action options for the stencil attachment. _(deprecated)_
