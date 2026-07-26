---
title: resolveSlice
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/resolveslice
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/resolveslice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/resolveslice.json'
content_hash: 'sha256:fc693606061b5337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# resolveSlice

<sub>Instance Property</sub>

The slice of the texture used for the multisample resolve action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var resolveSlice: Int { get set }
```

## Discussion

If the value of [storeAction](storeaction.md) is set to [MTLStoreActionMultisampleResolve](../mtlstoreaction/multisampleresolve.md) or [MTLStoreActionStoreAndMultisampleResolve](../mtlstoreaction/storeandmultisampleresolve.md), set this property to point to a slice in the resolve texture.

The default value is `0`.

## See Also

### Specifying the texture to resolve multisample data

- [resolveTexture](resolvetexture.md) — The destination texture used when resolving multisampled texture data into single sample values.
- [resolveLevel](resolvelevel.md) — The mipmap level of the texture used for the multisample resolve action.
- [resolveDepthPlane](resolvedepthplane.md) — The depth plane of the texture used for the multisample resolve action.
