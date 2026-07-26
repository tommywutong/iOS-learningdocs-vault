---
title: nextDrawable()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/nextdrawable()
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/nextdrawable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/nextdrawable%28%29.json'
content_hash: 'sha256:bd57d85eeeb4f8a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# nextDrawable()

<sub>Instance Method</sub>

Waits until a Metal drawable is available, and then returns it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func nextDrawable() -> (any CAMetalDrawable)?
```

## Return Value

A Metal drawable. Use the drawable’s [texture](../cametaldrawable/texture.md) property to configure a [MTLRenderPipelineColorAttachmentDescriptor](../../metal/mtlrenderpipelinecolorattachmentdescriptor.md) object for rendering to the layer.

## Discussion

A [CAMetalLayer](../cametallayer.md) object maintains an internal pool of textures for displaying layer content, each wrapped in a [CAMetalDrawable](../cametaldrawable.md) object. Use this method to retrieve the next available drawable from the pool. If all drawables are in use, the layer waits up to one second for one to become available, after which it returns `nil`. The [allowsNextDrawableTimeout](allowsnextdrawabletimeout.md) property affects this behavior.

This method returns `nil` if the layer’s [pixelFormat](pixelformat.md) or other properties are invalid.

## See Also

### Obtaining a Metal Drawable

- [maximumDrawableCount](maximumdrawablecount.md) — The number of Metal drawables in the resource pool managed by Core Animation.
- [allowsNextDrawableTimeout](allowsnextdrawabletimeout.md) — A Boolean value that determines whether requests for a new buffer expire if the system can’t satisfy them.
