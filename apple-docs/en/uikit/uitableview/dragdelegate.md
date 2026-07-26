---
title: dragDelegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/dragdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/dragdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/dragdelegate.json'
content_hash: 'sha256:4c938068bb152d72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# dragDelegate

<sub>Instance Property</sub>

The delegate object that manages the dragging of items from the table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var dragDelegate: (any UITableViewDragDelegate)? { get set }
```

## See Also

### Managing drag interactions

- [UITableViewDragDelegate](../uitableviewdragdelegate.md) — The interface for initiating drags from a table view.
- [hasActiveDrag](hasactivedrag.md) — A Boolean value that indicates whether the table view is currently tracking a drag session.
- [dragInteractionEnabled](draginteractionenabled.md) — A Boolean value that indicates whether the table view supports dragging content.
