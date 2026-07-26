---
title: lastBaselineAnchor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/lastbaselineanchor
source_url: 'https://developer.apple.com/documentation/uikit/uiview/lastbaselineanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/lastbaselineanchor.json'
content_hash: 'sha256:a132d330a7b0c6ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# lastBaselineAnchor

<sub>Instance Property</sub>

A layout anchor representing the baseline for the bottommost line of text in the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var lastBaselineAnchor: NSLayoutYAxisAnchor { get }
```

## Discussion

For views with multiple lines of text, this anchor represents the baseline of the bottom row of text. Use this anchor to create constraints with this baseline. You can combine this anchor only with other [NSLayoutYAxisAnchor](../nslayoutyaxisanchor.md) anchors. For more information, see [NSLayoutAnchor](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors

- [bottomAnchor](bottomanchor.md) — A layout anchor representing the bottom edge of the view’s frame.
- [centerXAnchor](centerxanchor.md) — A layout anchor representing the horizontal center of the view’s frame.
- [centerYAnchor](centeryanchor.md) — A layout anchor representing the vertical center of the view’s frame.
- [firstBaselineAnchor](firstbaselineanchor.md) — A layout anchor representing the baseline for the topmost line of text in the view.
- [heightAnchor](heightanchor.md) — A layout anchor representing the height of the view’s frame.
- [leadingAnchor](leadinganchor.md) — A layout anchor representing the leading edge of the view’s frame.
- [leftAnchor](leftanchor.md) — A layout anchor representing the left edge of the view’s frame.
- [rightAnchor](rightanchor.md) — A layout anchor representing the right edge of the view’s frame.
- [topAnchor](topanchor.md) — A layout anchor representing the top edge of the view’s frame.
- [trailingAnchor](trailinganchor.md) — A layout anchor representing the trailing edge of the view’s frame.
- [widthAnchor](widthanchor.md) — A layout anchor representing the width of the view’s frame.
