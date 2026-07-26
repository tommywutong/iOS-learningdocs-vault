---
title: 'exchangeSubview(at:withSubviewAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/exchangesubview(at:withsubviewat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/exchangesubview(at:withsubviewat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/exchangesubview%28at%3Awithsubviewat%3A%29.json'
content_hash: 'sha256:24f55368786325de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# exchangeSubview(at:withSubviewAt:)

<sub>Instance Method</sub>

Exchanges the subviews at the specified indices.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func exchangeSubview(at index1: Int, withSubviewAt index2: Int)
```

## Parameters

- `index1` — The index of the first subview in the receiver.

- `index2` — The index of the second subview in the receiver.

## Discussion

Each index represents the position of the corresponding view in the array in the [subviews](subviews.md) property. Subview indices start at `0` and cannot be greater than the number of subviews. This method does not change the superview of either view but simply swaps their positions in the [subviews](subviews.md) array.

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
- [- insertSubview:aboveSubview:](<insertsubview(__abovesubview_).md>) — Inserts a view above another view in the view hierarchy.
- [- insertSubview:belowSubview:](<insertsubview(__belowsubview_).md>) — Inserts a view below another view in the view hierarchy.
- [- isDescendantOfView:](<isdescendant(of_).md>) — Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.
