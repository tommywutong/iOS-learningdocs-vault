---
title: 'insertSubview(_:aboveSubview:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/insertsubview(_:abovesubview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/insertsubview(_:abovesubview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/insertsubview%28_%3Aabovesubview%3A%29.json'
content_hash: 'sha256:45d27341daf7d64b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# insertSubview(_:aboveSubview:)

<sub>Instance Method</sub>

Inserts a view above another view in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)
```

## Parameters

- `view` — The view to insert. It’s removed from its superview if it’s not a sibling of `siblingSubview`.

- `siblingSubview` — The sibling view that will be behind the inserted view.

## Discussion

This method establishes a strong reference to `view` and sets its next responder to the receiver, which is its new superview.

Views can have only one superview. If `view` already has a superview and that view is not the receiver, this method removes the previous superview before making the receiver its new superview.

## See Also

### Managing the view hierarchy

- [superview](superview.md) — The receiver’s superview, or `nil` if it has none.
- [subviews](subviews.md) — The receiver’s immediate subviews.
- [window](window.md) — The receiver’s window object, or `nil` if it has none.
- [- addSubview:](<addsubview(__).md>) — Adds a view to the end of the receiver’s list of subviews.
- [- bringSubviewToFront:](<bringsubviewtofront(__).md>) — Moves the specified subview so that it appears on top of its siblings.
- [- sendSubviewToBack:](<sendsubviewtoback(__).md>) — Moves the specified subview so that it appears behind its siblings.
- [- removeFromSuperview](<removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [- insertSubview:atIndex:](<insertsubview(__at_).md>) — Inserts a subview at the specified index.
- [- insertSubview:belowSubview:](<insertsubview(__belowsubview_).md>) — Inserts a view below another view in the view hierarchy.
- [- exchangeSubviewAtIndex:withSubviewAtIndex:](<exchangesubview(at_withsubviewat_).md>) — Exchanges the subviews at the specified indices.
- [- isDescendantOfView:](<isdescendant(of_).md>) — Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.
