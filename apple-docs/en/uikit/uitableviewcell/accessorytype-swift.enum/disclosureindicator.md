---
title: UITableViewCell.AccessoryType.disclosureIndicator
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator.json'
content_hash: 'sha256:8028e98ca6111ea1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITableViewCell](../../uitableviewcell.md) · [AccessoryType](../accessorytype-swift.enum.md)

# UITableViewCell.AccessoryType.disclosureIndicator

<sub>Case</sub>

A chevron-shaped control for presenting new content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case disclosureIndicator
```

## Discussion

Choose this type when you want taps in the accessory view to display new content. Connect the accessory view itself to a push segue to display that content.

The table view doesn’t call the delegate’s [- tableView:accessoryButtonTappedForRowWithIndexPath:](<../../uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>) method in response to touch events in this accessory view.

## See Also

### Accessory views

- [UITableViewCellAccessoryNone](none.md) — No accessory view.
- [UITableViewCellAccessoryDetailDisclosureButton](detaildisclosurebutton.md) — An information button and a disclosure (chevron) control.
- [UITableViewCellAccessoryCheckmark](checkmark.md) — A checkmark image.
- [UITableViewCellAccessoryDetailButton](detailbutton.md) — An information button.
