---
title: 'setTexture(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4argumenttable/settexture(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4argumenttable/settexture(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4argumenttable/settexture%28_%3Aindex%3A%29.json'
content_hash: 'sha256:95f0c238cc151cae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ArgumentTable](../mtl4argumenttable.md)

# setTexture(_:index:)

<sub>Instance Method</sub>

Binds a texture to a texture binding slot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTexture(_ resourceID: MTLResourceID, index bindingIndex: Int)
```

## Parameters

- `resourceID` — The [MTLResourceID](../mtlresourceid.md) of the [MTLTexture](../mtltexture.md) instance to bind.

- `bindingIndex` — A valid binding index in the texture binding range. It is an error for this value to match or exceed the value of property [maxTextureBindCount](../mtl4argumenttabledescriptor/maxtexturebindcount.md) on the descriptor from which you created this argument table.
