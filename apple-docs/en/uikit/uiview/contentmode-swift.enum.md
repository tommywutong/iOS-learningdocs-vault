---
title: UIView.ContentMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/contentmode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiview/contentmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/contentmode-swift.enum.json'
content_hash: 'sha256:fa9e2ac45e9c4cff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.ContentMode

<sub>Enumeration</sub>

Options to specify how a view adjusts its content when its size changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ContentMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIViewContentModeScaleToFill](contentmode-swift.enum/scaletofill.md) — The option to scale the content to fit the size of itself by changing the aspect ratio of the content if necessary.
- [UIViewContentModeScaleAspectFit](contentmode-swift.enum/scaleaspectfit.md) — The option to scale the content to fit the size of the view by maintaining the aspect ratio. Any remaining area of the view’s bounds is transparent.
- [UIViewContentModeScaleAspectFill](contentmode-swift.enum/scaleaspectfill.md) — The option to scale the content to fill the size of the view. Some portion of the content may be clipped to fill the view’s bounds.
- [UIViewContentModeRedraw](contentmode-swift.enum/redraw.md) — The option to redisplay the view when the bounds change by invoking the [- setNeedsDisplay](<setneedsdisplay().md>) method.
- [UIViewContentModeCenter](contentmode-swift.enum/center.md) — The option to center the content in the view’s bounds, keeping the proportions the same.
- [UIViewContentModeTop](contentmode-swift.enum/top.md) — The option to center the content aligned at the top in the view’s bounds.
- [UIViewContentModeBottom](contentmode-swift.enum/bottom.md) — The option to center the content aligned at the bottom in the view’s bounds.
- [UIViewContentModeLeft](contentmode-swift.enum/left.md) — The option to align the content on the left of the view.
- [UIViewContentModeRight](contentmode-swift.enum/right.md) — The option to align the content on the right of the view.
- [UIViewContentModeTopLeft](contentmode-swift.enum/topleft.md) — The option to align the content in the top-left corner of the view.
- [UIViewContentModeTopRight](contentmode-swift.enum/topright.md) — The option to align the content in the top-right corner of the view.
- [UIViewContentModeBottomLeft](contentmode-swift.enum/bottomleft.md) — The option to align the content in the bottom-left corner of the view.
- [UIViewContentModeBottomRight](contentmode-swift.enum/bottomright.md) — The option to align the content in the bottom-right corner of the view.

### Initializers

- [init(rawValue:)](<contentmode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the resizing behavior

- [contentMode](contentmode-swift.property.md) — A flag used to determine how a view lays out its content when its bounds change.
- [- sizeThatFits:](<sizethatfits(__).md>) — Asks the view to calculate and return the size that best fits the specified size.
- [- sizeToFit](<sizetofit().md>) — Resizes and moves the receiver view so it just encloses its subviews.
- [autoresizesSubviews](autoresizessubviews.md) — A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [autoresizingMask](autoresizingmask-swift.property.md) — An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.
