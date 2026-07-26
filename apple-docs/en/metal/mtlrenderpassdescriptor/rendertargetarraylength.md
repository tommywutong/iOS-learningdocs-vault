---
title: renderTargetArrayLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/rendertargetarraylength
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/rendertargetarraylength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/rendertargetarraylength.json'
content_hash: 'sha256:184d02a7fdcc6fed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# renderTargetArrayLength

<sub>Instance Property</sub>

The number of active layers that all attachments need to have for layered rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderTargetArrayLength: Int { get set }
```

## Discussion

The default value is `0`, indicating that the GPU does not use layered rendering on this render pass.

The table below gives typical values you might set, depending on the type of texture being used as attachments in the render pass. Your vertex shader need to select the render target array index between `0` and the array length minus `1`.

| Texture Type | Typical Length |
|---|---|
| [MTLTextureType1DArray](../mtltexturetype/type1darray.md) or [MTLTextureType2DArray](../mtltexturetype/type2darray.md) | The length of the texture array ([arrayLength](../mtltexture/arraylength.md)) |
| [MTLTextureTypeCube](../mtltexturetype/typecube.md) | 6 |
| [MTLTextureTypeCubeArray](../mtltexturetype/typecubearray.md) | 6 times the length of the texture array ([arrayLength](../mtltexture/arraylength.md)) |

## See Also

### Layered rendering

- [renderTargetWidth](rendertargetwidth.md) — The width, in pixels, to constrain the render target to.
- [renderTargetHeight](rendertargetheight.md) — The height, in pixels, to constrain the render target to.
