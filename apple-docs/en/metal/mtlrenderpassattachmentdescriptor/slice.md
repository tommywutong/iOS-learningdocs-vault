---
title: slice
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/slice
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/slice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/slice.json'
content_hash: 'sha256:eb46ecca2c127a22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# slice

<sub>Instance Property</sub>

The slice of the texture used for rendering to the attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var slice: Int { get set }
```

## Discussion

The default value is `0`.

## See Also

### Specifying the texture for the attachment

- [texture](texture.md) — The texture object associated with this attachment.
- [level](level.md) — The mipmap level of the texture used for rendering to the attachment.
- [depthPlane](depthplane.md) — The depth plane of the texture used for rendering to the attachment.
