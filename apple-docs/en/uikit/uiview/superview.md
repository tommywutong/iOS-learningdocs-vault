---
title: superview
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/superview
source_url: 'https://developer.apple.com/documentation/uikit/uiview/superview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/superview.json'
content_hash: 'sha256:4bca16a505bf398f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# superview

<sub>Instance Property</sub>

The receiver’s superview, or `nil` if it has none.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var superview: UIView? { get }
```

## See Also

### Managing the view hierarchy

- [subviews](subviews.md) — The receiver’s immediate subviews.
- [window](window.md) — The receiver’s window object, or `nil` if it has none.
- [- addSubview:](<addsubview(__).md>) — Adds a view to the end of the receiver’s list of subviews.
- [- bringSubviewToFront:](<bringsubviewtofront(__).md>) — Moves the specified subview so that it appears on top of its siblings.
- [- sendSubviewToBack:](<sendsubviewtoback(__).md>) — Moves the specified subview so that it appears behind its siblings.
- [- removeFromSuperview](<removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [- insertSubview:atIndex:](<insertsubview(__at_).md>) — Inserts a subview at the specified index.
- [- insertSubview:aboveSubview:](<insertsubview(__abovesubview_).md>) — Inserts a view above another view in the view hierarchy.
- [- insertSubview:belowSubview:](<insertsubview(__belowsubview_).md>) — Inserts a view below another view in the view hierarchy.
- [- exchangeSubviewAtIndex:withSubviewAtIndex:](<exchangesubview(at_withsubviewat_).md>) — Exchanges the subviews at the specified indices.
- [- isDescendantOfView:](<isdescendant(of_).md>) — Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.
