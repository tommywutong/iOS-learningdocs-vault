---
title: 'setViewports(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setviewports(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setviewports(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setviewports%28_%3A%29.json'
content_hash: 'sha256:aa832b546de4b9e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setViewports(_:)

<sub>Instance Method</sub>

Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setViewports(_ viewports: [MTLViewport])
```

## Parameters

- `viewports` — A Swift array of [MTLViewport](../mtlviewport.md) elements.

## Discussion

Metal clips fragments that lie outside of the viewport, and optionally clamps fragments outside of z-near/z-far range, depending on the value you assign to [- setDepthClipMode:](<setdepthclipmode(__).md>).

Metal selects the viewport to use from the `[[ viewport_array_index ]]` attribute you specify in the pipeline state’s vertex shader function in the Metal Shading Language.

## See Also

### Configuring viewport and scissor behavior

- [- setViewport:](<setviewport(__).md>) — Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [- setScissorRect:](<setscissorrect(__).md>) — Sets a scissor rectangle to discard fragments outside a specific area.
- [setScissorRects(_:)](<setscissorrects(__).md>) — Sets an array of scissor rectangles for a fragment scissor test.
