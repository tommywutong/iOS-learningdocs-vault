---
title: setNeedsDisplay()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/setneedsdisplay()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setneedsdisplay()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setneedsdisplay%28%29.json'
content_hash: 'sha256:0655cc179bfb098c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setNeedsDisplay()

<sub>Instance Method</sub>

Marks the receiver’s entire bounds rectangle as needing to be redrawn.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsDisplay()
```

## Discussion

You can use this method or the [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) to notify the system that your view’s contents need to be redrawn. This method makes a note of the request and returns immediately. The view is not actually redrawn until the next drawing cycle, at which point all invalidated views are updated.

> [!note] Note
> If your view is backed by a [CAEAGLLayer](../../quartzcore/caeagllayer.md) object, this method has no effect. It is intended for use only with views that use native drawing technologies (such as UIKit and Core Graphics) to render their content.

You should use this method to request that a view be redrawn only when the content or appearance of the view change. If you simply change the geometry of the view, the view is typically not redrawn. Instead, its existing content is adjusted based on the value in the view’s [contentMode](contentmode-swift.property.md) property. Redisplaying the existing content improves performance by avoiding the need to redraw content that has not changed.

## See Also

### Related Documentation

- [contentMode](contentmode-swift.property.md) — A flag used to determine how a view lays out its content when its bounds change.

### Drawing and updating the view

- [- drawRect:](<draw(__).md>) — Draws the view’s image within the passed-in rectangle.
- [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) — Marks the specified rectangle of the receiver as needing to be redrawn.
- [contentScaleFactor](contentscalefactor.md) — The scale factor applied to the view.
- [- tintColorDidChange](<tintcolordidchange().md>) — Called by the system when the tint color property changes.
