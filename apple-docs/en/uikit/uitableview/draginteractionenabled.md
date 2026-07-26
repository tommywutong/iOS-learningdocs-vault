---
title: dragInteractionEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/draginteractionenabled
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/draginteractionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/draginteractionenabled.json'
content_hash: 'sha256:c7a8447af89257fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# dragInteractionEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the table view supports dragging content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var dragInteractionEnabled: Bool { get set }
```

## Discussion

To support dragging content from the table view to a view in your app or another app, set this property value to [true](../../swift/true.md). To disable this behavior, set the value to [false](../../swift/false.md). The default value is [true](../../swift/true.md).

In iOS 14 and earlier, the default value is [true](../../swift/true.md) for iPad and [false](../../swift/false.md) for iPhone. Setting the value to [true](../../swift/true.md) on iPhone enables dragging within your app only. Dragging content to other apps isn’t possible on iPhone prior to iOS 15.

## See Also

### Managing drag interactions

- [dragDelegate](dragdelegate.md) — The delegate object that manages the dragging of items from the table view.
- [UITableViewDragDelegate](../uitableviewdragdelegate.md) — The interface for initiating drags from a table view.
- [hasActiveDrag](hasactivedrag.md) — A Boolean value that indicates whether the table view is currently tracking a drag session.
