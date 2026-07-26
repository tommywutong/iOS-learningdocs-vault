---
title: 'tableView(_:dragPreviewParametersForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdragdelegate/tableview(_:dragpreviewparametersforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragpreviewparametersforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdragdelegate/tableview%28_%3Adragpreviewparametersforrowat%3A%29.json'
content_hash: 'sha256:982d33ed714adc58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDragDelegate](../uitableviewdragdelegate.md)

# tableView(_:dragPreviewParametersForRowAt:)

<sub>Instance Method</sub>

Returns custom information about how to display the row at the specified location during the drag.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dragPreviewParametersForRowAt indexPath: IndexPath) -> UIDragPreviewParameters?
```

## Parameters

- `tableView` — The table view from which the drag operation originated.

- `indexPath` — The index path of the row being dragged.

## Return Value

A [UIDragPreviewParameters](../uidragpreviewparameters.md) object containing information about how to customize the row’s appearance. Return `nil` to use the default appearance.

## Discussion

Use this method to customize the appearance of the row during drags. For example, you might use this method to specify that only part of the cell’s visible content should be used for the drag preview. If you don’t implement this method, or if you return `nil`, the drag preview displays the row’s visible content.

In your implementation, create a [UIDragPreviewParameters](../uidragpreviewparameters.md) object and specify the custom preview information for the specified row. Use the parameters to specify the portion of the row that you want to display or to change the background color drawn beneath the row’s contents.
