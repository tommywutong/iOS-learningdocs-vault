---
title: level
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/level
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/level'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/level.json'
content_hash: 'sha256:6c1c790dea6cc3a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# level

<sub>Instance Property</sub>

The mipmap level of the texture used for rendering to the attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var level: Int { get set }
```

## Discussion

The default value is `0`.

## See Also

### Specifying the texture for the attachment

- [texture](texture.md) — The texture object associated with this attachment.
- [slice](slice.md) — The slice of the texture used for rendering to the attachment.
- [depthPlane](depthplane.md) — The depth plane of the texture used for rendering to the attachment.
