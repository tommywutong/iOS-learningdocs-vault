---
title: userInteractionEnabledWhileDragging
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/userinteractionenabledwhiledragging
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/userinteractionenabledwhiledragging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/userinteractionenabledwhiledragging.json'
content_hash: 'sha256:a148298bc0f628ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# userInteractionEnabledWhileDragging

<sub>Instance Property</sub>

A Boolean value indicating whether users can interact with a cell while it is being dragged.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var userInteractionEnabledWhileDragging: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md).

## See Also

### Dragging the row

- [- dragStateDidChange:](<dragstatedidchange(__).md>) — Notifies the cell that its drag status changed.
- [DragState](dragstate.md) — Constants indicating the current state of a row involved in a drag operation.
