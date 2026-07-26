---
title: 'resizeSublayers(withOldSize:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/resizesublayers(witholdsize:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/resizesublayers(witholdsize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/resizesublayers%28witholdsize%3A%29.json'
content_hash: 'sha256:36c905e96d98db20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# resizeSublayers(withOldSize:)

<sub>Instance Method</sub>

Informs the receiver’s sublayers that the receiver’s size has changed.

<sub>Mac Catalyst, macOS</sub>

```swift
func resizeSublayers(withOldSize size: CGSize)
```

## Parameters

- `size` — The previous size of the current layer.

## Discussion

When the [autoresizingMask](autoresizingmask.md) property is used for resizing and the bounds of this layer change, the layer calls this method. The default implementation calls the [- resizeWithOldSuperlayerSize:](<resize(witholdsuperlayersize_).md>) method of each sublayer to let it know its superlayer’s bounds changed. You should not need to call or override this method directly.

## See Also

### Managing layer resizing and layout

- [layoutManager](layoutmanager.md) — The object responsible for laying out the layer’s sublayers.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the layer’s layout and marks it as needing an update.
- [- layoutSublayers](<layoutsublayers().md>) — Tells the layer to update its layout.
- [- layoutIfNeeded](<layoutifneeded().md>) — Recalculate the receiver’s layout, if required.
- [- needsLayout](<needslayout().md>) — Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [autoresizingMask](autoresizingmask.md) — A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [- resizeWithOldSuperlayerSize:](<resize(witholdsuperlayersize_).md>) — Informs the receiver that the size of its superlayer changed.
- [- preferredFrameSize](<preferredframesize().md>) — Returns the preferred size of the layer in the coordinate space of its superlayer.
