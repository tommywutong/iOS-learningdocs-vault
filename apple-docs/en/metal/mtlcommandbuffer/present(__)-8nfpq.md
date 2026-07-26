---
title: 'present(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 26.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/present(_:)-8nfpq'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:)-8nfpq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/present%28_%3A%29-8nfpq.json'
content_hash: 'sha256:30396ee2e132ab55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# present(_:)

<sub>Instance Method</sub>

Presents a texture resource drawable as early as possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func present(_ drawable: TextureResource.Drawable)
```

## Parameters

- `drawable` — A [TextureResource.Drawable](../../realitykit/textureresource/drawable.md) instance that contains a texture the system can show on a display.

## Discussion

This convenience method calls the drawable’s [- present](<../mtldrawable/present().md>) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [- addScheduledHandler:](<addscheduledhandler(__).md>) method for you.

> [!important] Important
> You can only call this method before calling the command buffer’s [- commit](<commit().md>) method.
