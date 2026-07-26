---
title: 'setTextureView(texture:descriptor:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltextureviewpool/settextureview(texture:descriptor:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltextureviewpool/settextureview(texture:descriptor:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureviewpool/settextureview%28texture%3Adescriptor%3Aindex%3A%29.json'
content_hash: 'sha256:28ab10c2f44ab096'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureViewPool](../mtltextureviewpool.md)

# setTextureView(texture:descriptor:index:)

<sub>Instance Method</sub>

Creates a new lightweight texture view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTextureView(texture: any MTLTexture, descriptor: MTLTextureViewDescriptor, index: Int) -> MTLResourceID
```

## Parameters

- `texture` — An [MTLTexture](../mtltexture.md) instance for which to create a new lightweight texture view.

- `descriptor` — A descriptor specifying properties of the texture view to create.

- `index` — An index of a slot in the texture pool into which this method writes the new texture view.

## Return Value

The [MTLResourceID](../mtlresourceid.md) of a newly created texture view in this pool.

## Discussion

This method creates a lightweight texture view over a texture according to a descriptor you provide. It then associates the texture view with a slot in this texture view pool at the index you specify.
