---
title: sectionIndexBackgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/sectionindexbackgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/sectionindexbackgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/sectionindexbackgroundcolor.json'
content_hash: 'sha256:ff62c9b1d4006bf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# sectionIndexBackgroundColor

<sub>Instance Property</sub>

The color to use for the background of the table view’s section index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionIndexBackgroundColor: UIColor? { get set }
```

## Discussion

Table views can display an index along the side of the view, making it easier for users to navigate the contents of the table quickly. This property specifies the color to use for the background of the index. The table view applies this color when the user isn’t touching the index. A value of `nil` represents the default color.

## See Also

### Configuring the table index

- [sectionIndexMinimumDisplayRowCount](sectionindexminimumdisplayrowcount.md) — The number of table rows at which to display the index list on the right edge of the table.
- [sectionIndexColor](sectionindexcolor.md) — The color to use for the table view’s index text.
- [sectionIndexTrackingBackgroundColor](sectionindextrackingbackgroundcolor.md) — The color to use for the table view’s index background area.
- [UITableViewIndexSearch](indexsearch.md) — A constant for adding the magnifying glass icon to the section index of a table view.
