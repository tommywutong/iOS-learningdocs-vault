---
title: selectionStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/selectionstyle-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/selectionstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/selectionstyle-swift.property.json'
content_hash: 'sha256:37077931b9678909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# selectionStyle

<sub>Instance Property</sub>

The style of selection for a cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectionStyle: UITableViewCell.SelectionStyle { get set }
```

## Discussion

The selection style is a [backgroundView](backgroundview.md) constant that determines the color of a cell when it’s selected. The default value is [UITableViewCellSelectionStyleDefault](selectionstyle-swift.enum/default.md). See [SelectionStyle](selectionstyle-swift.enum.md) for a description of valid constants.

## See Also

### Managing cell selection and highlighting

- [SelectionStyle](selectionstyle-swift.enum.md) — The style of selected cells.
- [selected](isselected.md) — A Boolean value that indicates whether the cell is selected.
- [- setSelected:animated:](<setselected(__animated_).md>) — Sets the selected state of the cell, optionally animating the transition between states.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the cell is highlighted.
- [- setHighlighted:animated:](<sethighlighted(__animated_).md>) — Sets the highlighted state of the cell, optionally animating the transition between states.
