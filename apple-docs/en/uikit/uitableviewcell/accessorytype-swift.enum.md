---
title: UITableViewCell.AccessoryType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/accessorytype-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/accessorytype-swift.enum.json'
content_hash: 'sha256:28b6864d331eb3b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# UITableViewCell.AccessoryType

<sub>Enumeration</sub>

The type of standard accessory control used by a cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum AccessoryType
```

## Overview

Use these constants to set the value of the [accessoryType](accessorytype-swift.property.md) property.

Several accessory views support additional interactions. For example, a detail button conveys that there is additional information for the user to see. For information about how to respond to interactions with a specific accessory view, see the discussion for that type.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Accessory views

- [UITableViewCellAccessoryNone](accessorytype-swift.enum/none.md) — No accessory view.
- [UITableViewCellAccessoryDisclosureIndicator](accessorytype-swift.enum/disclosureindicator.md) — A chevron-shaped control for presenting new content.
- [UITableViewCellAccessoryDetailDisclosureButton](accessorytype-swift.enum/detaildisclosurebutton.md) — An information button and a disclosure (chevron) control.
- [UITableViewCellAccessoryCheckmark](accessorytype-swift.enum/checkmark.md) — A checkmark image.
- [UITableViewCellAccessoryDetailButton](accessorytype-swift.enum/detailbutton.md) — An information button.

### Initializers

- [init(rawValue:)](<accessorytype-swift.enum/init(rawvalue_).md>)

## See Also

### Managing accessory views

- [accessoryType](accessorytype-swift.property.md) — The type of standard accessory view for the cell to use in the table view’s normal state.
- [accessoryView](accessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [editingAccessoryType](editingaccessorytype.md) — The type of standard accessory view for the cell to use in the table view’s editing state.
- [editingAccessoryView](editingaccessoryview.md) — The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
