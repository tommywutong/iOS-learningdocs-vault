---
title: 'setHighlighted(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewcell/sethighlighted(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/sethighlighted(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/sethighlighted%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:cb9dde313e7ab3ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# setHighlighted(_:animated:)

<sub>Instance Method</sub>

Sets the highlighted state of the cell, optionally animating the transition between states.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setHighlighted(_ highlighted: Bool, animated: Bool)
```

## Parameters

- `highlighted` — [true](../../swift/true.md) to set the cell as highlighted, [false](../../swift/false.md) to set it as unhighlighted. The default is [false](../../swift/false.md).

- `animated` — [true](../../swift/true.md) to animate the transition between highlighted states, [false](../../swift/false.md) to make the transition immediate.

## Discussion

Highlights or unhighlights the cell, animating the transition between regular and highlighted state if `animated` is YES.  Highlighting affects the appearance of the cell’s labels, image, and background.

Note that for highlighting to work properly, you must fetch the cell’s label (or labels) using the [textLabel](textlabel.md) (and [detailTextLabel](detailtextlabel.md) properties and set the label’s [highlightedTextColor](../uilabel/highlightedtextcolor.md) property; for images, get the cell’s image using the [imageView](imageview.md) property and set the [UIImageView](../uiimageview.md) object’s `highlightedImage` property.

A custom table cell may override this method to make any transitory appearance changes.

## See Also

### Managing cell selection and highlighting

- [selectionStyle](selectionstyle-swift.property.md) — The style of selection for a cell.
- [SelectionStyle](selectionstyle-swift.enum.md) — The style of selected cells.
- [selected](isselected.md) — A Boolean value that indicates whether the cell is selected.
- [- setSelected:animated:](<setselected(__animated_).md>) — Sets the selected state of the cell, optionally animating the transition between states.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the cell is highlighted.
