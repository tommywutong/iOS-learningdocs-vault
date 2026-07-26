---
title: 'sendSubviewToBack(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/sendsubviewtoback(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/sendsubviewtoback(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/sendsubviewtoback%28_%3A%29.json'
content_hash: 'sha256:9a225218daba3090'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# sendSubviewToBack(_:)

<sub>Instance Method</sub>

Moves the specified subview so that it appears behind its siblings.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sendSubviewToBack(_ view: UIView)
```

## Parameters

- `view` — The subview to move to the back.

## Discussion

This method moves the specified view to the beginning of the array of views in the [subviews](subviews.md) property.

## See Also

### Managing the view hierarchy

- [superview](superview.md) — The receiver’s superview, or `nil` if it has none.
- [subviews](subviews.md) — The receiver’s immediate subviews.
- [window](window.md) — The receiver’s window object, or `nil` if it has none.
- [- addSubview:](<addsubview(__).md>) — Adds a view to the end of the receiver’s list of subviews.
- [- bringSubviewToFront:](<bringsubviewtofront(__).md>) — Moves the specified subview so that it appears on top of its siblings.
- [- removeFromSuperview](<removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [- insertSubview:atIndex:](<insertsubview(__at_).md>) — Inserts a subview at the specified index.
- [- insertSubview:aboveSubview:](<insertsubview(__abovesubview_).md>) — Inserts a view above another view in the view hierarchy.
- [- insertSubview:belowSubview:](<insertsubview(__belowsubview_).md>) — Inserts a view below another view in the view hierarchy.
- [- exchangeSubviewAtIndex:withSubviewAtIndex:](<exchangesubview(at_withsubviewat_).md>) — Exchanges the subviews at the specified indices.
- [- isDescendantOfView:](<isdescendant(of_).md>) — Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.
