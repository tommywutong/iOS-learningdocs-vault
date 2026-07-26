---
title: sectionIndexMinimumDisplayRowCount
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/sectionindexminimumdisplayrowcount
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/sectionindexminimumdisplayrowcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/sectionindexminimumdisplayrowcount.json'
content_hash: 'sha256:28fe7aa5fe348dbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# sectionIndexMinimumDisplayRowCount

<sub>Instance Property</sub>

The number of table rows at which to display the index list on the right edge of the table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionIndexMinimumDisplayRowCount: Int { get set }
```

## Discussion

This property is applicable only to table views in the [UITableViewStylePlain](style-swift.enum/plain.md) style. The default value is zero.

## See Also

### Configuring the table index

- [sectionIndexColor](sectionindexcolor.md) — The color to use for the table view’s index text.
- [sectionIndexBackgroundColor](sectionindexbackgroundcolor.md) — The color to use for the background of the table view’s section index.
- [sectionIndexTrackingBackgroundColor](sectionindextrackingbackgroundcolor.md) — The color to use for the table view’s index background area.
- [UITableViewIndexSearch](indexsearch.md) — A constant for adding the magnifying glass icon to the section index of a table view.
