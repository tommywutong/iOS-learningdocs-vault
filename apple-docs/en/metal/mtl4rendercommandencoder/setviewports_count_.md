---
title: 'setViewports:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setviewports:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setviewports:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setviewports%3Acount%3A.json'
content_hash: 'sha256:e66aee1be9ee9444'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setViewports:count:

<sub>Instance Method</sub>

Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setViewports:(const MTLViewport[]) viewports count:(NSUInteger) count;
```

## Parameters

- `viewports` — Array of [MTLViewport](../mtlviewport.md) instances.

- `count` — Number of [MTLViewport](../mtlviewport.md) instances in the array.

## Discussion

Metal clips fragments that lie outside of the viewport, and optionally clamps fragments outside of z-near/z-far range, depending on the value you assign to [- setDepthClipMode:](<setdepthclipmode(__).md>).

Metal selects the viewport to use from the `[[ viewport_array_index ]]` attribute you specify in the pipeline state’s vertex shader function in the Metal Shading Language.

## See Also

### Configuring viewport and scissor behavior

- [- setViewport:](<setviewport(__).md>) — Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [- setScissorRect:](<setscissorrect(__).md>) — Sets a scissor rectangle to discard fragments outside a specific area.
- [setScissorRects:count:](setscissorrects_count_.md) — Sets an array of scissor rectangles for a fragment scissor test.
