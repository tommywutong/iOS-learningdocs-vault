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
doc_path: '/documentation/metal/mtlparallelrendercommandencoder/setcolorstoreactionoptions(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/setcolorstoreactionoptions(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlparallelrendercommandencoder/setcolorstoreactionoptions%28_%3Aindex%3A%29.json'
content_hash: 'sha256:5c3ce56aced9beca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLParallelRenderCommandEncoder](../mtlparallelrendercommandencoder.md)

# setColorStoreActionOptions(_:index:)

<sub>Instance Method</sub>

Specifies known store action options for a given color attachment.

> [!warning] Deprecated
> Store action options have no effect on Apple Silicon

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setColorStoreActionOptions(_ storeActionOptions: MTLStoreActionOptions, index colorAttachmentIndex: Int)
```

## Parameters

- `storeActionOptions` — The additional store action options for the color attachment.

- `colorAttachmentIndex` — The index of the color attachment.

## See Also

### Setting render pass state

- [- setColorStoreAction:atIndex:](<setcolorstoreaction(__index_).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given color attachment.
- [- setDepthStoreAction:](<setdepthstoreaction(__).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [- setDepthStoreActionOptions:](<setdepthstoreactionoptions(__).md>) — Specifies known store action options for a given depth attachment. _(deprecated)_
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given stencil attachment.
- [- setStencilStoreActionOptions:](<setstencilstoreactionoptions(__).md>) — Specifies known store action options for a given stencil attachment. _(deprecated)_
