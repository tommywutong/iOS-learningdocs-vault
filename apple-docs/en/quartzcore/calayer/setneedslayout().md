---
title: setNeedsLayout()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/setneedslayout()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/setneedslayout()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/setneedslayout%28%29.json'
content_hash: 'sha256:a456f687435d6523'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# setNeedsLayout()

<sub>Instance Method</sub>

Invalidates the layer’s layout and marks it as needing an update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setNeedsLayout()
```

## Discussion

You can call this method to indicate that the layout of a layer’s sublayers has changed and must be updated. The system typically calls this method automatically when the layer’s bounds change or when sublayers are added or removed. In macOS, if your layer’s [layoutManager](layoutmanager.md) property contains an object that implements the `invalidateLayout(of:)` method in Swift or the `invalidateLayoutOfLayer:` method in Objective-C, the system calls that method too.

During the next update cycle, the system calls the [- layoutSublayers](<layoutsublayers().md>) method of any layers requiring layout updates.

## See Also

### Managing layer resizing and layout

- [layoutManager](layoutmanager.md) — The object responsible for laying out the layer’s sublayers.
- [- layoutSublayers](<layoutsublayers().md>) — Tells the layer to update its layout.
- [- layoutIfNeeded](<layoutifneeded().md>) — Recalculate the receiver’s layout, if required.
- [- needsLayout](<needslayout().md>) — Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [autoresizingMask](autoresizingmask.md) — A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [- resizeWithOldSuperlayerSize:](<resize(witholdsuperlayersize_).md>) — Informs the receiver that the size of its superlayer changed.
- [- resizeSublayersWithOldSize:](<resizesublayers(witholdsize_).md>) — Informs the receiver’s sublayers that the receiver’s size has changed.
- [- preferredFrameSize](<preferredframesize().md>) — Returns the preferred size of the layer in the coordinate space of its superlayer.
