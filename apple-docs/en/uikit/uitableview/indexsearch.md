---
title: indexSearch
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/indexsearch
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/indexsearch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/indexsearch.json'
content_hash: 'sha256:2d9c40cc1dcc468a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# indexSearch

<sub>Type Property</sub>

A constant for adding the magnifying glass icon to the section index of a table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class let indexSearch: String
```

## Discussion

If the data source includes this constant string in the array of strings it returns in [- sectionIndexTitlesForTableView:](<../uitableviewdatasource/sectionindextitles(for_).md>), the section index displays a magnifying glass icon at the corresponding index location. This location should generally be the first title in the index.

## See Also

### Configuring the table index

- [sectionIndexMinimumDisplayRowCount](sectionindexminimumdisplayrowcount.md) — The number of table rows at which to display the index list on the right edge of the table.
- [sectionIndexColor](sectionindexcolor.md) — The color to use for the table view’s index text.
- [sectionIndexBackgroundColor](sectionindexbackgroundcolor.md) — The color to use for the background of the table view’s section index.
- [sectionIndexTrackingBackgroundColor](sectionindextrackingbackgroundcolor.md) — The color to use for the table view’s index background area.
