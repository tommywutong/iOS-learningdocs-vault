---
title: 'setSelected(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewcell/setselected(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/setselected(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/setselected%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:3b171ef3127a4600'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# setSelected(_:animated:)

<sub>Instance Method</sub>

Sets the selected state of the cell, optionally animating the transition between states.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setSelected(_ selected: Bool, animated: Bool)
```

## Parameters

- `selected` — [true](../../swift/true.md) to set the cell as selected, [false](../../swift/false.md) to set it as unselected. The default is [false](../../swift/false.md).

- `animated` — [true](../../swift/true.md) to animate the transition between selected states, [false](../../swift/false.md) to make the transition immediate.

## Discussion

The selection affects the appearance of labels, image, and background. When the selected state of a cell is [true](../../swift/true.md), it draws the background for selected cells (Reusing cells) with its title in white.

## See Also

### Managing cell selection and highlighting

- [selectionStyle](selectionstyle-swift.property.md) — The style of selection for a cell.
- [SelectionStyle](selectionstyle-swift.enum.md) — The style of selected cells.
- [selected](isselected.md) — A Boolean value that indicates whether the cell is selected.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the cell is highlighted.
- [- setHighlighted:animated:](<sethighlighted(__animated_).md>) — Sets the highlighted state of the cell, optionally animating the transition between states.
