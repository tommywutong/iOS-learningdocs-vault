---
title: 'setTextureView(texture:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltextureviewpool/settextureview(texture:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltextureviewpool/settextureview(texture:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureviewpool/settextureview%28texture%3Aindex%3A%29.json'
content_hash: 'sha256:5b1ae9f7dbd6c331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureViewPool](../mtltextureviewpool.md)

# setTextureView(texture:index:)

<sub>Instance Method</sub>

Copies a default texture view to a slot in this texture view pool at an index provided.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTextureView(texture: any MTLTexture, index: Int) -> MTLResourceID
```

## Parameters

- `texture` — An [MTLTexture](../mtltexture.md) instance for which to copy its texture view.

- `index` — An index of a slot in this texture pool into which this method copies the texture view.

## Return Value

The [MTLResourceID](../mtlresourceid.md) of a newly created texture view in this pool.
