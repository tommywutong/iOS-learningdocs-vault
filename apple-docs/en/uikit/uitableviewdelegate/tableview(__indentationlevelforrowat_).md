---
title: 'tableView(_:indentationLevelForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:indentationlevelforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:indentationlevelforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aindentationlevelforrowat%3A%29.json'
content_hash: 'sha256:ce9ae3f21258d152'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:indentationLevelForRowAt:)

<sub>Instance Method</sub>

Asks the delegate to return the level of indentation for a row in a given section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, indentationLevelForRowAt indexPath: IndexPath) -> Int
```

## Parameters

- `tableView` — The table view requesting this information.

- `indexPath` — An index path locating the row in `tableView`.

## Return Value

Returns the depth of the specified row to show its hierarchical position in the section.

## See Also

### Configuring rows for the table view

- [- tableView:willDisplayCell:forRowAtIndexPath:](<tableview(__willdisplay_forrowat_).md>) — Tells the delegate the table view is about to draw a cell for a particular row.
- [- tableView:shouldSpringLoadRowAtIndexPath:withContext:](<tableview(__shouldspringloadrowat_with_).md>) — Called to let you fine tune the spring-loading behavior of the rows in a table.
