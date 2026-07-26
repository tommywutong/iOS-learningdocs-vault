---
title: 'setBlendColor(red:green:blue:alpha:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setblendcolor(red:green:blue:alpha:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setblendcolor(red:green:blue:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setblendcolor%28red%3Agreen%3Ablue%3Aalpha%3A%29.json'
content_hash: 'sha256:0730272a9a104639'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setBlendColor(red:green:blue:alpha:)

<sub>Instance Method</sub>

Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)
```

## Parameters

- `red` — A value for the red component for the blend color constant.

- `green` — A value for the green component for the blend color constant.

- `blue` — A value for the blue component for the blend color constant.

- `alpha` — A value for the alpha component for the blend color constant.

## See Also

### Configuring blend behavior

- [- setColorAttachmentMap:](<setcolorattachmentmap(__).md>) — Sets the mapping from logical shader color output to physical render pass color attachments.
