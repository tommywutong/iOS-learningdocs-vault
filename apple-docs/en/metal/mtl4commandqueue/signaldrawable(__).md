---
title: 'signalDrawable(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/signaldrawable(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/signaldrawable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/signaldrawable%28_%3A%29.json'
content_hash: 'sha256:ad240372e3397442'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# signalDrawable(_:)

<sub>Instance Method</sub>

Schedules a signal operation on the command queue to indicate when rendering to a Metal drawable is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func signalDrawable(_ drawable: any MTLDrawable)
```

## Parameters

- `drawable` — [MTLDrawable](../mtldrawable.md) instance to signal.

## Discussion

Signaling when rendering to a [MTLDrawable](../mtldrawable.md) instance is complete indicates that it’s safe to present it to the display.

You are responsible for calling this method after committing all command buffers that contain commands targeting this drawable, and before calling [- present](<../mtldrawable/present().md>), [- presentAtTime:](<../mtldrawable/present(at_).md>), or [- presentAfterMinimumDuration:](<../mtldrawable/present(afterminimumduration_).md>).

> [!note] Note
> This method doesn’t trigger the presentation of the drawable, and fails if you call it after any of the present methods, or if you call it multiple times.

Metal doesn’t guarantee that command buffers you commit to the command queue after calling this method execute before presentation.
