---
title: clearColor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpasscolorattachmentdescriptor/clearcolor
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptor/clearcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpasscolorattachmentdescriptor/clearcolor.json'
content_hash: 'sha256:9a8d083eaf615fa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassColorAttachmentDescriptor](../mtlrenderpasscolorattachmentdescriptor.md)

# clearColor

<sub>Instance Property</sub>

The color to use when clearing the color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var clearColor: MTLClearColor { get set }
```

## Discussion

If the [loadAction](../mtlrenderpassattachmentdescriptor/loadaction.md) property of the attachment is set to [MTLLoadActionClear](../mtlloadaction/clear.md), then at the start of a render pass, the GPU fills the texture with the value stored in the [clearColor](clearcolor.md) property. Otherwise, the GPU ignores the [clearColor](clearcolor.md) property.

The [clearColor](clearcolor.md) property represents a set of RGBA components. The default value is `(0.0, 0.0, 0.0, 1.0)` (black). Use the [MTLClearColorMake](<../mtlclearcolormake(________).md>) function to construct an [MTLClearColor](../mtlclearcolor.md) value.

## See Also

### Specifying clearing value

- [MTLClearColorMake](<../mtlclearcolormake(________).md>) — Returns a color value used to clear a color attachment.
