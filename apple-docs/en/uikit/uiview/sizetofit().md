---
title: sizeToFit()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/sizetofit()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/sizetofit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/sizetofit%28%29.json'
content_hash: 'sha256:96932276c7c627b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# sizeToFit()

<sub>Instance Method</sub>

Resizes and moves the receiver view so it just encloses its subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sizeToFit()
```

## Discussion

Call this method when you want to resize the current view so that it uses the most appropriate amount of space. Specific UIKit views resize themselves according to their own internal needs. In some cases, if a view does not have a superview, it may size itself to the screen bounds. Thus, if you want a given view to size itself to its parent view, you should add it to the parent view before calling this method.

You should not override this method. If you want to change the default sizing information for your view, override the [- sizeThatFits:](<sizethatfits(__).md>) instead. That method performs any needed calculations and returns them to this method, which then makes the change.

## See Also

### Configuring the resizing behavior

- [contentMode](contentmode-swift.property.md) — A flag used to determine how a view lays out its content when its bounds change.
- [ContentMode](contentmode-swift.enum.md) — Options to specify how a view adjusts its content when its size changes.
- [- sizeThatFits:](<sizethatfits(__).md>) — Asks the view to calculate and return the size that best fits the specified size.
- [autoresizesSubviews](autoresizessubviews.md) — A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [autoresizingMask](autoresizingmask-swift.property.md) — An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.
