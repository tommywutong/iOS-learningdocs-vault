---
title: depthPlane
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/depthplane
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/depthplane'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/depthplane.json'
content_hash: 'sha256:696a271a5e4acca5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# depthPlane

<sub>Instance Property</sub>

The depth plane of the texture used for rendering to the attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var depthPlane: Int { get set }
```

## Discussion

If the texture isn’t a 3D texture, then Metal ignores this property.

The default value is `0`.

## See Also

### Specifying the texture for the attachment

- [texture](texture.md) — The texture object associated with this attachment.
- [level](level.md) — The mipmap level of the texture used for rendering to the attachment.
- [slice](slice.md) — The slice of the texture used for rendering to the attachment.
