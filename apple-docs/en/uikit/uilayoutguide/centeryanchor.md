---
title: centerYAnchor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutguide/centeryanchor
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutguide/centeryanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutguide/centeryanchor.json'
content_hash: 'sha256:6f3782a37e8ccd75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutGuide](../uilayoutguide.md)

# centerYAnchor

<sub>Instance Property</sub>

A layout anchor representing the vertical center of the layout guide’s frame.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var centerYAnchor: NSLayoutYAxisAnchor { get }
```

## Discussion

Use this anchor to create constraints with the layout guide’s vertical center. You can combine this anchor only with other [NSLayoutYAxisAnchor](../nslayoutyaxisanchor.md) anchors. For more information, see [NSLayoutAnchor](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors

- [bottomAnchor](bottomanchor.md) — A layout anchor representing the bottom edge of the layout guide’s frame.
- [centerXAnchor](centerxanchor.md) — A layout anchor representing the horizontal center of the layout guide’s frame.
- [heightAnchor](heightanchor.md) — A layout anchor representing the height of the layout guide’s frame.
- [leadingAnchor](leadinganchor.md) — A layout anchor representing the leading edge of the layout guide’s frame.
- [leftAnchor](leftanchor.md) — A layout anchor representing the left edge of the layout guide’s frame.
- [rightAnchor](rightanchor.md) — A layout anchor representing the right edge of the layout guide’s frame.
- [topAnchor](topanchor.md) — A layout anchor representing the top edge of the layout guide’s frame.
- [trailingAnchor](trailinganchor.md) — A layout anchor representing the trailing edge of the layout guide’s frame.
- [widthAnchor](widthanchor.md) — A layout anchor representing the width of the layout guide’s frame.
