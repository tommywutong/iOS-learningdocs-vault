---
title: fillerRowHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/fillerrowheight
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/fillerrowheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/fillerrowheight.json'
content_hash: 'sha256:5de60cc711fbe24a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# fillerRowHeight

<sub>Instance Property</sub>

The height for empty rows that fill the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var fillerRowHeight: CGFloat { get set }
```

## Discussion

Table views with a [style](style-swift.property.md) of [UITableViewStylePlain](style-swift.enum/plain.md) can display filler rows, empty rows that appear below the last row when there isn’t enough content to fill the table view. Set this property to adjust the height of each filler row:

- Set `0.0` to not display filler rows. This behavior is the default in iOS 15 and later.
- Set [UITableViewAutomaticDimension](automaticdimension.md) to display filler rows that use an automatic height, matching the height of the last row in the table view. This behavior is the default in versions of iOS earlier than iOS 15.
- Set any other positive value to display filler rows of that specified height.

A table view with a [style](style-swift.property.md) other than [UITableViewStylePlain](style-swift.enum/plain.md) doesn’t show filler rows, so it ignores any value other than `0.0` for this property.

## See Also

### Configuring cell height and layout

- [rowHeight](rowheight.md) — The default height in points of each row in the table view.
- [estimatedRowHeight](estimatedrowheight.md) — The estimated height of rows in the table view.
- [cellLayoutMarginsFollowReadableWidth](celllayoutmarginsfollowreadablewidth.md) — A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.
- [insetsContentViewsToSafeArea](insetscontentviewstosafearea.md) — A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.
