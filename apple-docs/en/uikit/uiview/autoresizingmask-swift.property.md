---
title: autoresizingMask
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/autoresizingmask-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiview/autoresizingmask-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/autoresizingmask-swift.property.json'
content_hash: 'sha256:0b81c44f62023dac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# autoresizingMask

<sub>Instance Property</sub>

An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var autoresizingMask: UIView.AutoresizingMask { get set }
```

## Discussion

When a view’s bounds change, that view automatically resizes its subviews according to each subview’s autoresizing mask. You specify the value of this mask by combining the constants described in [AutoresizingMask](autoresizingmask-swift.struct.md) using the C bitwise OR operator. Combining these constants lets you specify which dimensions of the view should grow or shrink relative to the superview. The default value of this property is [UIViewAutoresizingNone](../uiviewautoresizing/uiviewautoresizingnone.md), which indicates that the view should not be resized at all.

When more than one option along the same axis is set, the default behavior is to distribute the size difference proportionally among the flexible portions. The larger the flexible portion, relative to the other flexible portions, the more it is likely to grow. For example, suppose this property includes the [UIViewAutoresizingFlexibleWidth](autoresizingmask-swift.struct/flexiblewidth.md) and [UIViewAutoresizingFlexibleRightMargin](autoresizingmask-swift.struct/flexiblerightmargin.md) constants but does not include the [UIViewAutoresizingFlexibleLeftMargin](autoresizingmask-swift.struct/flexibleleftmargin.md) constant, thus indicating that the width of the view’s left margin is fixed but that the view’s width and right margin may change. Thus, the view appears anchored to the left side of its superview while both the view width and the gap to the right of the view increase.

If the autoresizing behaviors do not offer the precise layout that you need for your views, you can use a custom container view and override its [- layoutSubviews](<layoutsubviews().md>) method to position your subviews more precisely.

## See Also

### Configuring the resizing behavior

- [contentMode](contentmode-swift.property.md) — A flag used to determine how a view lays out its content when its bounds change.
- [ContentMode](contentmode-swift.enum.md) — Options to specify how a view adjusts its content when its size changes.
- [- sizeThatFits:](<sizethatfits(__).md>) — Asks the view to calculate and return the size that best fits the specified size.
- [- sizeToFit](<sizetofit().md>) — Resizes and moves the receiver view so it just encloses its subviews.
- [autoresizesSubviews](autoresizessubviews.md) — A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
