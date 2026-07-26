---
title: 'setScissorRect(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setscissorrect(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setscissorrect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setscissorrect%28_%3A%29.json'
content_hash: 'sha256:2bb52297d71c5acd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setScissorRect(_:)

<sub>Instance Method</sub>

Sets a scissor rectangle to discard fragments outside a specific area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setScissorRect(_ rect: MTLScissorRect)
```

## Parameters

- `rect` — [MTLScissorRect](../mtlscissorrect.md) rectangle to specify. This rectangle needs to lie completely within the current render attachment.

## Discussion

Metal performs a scissor test and discards all fragments outside of the scissor rect.

## See Also

### Configuring viewport and scissor behavior

- [- setViewport:](<setviewport(__).md>) — Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [setViewports(_:)](<setviewports(__).md>) — Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [setScissorRects(_:)](<setscissorrects(__).md>) — Sets an array of scissor rectangles for a fragment scissor test.
