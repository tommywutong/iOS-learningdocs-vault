---
title: 'tableView(_:accessoryButtonTappedForRowWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:accessorybuttontappedforrowwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:accessorybuttontappedforrowwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aaccessorybuttontappedforrowwith%3A%29.json'
content_hash: 'sha256:a4af19d80b43d17d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:accessoryButtonTappedForRowWith:)

<sub>Instance Method</sub>

Tells the delegate that the user tapped the detail button for the specified row.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWith indexPath: IndexPath)
```

## Parameters

- `tableView` — The table view informing the delegate of this event.

- `indexPath` — The index path of the row whose detail button was tapped.

## Discussion

Use this method to respond to taps in the detail button accessory view of a row. The table view does not call this method for other types of accessory views.
