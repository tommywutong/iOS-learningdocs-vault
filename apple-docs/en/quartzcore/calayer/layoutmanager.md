---
title: layoutManager
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/layoutmanager
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/layoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/layoutmanager.json'
content_hash: 'sha256:a09b6ac2185caac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# layoutManager

<sub>Instance Property</sub>

The object responsible for laying out the layer’s sublayers.

<sub>Mac Catalyst, macOS</sub>

```swift
var layoutManager: (any CALayoutManager)? { get set }
```

## Discussion

The object you assign to this property must nominally implement the CALayoutManager Informal Protocol informal protocol. If the layer’s delegate does not handle layout updates, the object assigned to this property is given a chance to update the layout of the layer’s sublayers.

In macOS, assign an instance of the [CAConstraintLayoutManager](../caconstraintlayoutmanager.md) class to this property if your layer uses layer-based constraints to handle layout changes.

The default value of this property is `nil`.

## See Also

### Managing layer resizing and layout

- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the layer’s layout and marks it as needing an update.
- [- layoutSublayers](<layoutsublayers().md>) — Tells the layer to update its layout.
- [- layoutIfNeeded](<layoutifneeded().md>) — Recalculate the receiver’s layout, if required.
- [- needsLayout](<needslayout().md>) — Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [autoresizingMask](autoresizingmask.md) — A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [- resizeWithOldSuperlayerSize:](<resize(witholdsuperlayersize_).md>) — Informs the receiver that the size of its superlayer changed.
- [- resizeSublayersWithOldSize:](<resizesublayers(witholdsize_).md>) — Informs the receiver’s sublayers that the receiver’s size has changed.
- [- preferredFrameSize](<preferredframesize().md>) — Returns the preferred size of the layer in the coordinate space of its superlayer.
