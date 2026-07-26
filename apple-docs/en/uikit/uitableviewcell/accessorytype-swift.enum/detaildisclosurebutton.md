---
title: UITableViewCell.AccessoryType.detailDisclosureButton
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton.json'
content_hash: 'sha256:5ae7dacfbc977d8f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITableViewCell](../../uitableviewcell.md) · [AccessoryType](../accessorytype-swift.enum.md)

# UITableViewCell.AccessoryType.detailDisclosureButton

<sub>Case</sub>

An information button and a disclosure (chevron) control.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case detailDisclosureButton
```

## Discussion

Choose this type when you want both an information button and a disclosure control. Connect the disclosure control to a push segue to display new content. Use the delegate’s [- tableView:accessoryButtonTappedForRowWithIndexPath:](<../../uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>)method to respond to touch events in the detail button.

## See Also

### Accessory views

- [UITableViewCellAccessoryNone](none.md) — No accessory view.
- [UITableViewCellAccessoryDisclosureIndicator](disclosureindicator.md) — A chevron-shaped control for presenting new content.
- [UITableViewCellAccessoryCheckmark](checkmark.md) — A checkmark image.
- [UITableViewCellAccessoryDetailButton](detailbutton.md) — An information button.
