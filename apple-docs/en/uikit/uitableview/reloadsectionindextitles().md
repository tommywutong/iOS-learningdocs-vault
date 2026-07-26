---
title: reloadSectionIndexTitles()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/reloadsectionindextitles()
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/reloadsectionindextitles()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/reloadsectionindextitles%28%29.json'
content_hash: 'sha256:d858865f0679607c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# reloadSectionIndexTitles()

<sub>Instance Method</sub>

Reloads the items in the index bar along the right side of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reloadSectionIndexTitles()
```

## Discussion

This method gives you a way to update the section index after inserting or deleting sections without having to reload the whole table.

## See Also

### Related Documentation

- [- sectionIndexTitlesForTableView:](<../uitableviewdatasource/sectionindextitles(for_).md>) — Asks the data source to return the titles for the sections of a table view.

### Reloading the table view

- [hasUncommittedUpdates](hasuncommittedupdates.md) — A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [- reconfigureRowsAtIndexPaths:](<reconfigurerows(at_).md>) — Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [- reloadData](<reloaddata().md>) — Reloads the rows and sections of the table view.
- [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>) — Reloads the specified rows using the provided animation effect.
- [- reloadSections:withRowAnimation:](<reloadsections(__with_).md>) — Reloads the specified sections using the provided animation effect.
