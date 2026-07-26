---
title: leftAnchor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/leftanchor
source_url: 'https://developer.apple.com/documentation/uikit/uiview/leftanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/leftanchor.json'
content_hash: 'sha256:f90bf1289bc287b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# leftAnchor

<sub>Instance Property</sub>

A layout anchor representing the left edge of the view’s frame.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var leftAnchor: NSLayoutXAxisAnchor { get }
```

## Discussion

Use this anchor to create constraints with the view’s left edge. You can combine this anchor only with a subset of the [NSLayoutXAxisAnchor](../nslayoutxaxisanchor.md) anchors. You can combine a [UIView](../uiview.md) with another `leftAnchor`, a `rightAnchor`, or a `centerXAnchor`. For more information, see [NSLayoutAnchor](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors

- [bottomAnchor](bottomanchor.md) — A layout anchor representing the bottom edge of the view’s frame.
- [centerXAnchor](centerxanchor.md) — A layout anchor representing the horizontal center of the view’s frame.
- [centerYAnchor](centeryanchor.md) — A layout anchor representing the vertical center of the view’s frame.
- [firstBaselineAnchor](firstbaselineanchor.md) — A layout anchor representing the baseline for the topmost line of text in the view.
- [heightAnchor](heightanchor.md) — A layout anchor representing the height of the view’s frame.
- [lastBaselineAnchor](lastbaselineanchor.md) — A layout anchor representing the baseline for the bottommost line of text in the view.
- [leadingAnchor](leadinganchor.md) — A layout anchor representing the leading edge of the view’s frame.
- [rightAnchor](rightanchor.md) — A layout anchor representing the right edge of the view’s frame.
- [topAnchor](topanchor.md) — A layout anchor representing the top edge of the view’s frame.
- [trailingAnchor](trailinganchor.md) — A layout anchor representing the trailing edge of the view’s frame.
- [widthAnchor](widthanchor.md) — A layout anchor representing the width of the view’s frame.
