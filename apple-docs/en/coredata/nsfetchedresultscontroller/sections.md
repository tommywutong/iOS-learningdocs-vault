---
title: sections
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontroller/sections
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/sections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontroller/sections.json'
content_hash: 'sha256:8d37b3ba4bef2fbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsController](../nsfetchedresultscontroller.md)

# sections

<sub>Instance Property</sub>

The sections for the fetch results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sections: [any NSFetchedResultsSectionInfo]? { get }
```

## Discussion

The objects in the sections array implement the [NSFetchedResultsSectionInfo](../nsfetchedresultssectioninfo.md) protocol.

You typically use the sections array when implementing `UITableViewDataSource` methods, such as [numberOfSections(in:)](<../../uikit/uitableviewdatasource/numberofsections(in_).md>) and [tableView(_:titleForHeaderInSection:)](<../../uikit/uitableviewdatasource/tableview(__titleforheaderinsection_).md>).

## See Also

### Querying Section Information

- [- sectionForSectionIndexTitle:atIndex:](<section(forsectionindextitle_at_).md>) — Returns the section number for a given section title and index in the section index.
