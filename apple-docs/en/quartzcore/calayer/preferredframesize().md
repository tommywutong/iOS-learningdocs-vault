---
title: preferredFrameSize()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/preferredframesize()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/preferredframesize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/preferredframesize%28%29.json'
content_hash: 'sha256:c4a04f90c6d9ae46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# preferredFrameSize()

<sub>Instance Method</sub>

Returns the preferred size of the layer in the coordinate space of its superlayer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func preferredFrameSize() -> CGSize
```

## Return Value

The layer’s preferred frame size.

## Discussion

In macOS, the default implementation of this method calls the `preferredSize(of:)` method in Swift or the `preferredSizeOfLayer:` method in Objective-C of its layout manager—that is, the object in its [layoutManager](layoutmanager.md) property. If that object does not exist or does not implement that method, this method returns the size of the layer’s current [bounds](bounds.md) rectangle mapped into the coordinate space of its [superlayer](superlayer.md).

## See Also

### Managing layer resizing and layout

- [layoutManager](layoutmanager.md) — The object responsible for laying out the layer’s sublayers.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the layer’s layout and marks it as needing an update.
- [- layoutSublayers](<layoutsublayers().md>) — Tells the layer to update its layout.
- [- layoutIfNeeded](<layoutifneeded().md>) — Recalculate the receiver’s layout, if required.
- [- needsLayout](<needslayout().md>) — Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [autoresizingMask](autoresizingmask.md) — A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [- resizeWithOldSuperlayerSize:](<resize(witholdsuperlayersize_).md>) — Informs the receiver that the size of its superlayer changed.
- [- resizeSublayersWithOldSize:](<resizesublayers(witholdsize_).md>) — Informs the receiver’s sublayers that the receiver’s size has changed.
