---
title: 'setDepthStoreActionOptions(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlrendercommandencoder/setdepthstoreactionoptions(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthstoreactionoptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setdepthstoreactionoptions%28_%3A%29.json'
content_hash: 'sha256:b567ba274d339847'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setDepthStoreActionOptions(_:)

<sub>Instance Method</sub>

Configures the store action options for the depth attachment.

> [!warning] Deprecated
> Store action options have no effect on Apple Silicon

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthStoreActionOptions(_ storeActionOptions: MTLStoreActionOptions)
```

## Parameters

- `storeActionOptions` — Additional options for the store action of the depth attachment.

## See Also

### Configuring the actions for attachments

- [- setColorStoreAction:atIndex:](<setcolorstoreaction(__index_).md>) — Configures the store action for a color attachment.
- [- setColorStoreActionOptions:atIndex:](<setcolorstoreactionoptions(__index_).md>) — Configures the store action options for a color attachment. _(deprecated)_
- [- setDepthStoreAction:](<setdepthstoreaction(__).md>) — Configures the store action for the depth attachment.
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Configures the store action for the stencil attachment.
- [- setStencilStoreActionOptions:](<setstencilstoreactionoptions(__).md>) — Configures the store action options for the stencil attachment. _(deprecated)_
