---
title: 'section(forSectionIndexTitle:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilocalizedindexedcollation/section(forsectionindextitle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/section(forsectionindextitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalizedindexedcollation/section%28forsectionindextitle%3A%29.json'
content_hash: 'sha256:2c73bae377304add'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalizedIndexedCollation](../uilocalizedindexedcollation.md)

# section(forSectionIndexTitle:)

<sub>Instance Method</sub>

Returns the section that the table view should scroll to for the given index title.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func section(forSectionIndexTitle indexTitleIndex: Int) -> Int
```

## Parameters

- `indexTitleIndex` — An integer identifying a section-index title by its position in the array of such titles.

## Return Value

An integer identifying the table-view section associated with `indexTitleIndex`.

## Discussion

This method allows the table view to map between a given item in the section index and a given section even when there isn’t a one-to-one mapping. In its implementation of [- tableView:sectionForSectionIndexTitle:atIndex:](<../uitableviewdatasource/tableview(__sectionforsectionindextitle_at_).md>), the data source can call this method on the indexed-collation object specifying as an argument the passed-in index integer; it then returns the result to the table view.

## See Also

### Providing section index data to the table view

- [sectionTitles](sectiontitles.md) — Returns the list of section titles for the table view.
- [sectionIndexTitles](sectionindextitles.md) — Returns the list of section-index titles for the table view.
