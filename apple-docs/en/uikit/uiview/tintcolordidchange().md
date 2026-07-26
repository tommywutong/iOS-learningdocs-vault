---
title: tintColorDidChange()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/tintcolordidchange()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/tintcolordidchange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/tintcolordidchange%28%29.json'
content_hash: 'sha256:224a326945aef55d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# tintColorDidChange()

<sub>Instance Method</sub>

Called by the system when the tint color property changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func tintColorDidChange()
```

## Discussion

The system calls this method on a view when your code changes the value of the [tintColor](tintcolor.md) property on that view. In addition, the system calls this method on a subview that inherits a changed interaction tint color.

In your implementation, refresh the view rendering as needed.

## See Also

### Related Documentation

- [tintColor](tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.

### Drawing and updating the view

- [- drawRect:](<draw(__).md>) — Draws the view’s image within the passed-in rectangle.
- [- setNeedsDisplay](<setneedsdisplay().md>) — Marks the receiver’s entire bounds rectangle as needing to be redrawn.
- [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) — Marks the specified rectangle of the receiver as needing to be redrawn.
- [contentScaleFactor](contentscalefactor.md) — The scale factor applied to the view.
