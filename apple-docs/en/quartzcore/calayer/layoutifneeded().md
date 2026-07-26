---
title: layoutIfNeeded()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/layoutifneeded()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/layoutifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/layoutifneeded%28%29.json'
content_hash: 'sha256:439dfc7bf2eb8a53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# layoutIfNeeded()

<sub>Instance Method</sub>

Recalculate the receiver’s layout, if required.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func layoutIfNeeded()
```

## Discussion

When this message is received, the layer’s super layers are traversed until a ancestor layer is found that does not require layout. Then layout is performed on the entire layer-tree beneath that ancestor.

## See Also

### Managing layer resizing and layout

- [layoutManager](layoutmanager.md) — The object responsible for laying out the layer’s sublayers.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the layer’s layout and marks it as needing an update.
- [- layoutSublayers](<layoutsublayers().md>) — Tells the layer to update its layout.
- [- needsLayout](<needslayout().md>) — Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [autoresizingMask](autoresizingmask.md) — A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [- resizeWithOldSuperlayerSize:](<resize(witholdsuperlayersize_).md>) — Informs the receiver that the size of its superlayer changed.
- [- resizeSublayersWithOldSize:](<resizesublayers(witholdsize_).md>) — Informs the receiver’s sublayers that the receiver’s size has changed.
- [- preferredFrameSize](<preferredframesize().md>) — Returns the preferred size of the layer in the coordinate space of its superlayer.
