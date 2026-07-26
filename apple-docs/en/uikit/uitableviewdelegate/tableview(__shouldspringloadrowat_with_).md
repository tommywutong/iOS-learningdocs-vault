---
title: 'tableView(_:shouldSpringLoadRowAt:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:shouldspringloadrowat:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldspringloadrowat:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Ashouldspringloadrowat%3Awith%3A%29.json'
content_hash: 'sha256:62d65ad16627f14f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:shouldSpringLoadRowAt:with:)

<sub>Instance Method</sub>

Called to let you fine tune the spring-loading behavior of the rows in a table.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, shouldSpringLoadRowAt indexPath: IndexPath, with context: any UISpringLoadedInteractionContext) -> Bool
```

## Parameters

- `tableView` — The table view where the interaction is occurring.

- `indexPath` — The index path of the row whose spring-loading behavior is being considered.

- `context` — A context object that you can use to modify the spring-loading behavior. Use this object to specify the location for spring-loading animations associated in the row.

## Return Value

[true](../../swift/true.md) if the row allows spring-loaded interactions or [false](../../swift/false.md) if it does not.

## Discussion

Override this method when you want to selectively disable spring-loaded interactions with the rows of your table. For example, you might return [false](../../swift/false.md) for rows that represent leaf content and not a folder of content. If you do not implement this method, the table view performs spring-loading animations on the row when it is not currently being dragged.By default, spring-loading animations are performed on the entire row. To modify these animations, modify the provided context object. For example, you might use the context object to apply the spring-loading animations to a single subview of the row instead of to the entire row.

## See Also

### Configuring rows for the table view

- [- tableView:willDisplayCell:forRowAtIndexPath:](<tableview(__willdisplay_forrowat_).md>) — Tells the delegate the table view is about to draw a cell for a particular row.
- [- tableView:indentationLevelForRowAtIndexPath:](<tableview(__indentationlevelforrowat_).md>) — Asks the delegate to return the level of indentation for a row in a given section.
