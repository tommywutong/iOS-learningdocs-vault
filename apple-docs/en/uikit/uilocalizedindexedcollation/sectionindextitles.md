---
title: sectionIndexTitles
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilocalizedindexedcollation/sectionindextitles
source_url: 'https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sectionindextitles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalizedindexedcollation/sectionindextitles.json'
content_hash: 'sha256:d0bab1254a96dbaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalizedIndexedCollation](../uilocalizedindexedcollation.md)

# sectionIndexTitles

<sub>Instance Property</sub>

Returns the list of section-index titles for the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionIndexTitles: [String] { get }
```

## Discussion

This property contains the localized list of section-index titles sorted according to the specified ordering (for example, A through Z in US English). In its implementation of [- sectionIndexTitlesForTableView:](<../uitableviewdatasource/sectionindextitles(for_).md>), the data source can call this method on the indexed-collation object and pass back the result.

## See Also

### Providing section index data to the table view

- [sectionTitles](sectiontitles.md) — Returns the list of section titles for the table view.
- [- sectionForSectionIndexTitleAtIndex:](<section(forsectionindextitle_).md>) — Returns the section that the table view should scroll to for the given index title.
