---
title: removeFromSuperview()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/removefromsuperview()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/removefromsuperview()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/removefromsuperview%28%29.json'
content_hash: 'sha256:8312f5a1018c29fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# removeFromSuperview()

<sub>Instance Method</sub>

Unlinks the view from its superview and its window, and removes it from the responder chain.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeFromSuperview()
```

## Discussion

If the view’s superview is not `nil`, the superview releases the view.

Calling this method removes any constraints that refer to the view you are removing, or that refer to any view in the subtree of the view you are removing.

> [!important] Important
> Never call this method from inside your view’s [- drawRect:](<draw(__).md>) method.

## See Also

### Managing the view hierarchy

- [superview](superview.md) — The receiver’s superview, or `nil` if it has none.
- [subviews](subviews.md) — The receiver’s immediate subviews.
- [window](window.md) — The receiver’s window object, or `nil` if it has none.
- [- addSubview:](<addsubview(__).md>) — Adds a view to the end of the receiver’s list of subviews.
- [- bringSubviewToFront:](<bringsubviewtofront(__).md>) — Moves the specified subview so that it appears on top of its siblings.
- [- sendSubviewToBack:](<sendsubviewtoback(__).md>) — Moves the specified subview so that it appears behind its siblings.
- [- insertSubview:atIndex:](<insertsubview(__at_).md>) — Inserts a subview at the specified index.
- [- insertSubview:aboveSubview:](<insertsubview(__abovesubview_).md>) — Inserts a view above another view in the view hierarchy.
- [- insertSubview:belowSubview:](<insertsubview(__belowsubview_).md>) — Inserts a view below another view in the view hierarchy.
- [- exchangeSubviewAtIndex:withSubviewAtIndex:](<exchangesubview(at_withsubviewat_).md>) — Exchanges the subviews at the specified indices.
- [- isDescendantOfView:](<isdescendant(of_).md>) — Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.
