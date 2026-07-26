---
title: writeMask
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/writemask
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/writemask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/writemask.json'
content_hash: 'sha256:9e013c3a2aa734ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineColorAttachmentDescriptor](../mtlrenderpipelinecolorattachmentdescriptor.md)

# writeMask

<sub>Instance Property</sub>

A bitmask that restricts which color channels are written into the texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var writeMask: MTLColorWriteMask { get set }
```

## Discussion

The default value of `writeMask` is all ones, [MTLColorWriteMaskAll](../mtlcolorwritemask/all.md), which allows all color channels to be blended. The `MTLColorWriteMask` values `MTLColorWriteMaskRed`, `MTLColorWriteMaskGreen`, `MTLColorWriteMaskBlue`, and `MTLColorWriteMaskAlpha` limit blending to one color channel, and these values can be bitwise combined. `MTLColorWriteMaskNone` does not allow any color channels to be blended.

## See Also

### Configuring render pipeline states

- [pixelFormat](pixelformat.md) — The pixel format of the color attachment’s texture.
- [MTLColorWriteMask](../mtlcolorwritemask.md) — Values used to specify a mask to permit or restrict writing to color channels of a color value.
