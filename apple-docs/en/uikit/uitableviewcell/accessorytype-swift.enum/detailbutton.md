---
title: UITableViewCell.AccessoryType.detailButton
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/accessorytype-swift.enum/detailbutton
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/detailbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/accessorytype-swift.enum/detailbutton.json'
content_hash: 'sha256:b8f6dbcbd2614365'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITableViewCell](../../uitableviewcell.md) · [AccessoryType](../accessorytype-swift.enum.md)

# UITableViewCell.AccessoryType.detailButton

<sub>Case</sub>

An information button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case detailButton
```

## Discussion

Choose this option to display a button that, when tapped, displays information about the row. Use your delegate’s [- tableView:accessoryButtonTappedForRowWithIndexPath:](<../../uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>) method to respond to taps in the button.

## See Also

### Accessory views

- [UITableViewCellAccessoryNone](none.md) — No accessory view.
- [UITableViewCellAccessoryDisclosureIndicator](disclosureindicator.md) — A chevron-shaped control for presenting new content.
- [UITableViewCellAccessoryDetailDisclosureButton](detaildisclosurebutton.md) — An information button and a disclosure (chevron) control.
- [UITableViewCellAccessoryCheckmark](checkmark.md) — A checkmark image.
