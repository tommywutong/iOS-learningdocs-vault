---
title: 'setScissorRects(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setscissorrects(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setscissorrects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setscissorrects%28_%3A%29.json'
content_hash: 'sha256:91aaec89ad3e1f8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setScissorRects(_:)

<sub>Instance Method</sub>

Sets an array of scissor rectangles for a fragment scissor test.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setScissorRects(_ scissorRects: [MTLScissorRect])
```

## Parameters

- `scissorRects` — A Swift array of [MTLScissorRect](../mtlscissorrect.md) elements.

## Discussion

Metal uses the specific scissor rectangle corresponding to the index you specify via the `[[ viewport_array_index ]]` output attribute of the vertex shader function in the Metal Shading Language, discarding all fragments outside of the scissor rect.

## See Also

### Configuring viewport and scissor behavior

- [- setViewport:](<setviewport(__).md>) — Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [setViewports(_:)](<setviewports(__).md>) — Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [- setScissorRect:](<setscissorrect(__).md>) — Sets a scissor rectangle to discard fragments outside a specific area.
