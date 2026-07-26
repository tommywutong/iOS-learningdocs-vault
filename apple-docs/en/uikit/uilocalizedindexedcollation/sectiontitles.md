---
title: sectionTitles
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilocalizedindexedcollation/sectiontitles
source_url: 'https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sectiontitles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalizedindexedcollation/sectiontitles.json'
content_hash: 'sha256:2a07dafe95423b17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalizedIndexedCollation](../uilocalizedindexedcollation.md)

# sectionTitles

<sub>Instance Property</sub>

Returns the list of section titles for the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionTitles: [String] { get }
```

## Discussion

This property contains the localized list of section titles sorted according to the specified ordering (for example, A through Z in US English). In its implementation of [- tableView:titleForHeaderInSection:](<../uitableviewdatasource/tableview(__titleforheaderinsection_).md>), the data source can call this method on the indexed-collation object, passing in the section index and returning the result.

## See Also

### Providing section index data to the table view

- [sectionIndexTitles](sectionindextitles.md) — Returns the list of section-index titles for the table view.
- [- sectionForSectionIndexTitleAtIndex:](<section(forsectionindextitle_).md>) — Returns the section that the table view should scroll to for the given index title.
