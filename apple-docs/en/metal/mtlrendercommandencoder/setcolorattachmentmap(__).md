---
title: 'setColorAttachmentMap(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setcolorattachmentmap(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setcolorattachmentmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setcolorattachmentmap%28_%3A%29.json'
content_hash: 'sha256:632bcf8390514aaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setColorAttachmentMap(_:)

<sub>Instance Method</sub>

Sets the mapping from logical shader color output to physical render pass color attachments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setColorAttachmentMap(_ mapping: MTLLogicalToPhysicalColorAttachmentMap?)
```

## Parameters

- `mapping` — Mapping from logical shader outputs to physical outputs.

## Discussion

Use this method to define how the physical color attachments you specify via [colorAttachments](../mtlrenderpassdescriptor/colorattachments.md) map to the logical color output the fragment shader writes to.

To use this feature, make sure to set [supportColorAttachmentMapping](../mtlrenderpassdescriptor/supportcolorattachmentmapping.md) to [true](../../swift/true.md).

## See Also

### Configuring blend behavior

- [- setBlendColorRed:green:blue:alpha:](<setblendcolor(red_green_blue_alpha_).md>) — Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.
