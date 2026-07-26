---
title: 'sectionIndexTitles(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/sectionindextitles(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/sectionindextitles(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/sectionindextitles%28for%3A%29.json'
content_hash: 'sha256:e3c654bc9be5277b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# sectionIndexTitles(for:)

<sub>Instance Method</sub>

Asks the data source to return the titles for the sections of a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func sectionIndexTitles(for tableView: UITableView) -> [String]?
```

## Parameters

- `tableView` — The table-view object requesting this information.

## Return Value

An array of strings that serve as the title of sections in the table view and appear in the index list on the right side of the table view. The table view must be in the plain style (`UITableViewStylePlain`). For example, for an alphabetized list, you could return an array containing strings “A” through “Z”.

## See Also

### Configuring an index

- [- tableView:sectionForSectionIndexTitle:atIndex:](<tableview(__sectionforsectionindextitle_at_).md>) — Asks the data source to return the index of the section having the given title and section title index.
