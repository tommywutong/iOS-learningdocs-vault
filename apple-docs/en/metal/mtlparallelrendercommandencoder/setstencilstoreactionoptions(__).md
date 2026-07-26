---
title: 'setStencilStoreActionOptions(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlparallelrendercommandencoder/setstencilstoreactionoptions(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/setstencilstoreactionoptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlparallelrendercommandencoder/setstencilstoreactionoptions%28_%3A%29.json'
content_hash: 'sha256:aff7443461c1c89f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLParallelRenderCommandEncoder](../mtlparallelrendercommandencoder.md)

# setStencilStoreActionOptions(_:)

<sub>Instance Method</sub>

Specifies known store action options for a given stencil attachment.

> [!warning] Deprecated
> Store action options have no effect on Apple Silicon

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setStencilStoreActionOptions(_ storeActionOptions: MTLStoreActionOptions)
```

## Parameters

- `storeActionOptions` — The additional store action options for the stencil attachment.

## See Also

### Setting render pass state

- [- setColorStoreAction:atIndex:](<setcolorstoreaction(__index_).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given color attachment.
- [- setColorStoreActionOptions:atIndex:](<setcolorstoreactionoptions(__index_).md>) — Specifies known store action options for a given color attachment. _(deprecated)_
- [- setDepthStoreAction:](<setdepthstoreaction(__).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given depth attachment.
- [- setDepthStoreActionOptions:](<setdepthstoreactionoptions(__).md>) — Specifies known store action options for a given depth attachment. _(deprecated)_
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Specifies a known store action to replace the initial [MTLStoreActionUnknown](../mtlstoreaction/unknown.md) value specified for a given stencil attachment.
