---
title: readableContentGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/readablecontentguide
source_url: 'https://developer.apple.com/documentation/uikit/uiview/readablecontentguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/readablecontentguide.json'
content_hash: 'sha256:610a726d831353aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# readableContentGuide

<sub>Instance Property</sub>

A layout guide representing an area with a readable width within the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var readableContentGuide: UILayoutGuide { get }
```

## Discussion

This layout guide defines an area that can easily be read without forcing users to move their head to track the lines. The readable content area follows the following rules:

1. The readable content guide never extends beyond the view’s layout margin guide.
2. The readable content guide is vertically centered inside the layout margin guide.
3. The readable content guide’s width is equal to or less than the readable width defined for the current dynamic text size.

Use the readable content guide to lay out a single column of text. If you are laying out multiple columns, you can use the guide’s width to determine the optimal width for your columns.

## See Also

### Working with layout guides

- [- addLayoutGuide:](<addlayoutguide(__).md>) — Adds the specified layout guide to the view.
- [layoutGuides](layoutguides.md) — The array of layout guide objects owned by this view.
- [layoutMarginsGuide](layoutmarginsguide.md) — A layout guide representing the view’s margins.
- [- removeLayoutGuide:](<removelayoutguide(__).md>) — Removes the specified layout guide from the view.
