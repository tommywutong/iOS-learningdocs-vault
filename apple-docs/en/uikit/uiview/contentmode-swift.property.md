---
title: contentMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/contentmode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiview/contentmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/contentmode-swift.property.json'
content_hash: 'sha256:84f9674d3f627abd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# contentMode

<sub>Instance Property</sub>

A flag used to determine how a view lays out its content when its bounds change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentMode: UIView.ContentMode { get set }
```

## Discussion

The content mode specifies how the cached bitmap of the view’s layer is adjusted when the view’s bounds change. This property is often used to implement resizable controls. Instead of redrawing the contents of the view every time, you can use this property to specify that you want to scale the contents (either with or without distortion) or pin them to a particular spot on the view.

> [!note] Note
> You can always force the contents of a view to be redrawn by calling the [- setNeedsDisplay](<setneedsdisplay().md>) or [- setNeedsDisplayInRect:](<setneedsdisplay(__).md>) method.

For a list of values you can assign to this property, see [ContentMode](contentmode-swift.enum.md). The default value of this property is [UIViewContentModeScaleToFill](contentmode-swift.enum/scaletofill.md).

## See Also

### Configuring the resizing behavior

- [ContentMode](contentmode-swift.enum.md) — Options to specify how a view adjusts its content when its size changes.
- [- sizeThatFits:](<sizethatfits(__).md>) — Asks the view to calculate and return the size that best fits the specified size.
- [- sizeToFit](<sizetofit().md>) — Resizes and moves the receiver view so it just encloses its subviews.
- [autoresizesSubviews](autoresizessubviews.md) — A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [autoresizingMask](autoresizingmask-swift.property.md) — An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.
