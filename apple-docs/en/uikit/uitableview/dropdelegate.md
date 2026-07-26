---
title: dropDelegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/dropdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/dropdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/dropdelegate.json'
content_hash: 'sha256:44792a169907ba6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# dropDelegate

<sub>Instance Property</sub>

The delegate object that manages the dropping of content into the table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var dropDelegate: (any UITableViewDropDelegate)? { get set }
```

## See Also

### Managing drop interactions

- [UITableViewDropDelegate](../uitableviewdropdelegate.md) — The interface for handling drops in a table view.
- [hasActiveDrop](hasactivedrop.md) — A Boolean value that indicates whether the table view is currently tracking a drop session.
