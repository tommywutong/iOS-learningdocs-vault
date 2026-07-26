---
title: sectionIndexTrackingBackgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/sectionindextrackingbackgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/sectionindextrackingbackgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/sectionindextrackingbackgroundcolor.json'
content_hash: 'sha256:24654cd5ef272605'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# sectionIndexTrackingBackgroundColor

<sub>Instance Property</sub>

The color to use for the table view’s index background area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionIndexTrackingBackgroundColor: UIColor? { get set }
```

## Discussion

Table views can display an index along the side of the view, making it easier for users to navigate the contents of the table quickly. This property specifies the color to display in the background of the index when the user drags a finger through it. A value of `nil` represents the default color.

## See Also

### Configuring the table index

- [sectionIndexMinimumDisplayRowCount](sectionindexminimumdisplayrowcount.md) — The number of table rows at which to display the index list on the right edge of the table.
- [sectionIndexColor](sectionindexcolor.md) — The color to use for the table view’s index text.
- [sectionIndexBackgroundColor](sectionindexbackgroundcolor.md) — The color to use for the background of the table view’s section index.
- [UITableViewIndexSearch](indexsearch.md) — A constant for adding the magnifying glass icon to the section index of a table view.
