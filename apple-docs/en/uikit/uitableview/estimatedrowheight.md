---
title: estimatedRowHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/estimatedrowheight
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/estimatedrowheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/estimatedrowheight.json'
content_hash: 'sha256:cb491c19a307be7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# estimatedRowHeight

<sub>Instance Property</sub>

The estimated height of rows in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var estimatedRowHeight: CGFloat { get set }
```

## Discussion

Providing a nonnegative estimate of the height of rows can improve the performance of loading the table view. If the table contains variable height rows, it might be expensive to calculate all their heights when the table loads. Estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

The default value is [UITableViewAutomaticDimension](automaticdimension.md), which means that the table view selects an estimated height to use on your behalf. Setting the value to `0` disables estimated heights, which causes the table view to request the actual height for each cell. If your table uses self-sizing cells, the value of this property must not be `0`.

When using height estimates, the table view actively manages the [contentOffset](../uiscrollview/contentoffset.md) and [contentSize](../uiscrollview/contentsize.md) properties inherited from its scroll view. Don’t attempt to read or modify those properties directly.

## See Also

### Related Documentation

- [estimatedSectionHeaderHeight](estimatedsectionheaderheight.md) — The estimated height of section headers in the table view.
- [estimatedSectionFooterHeight](estimatedsectionfooterheight.md) — The estimated height of section footers in the table view.

### Configuring cell height and layout

- [rowHeight](rowheight.md) — The default height in points of each row in the table view.
- [fillerRowHeight](fillerrowheight.md) — The height for empty rows that fill the table view.
- [cellLayoutMarginsFollowReadableWidth](celllayoutmarginsfollowreadablewidth.md) — A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.
- [insetsContentViewsToSafeArea](insetscontentviewstosafearea.md) — A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.
