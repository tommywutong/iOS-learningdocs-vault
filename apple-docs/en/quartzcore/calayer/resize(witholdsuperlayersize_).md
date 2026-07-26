---
title: 'resize(withOldSuperlayerSize:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/resize(witholdsuperlayersize:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/resize(witholdsuperlayersize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/resize%28witholdsuperlayersize%3A%29.json'
content_hash: 'sha256:0ef9b6a6fe95288a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# resize(withOldSuperlayerSize:)

<sub>Instance Method</sub>

Informs the receiver that the size of its superlayer changed.

<sub>Mac Catalyst, macOS</sub>

```swift
func resize(withOldSuperlayerSize size: CGSize)
```

## Parameters

- `size` — The previous size of the superlayer.

## Discussion

When the [autoresizingMask](autoresizingmask.md) property is used for resizing and the bounds of a layer change, that layer calls this method on each of its sublayers. Sublayers use this method to adjust their own frame rectangles to reflect the new superlayer bounds, which can be retrieved directly from the superlayer. The old size of the superlayer is passed to this method so that the sublayer has that information for any calculations it must make.

## See Also

### Managing layer resizing and layout

- [layoutManager](layoutmanager.md) — The object responsible for laying out the layer’s sublayers.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the layer’s layout and marks it as needing an update.
- [- layoutSublayers](<layoutsublayers().md>) — Tells the layer to update its layout.
- [- layoutIfNeeded](<layoutifneeded().md>) — Recalculate the receiver’s layout, if required.
- [- needsLayout](<needslayout().md>) — Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [autoresizingMask](autoresizingmask.md) — A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [- resizeSublayersWithOldSize:](<resizesublayers(witholdsize_).md>) — Informs the receiver’s sublayers that the receiver’s size has changed.
- [- preferredFrameSize](<preferredframesize().md>) — Returns the preferred size of the layer in the coordinate space of its superlayer.
