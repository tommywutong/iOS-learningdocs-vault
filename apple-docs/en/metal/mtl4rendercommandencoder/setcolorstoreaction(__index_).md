---
title: 'setColorStoreAction(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setcolorstoreaction(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setcolorstoreaction(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setcolorstoreaction%28_%3Aindex%3A%29.json'
content_hash: 'sha256:d682ef13b32c7e78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

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

## See Also

### Configuring the actions for attachments

- [- setDepthStoreAction:](<setdepthstoreaction(__).md>) — Configures the store action for the depth attachment.
- [- setStencilStoreAction:](<setstencilstoreaction(__).md>) — Configures the store action for the stencil attachment.
