---
title: insetsContentViewsToSafeArea
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/insetscontentviewstosafearea
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/insetscontentviewstosafearea'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/insetscontentviewstosafearea.json'
content_hash: 'sha256:fffde909d836b1da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# insetsContentViewsToSafeArea

<sub>Instance Property</sub>

A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var insetsContentViewsToSafeArea: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md) (the default), the table view adjusts the insets of the content view within each of its cells, headers, and footers on the leading and trailing sides to make the content fit within the safe area. The safe area ensures that the content within the table view isn’t obscured by other views, or by the edges of the device.

When the value of this property is [false](../../swift/false.md), the table view doesn’t adjust the insets of the content view within each of its cells, headers, and footers to account for the safe area. In this case, the content views extend to the bounds of their respective superviews, which may cause the content to be obscured.

## See Also

### Related Documentation

- [safeAreaInsets](../uiview/safeareainsets.md) — The insets that you use to determine the safe area for this view.

### Configuring cell height and layout

- [rowHeight](rowheight.md) — The default height in points of each row in the table view.
- [estimatedRowHeight](estimatedrowheight.md) — The estimated height of rows in the table view.
- [fillerRowHeight](fillerrowheight.md) — The height for empty rows that fill the table view.
- [cellLayoutMarginsFollowReadableWidth](celllayoutmarginsfollowreadablewidth.md) — A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.
