---
title: resolveTexture
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/resolvetexture
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/resolvetexture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/resolvetexture.json'
content_hash: 'sha256:14eb22467a05031f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# resolveTexture

<sub>Instance Property</sub>

The destination texture used when resolving multisampled texture data into single sample values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var resolveTexture: (any MTLTexture)? { get set }
```

## Discussion

If the [storeAction](storeaction.md) value is set to [MTLStoreActionMultisampleResolve](../mtlstoreaction/multisampleresolve.md) or [MTLStoreActionStoreAndMultisampleResolve](../mtlstoreaction/storeandmultisampleresolve.md), then the [resolveTexture](resolvetexture.md) value needs to point to a valid texture. Otherwise, Metal ignores this property.

## See Also

### Specifying the texture to resolve multisample data

- [resolveLevel](resolvelevel.md) — The mipmap level of the texture used for the multisample resolve action.
- [resolveSlice](resolveslice.md) — The slice of the texture used for the multisample resolve action.
- [resolveDepthPlane](resolvedepthplane.md) — The depth plane of the texture used for the multisample resolve action.
