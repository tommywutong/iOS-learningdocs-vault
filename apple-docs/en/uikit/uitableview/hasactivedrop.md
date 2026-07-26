---
title: hasActiveDrop
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/hasactivedrop
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/hasactivedrop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/hasactivedrop.json'
content_hash: 'sha256:57dce814560cec59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# hasActiveDrop

<sub>Instance Property</sub>

A Boolean value that indicates whether the table view is currently tracking a drop session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hasActiveDrop: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the table view is tracking a drop session.

## See Also

### Managing drop interactions

- [dropDelegate](dropdelegate.md) — The delegate object that manages the dropping of content into the table view.
- [UITableViewDropDelegate](../uitableviewdropdelegate.md) — The interface for handling drops in a table view.
