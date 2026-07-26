---
title: UITableViewCell.AccessoryType.checkmark
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/accessorytype-swift.enum/checkmark
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/checkmark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/accessorytype-swift.enum/checkmark.json'
content_hash: 'sha256:ccefdfe0c926cade'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITableViewCell](../../uitableviewcell.md) · [AccessoryType](../accessorytype-swift.enum.md)

# UITableViewCell.AccessoryType.checkmark

<sub>Case</sub>

A checkmark image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case checkmark
```

## Discussion

Choose this option to display a checkmark image. This type of accessory view doesn’t track touches.

To hide or show a check mark for a row, toggle the [accessoryType](../accessorytype-swift.property.md) property of the cell between the [UITableViewCellAccessoryNone](none.md) and [UITableViewCellAccessoryCheckmark](checkmark.md) values. For example, if you use a checkmark to indicate one selected row from a group of rows, use your delegate’s [- tableView:didSelectRowAtIndexPath:](<../../uitableviewdelegate/tableview(__didselectrowat_).md>) method to update the accessory views of the affected rows.

## See Also

### Accessory views

- [UITableViewCellAccessoryNone](none.md) — No accessory view.
- [UITableViewCellAccessoryDisclosureIndicator](disclosureindicator.md) — A chevron-shaped control for presenting new content.
- [UITableViewCellAccessoryDetailDisclosureButton](detaildisclosurebutton.md) — An information button and a disclosure (chevron) control.
- [UITableViewCellAccessoryDetailButton](detailbutton.md) — An information button.
