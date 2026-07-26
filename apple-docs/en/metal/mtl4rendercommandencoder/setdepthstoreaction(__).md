---
title: 'setDepthStoreAction(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setdepthstoreaction(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthstoreaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setdepthstoreaction%28_%3A%29.json'
content_hash: 'sha256:5f1c24b7f92e6244'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setDepthStoreAction(_:)

<sub>Instance Method</sub>

Configures the store action for the depth attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDepthStoreAction(_ storeAction: MTLStoreAction)
```

## Parameters

- `storeAction` — A store action for the depth attachment that can’t be [MTLStoreActionUnknown](../mtlstoreaction/unknown.md).

## See Also

### Configuring the actions for attachments

- [- setColorStoreAction:atIndex:](<setcolorstoreaction(__index_).md>) — Configures the store action for a color attachment.
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Configures the store action for the stencil attachment.
