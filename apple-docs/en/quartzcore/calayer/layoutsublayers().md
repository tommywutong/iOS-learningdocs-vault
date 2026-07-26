---
title: layoutSublayers()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/layoutsublayers()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/layoutsublayers()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/layoutsublayers%28%29.json'
content_hash: 'sha256:3b5cb8e6bc7b26ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# layoutSublayers()

<sub>Instance Method</sub>

Tells the layer to update its layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func layoutSublayers()
```

## Discussion

Subclasses can override this method and use it to implement their own layout algorithm. Your implementation must set the frame of each sublayer managed by the receiver.

The default implementation of this method calls the `layoutSublayers(of:)` method in Swift or `layoutSublayersOfLayer:` method in Objective-C of the layer’s delegate object. If there is no delegate object, or the delegate does not implement that method, this method calls the `layoutSublayers(of:)` method in Swift or `layoutSublayersOfLayer:` method in Objective-C of the object in the [layoutManager](layoutmanager.md) property.

## See Also

### Managing layer resizing and layout

- [layoutManager](layoutmanager.md) — The object responsible for laying out the layer’s sublayers.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the layer’s layout and marks it as needing an update.
- [- layoutIfNeeded](<layoutifneeded().md>) — Recalculate the receiver’s layout, if required.
- [- needsLayout](<needslayout().md>) — Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [autoresizingMask](autoresizingmask.md) — A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [- resizeWithOldSuperlayerSize:](<resize(witholdsuperlayersize_).md>) — Informs the receiver that the size of its superlayer changed.
- [- resizeSublayersWithOldSize:](<resizesublayers(witholdsize_).md>) — Informs the receiver’s sublayers that the receiver’s size has changed.
- [- preferredFrameSize](<preferredframesize().md>) — Returns the preferred size of the layer in the coordinate space of its superlayer.
