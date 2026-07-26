---
title: isSelected
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/isselected
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/isselected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/isselected.json'
content_hash: 'sha256:7226189a389666bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# isSelected

<sub>Instance Property</sub>

A Boolean value that indicates whether the cell is selected.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isSelected: Bool { get set }
```

## Discussion

The selection affects the appearance of labels, image, and background. When the selected state of a cell is set to [true](../../swift/true.md), it draws the background for selected cells with its title in white. The default value is [false](../../swift/false.md). If you set the selection state to [true](../../swift/true.md) through this property, the transition to the new state appearance is not animated. For animated selected-state transitions, see the [- setSelected:animated:](<setselected(__animated_).md>) method.

## See Also

### Managing cell selection and highlighting

- [selectionStyle](selectionstyle-swift.property.md) — The style of selection for a cell.
- [SelectionStyle](selectionstyle-swift.enum.md) — The style of selected cells.
- [- setSelected:animated:](<setselected(__animated_).md>) — Sets the selected state of the cell, optionally animating the transition between states.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the cell is highlighted.
- [- setHighlighted:animated:](<sethighlighted(__animated_).md>) — Sets the highlighted state of the cell, optionally animating the transition between states.
