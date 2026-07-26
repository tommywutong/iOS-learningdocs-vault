---
title: resolveLevel
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/resolvelevel
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/resolvelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/resolvelevel.json'
content_hash: 'sha256:d3cd9c2451e6ff1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# resolveLevel

<sub>Instance Property</sub>

The mipmap level of the texture used for the multisample resolve action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var resolveLevel: Int { get set }
```

## Discussion

If the value of [storeAction](storeaction.md) is set to [MTLStoreActionMultisampleResolve](../mtlstoreaction/multisampleresolve.md) or [MTLStoreActionStoreAndMultisampleResolve](../mtlstoreaction/storeandmultisampleresolve.md), set this property to point to a mipmap in the resolve texture.

The default value is `0`.

## See Also

### Specifying the texture to resolve multisample data

- [resolveTexture](resolvetexture.md) — The destination texture used when resolving multisampled texture data into single sample values.
- [resolveSlice](resolveslice.md) — The slice of the texture used for the multisample resolve action.
- [resolveDepthPlane](resolvedepthplane.md) — The depth plane of the texture used for the multisample resolve action.
