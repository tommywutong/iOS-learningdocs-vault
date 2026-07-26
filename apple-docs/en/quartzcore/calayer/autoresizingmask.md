---
title: autoresizingMask
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/autoresizingmask
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/autoresizingmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/autoresizingmask.json'
content_hash: 'sha256:686ef964a6eaf06f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# autoresizingMask

<sub>Instance Property</sub>

A bitmask defining how the layer is resized when the bounds of its superlayer changes.

<sub>Mac Catalyst, macOS</sub>

```swift
var autoresizingMask: CAAutoresizingMask { get set }
```

## Discussion

If your app does not use a layout manager or constraints to handle layout changes, you can assign a value to this property to adjust the layer’s size in response to changes in the superlayer’s bounds. For a list of possible values, see [CAAutoresizingMask](../caautoresizingmask.md).

The default value of this property is [kCALayerNotSizable](../caautoresizingmask/kcalayernotsizable.md).

## See Also

### Managing layer resizing and layout

- [layoutManager](layoutmanager.md) — The object responsible for laying out the layer’s sublayers.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the layer’s layout and marks it as needing an update.
- [- layoutSublayers](<layoutsublayers().md>) — Tells the layer to update its layout.
- [- layoutIfNeeded](<layoutifneeded().md>) — Recalculate the receiver’s layout, if required.
- [- needsLayout](<needslayout().md>) — Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [- resizeWithOldSuperlayerSize:](<resize(witholdsuperlayersize_).md>) — Informs the receiver that the size of its superlayer changed.
- [- resizeSublayersWithOldSize:](<resizesublayers(witholdsize_).md>) — Informs the receiver’s sublayers that the receiver’s size has changed.
- [- preferredFrameSize](<preferredframesize().md>) — Returns the preferred size of the layer in the coordinate space of its superlayer.
