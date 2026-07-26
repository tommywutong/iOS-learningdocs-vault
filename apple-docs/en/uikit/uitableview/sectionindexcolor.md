---
title: sectionIndexColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/sectionindexcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/sectionindexcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/sectionindexcolor.json'
content_hash: 'sha256:3ba9093d88cdcd8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# sectionIndexColor

<sub>Instance Property</sub>

The color to use for the table view’s index text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionIndexColor: UIColor? { get set }
```

## Discussion

Table views can display an index along the side of the view, making it easier for users to navigate the contents of the table quickly. This property specifies the color to use for text displayed in this region. A value of `nil` represents the default color.

## See Also

### Configuring the table index

- [sectionIndexMinimumDisplayRowCount](sectionindexminimumdisplayrowcount.md) — The number of table rows at which to display the index list on the right edge of the table.
- [sectionIndexBackgroundColor](sectionindexbackgroundcolor.md) — The color to use for the background of the table view’s section index.
- [sectionIndexTrackingBackgroundColor](sectionindextrackingbackgroundcolor.md) — The color to use for the table view’s index background area.
- [UITableViewIndexSearch](indexsearch.md) — A constant for adding the magnifying glass icon to the section index of a table view.
