---
title: 'section(forSectionIndexTitle:at:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontroller/section(forsectionindextitle:at:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/section(forsectionindextitle:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/section%28forsectionindextitle%3Aat%3A%29.json'
content_hash: 'sha256:5a61af49465ee53f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# section(forSectionIndexTitle:at:)

<sub>Instance Method</sub>

Returns the section number for a given section title and index in the section index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func section(forSectionIndexTitle title: String, at sectionIndex: Int) -> Int
```

## Parameters

- `title` — The title of a section

- `sectionIndex` — The index of a section.

## Return Value

The section number for the given section title and index in the section index

## Discussion

You would typically call this method when executing `UITableViewDataSource`’s [tableView(_:sectionForSectionIndexTitle:at:)](<../../uikit/uitableviewdatasource/tableview(__sectionforsectionindextitle_at_).md>) method.

## See Also

### Querying Section Information

- [sections](sections.md) — The sections for the fetch results.
