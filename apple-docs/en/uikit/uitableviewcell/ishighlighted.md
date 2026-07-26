---
title: isHighlighted
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/ishighlighted
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/ishighlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/ishighlighted.json'
content_hash: 'sha256:a1e5913b7c336778'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# isHighlighted

<sub>Instance Property</sub>

A Boolean value that indicates whether the cell is highlighted.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHighlighted: Bool { get set }
```

## Discussion

The highlighting affects the appearance of labels, image, and background. When the highlighted state of a cell is set to [true](../../swift/true.md), labels are drawn in their highlighted text color (default is white). The default value is [false](../../swift/false.md). If you set the highlighted state to [true](../../swift/true.md) through this property, the transition to the new state appearance is not animated. For animated highlighted-state transitions, see the [- setHighlighted:animated:](<sethighlighted(__animated_).md>) method.

Note that for highlighting to work properly, you must fetch the cell’s labels using the [textLabel](textlabel.md) and [detailTextLabel](detailtextlabel.md) properties and set each label’s [highlightedTextColor](../uilabel/highlightedtextcolor.md) property; for images, get the cell’s image using the [imageView](imageview.md) property and set the [UIImageView](../uiimageview.md) object’s `highlightedImage` property.

## See Also

### Managing cell selection and highlighting

- [selectionStyle](selectionstyle-swift.property.md) — The style of selection for a cell.
- [SelectionStyle](selectionstyle-swift.enum.md) — The style of selected cells.
- [selected](isselected.md) — A Boolean value that indicates whether the cell is selected.
- [- setSelected:animated:](<setselected(__animated_).md>) — Sets the selected state of the cell, optionally animating the transition between states.
- [- setHighlighted:animated:](<sethighlighted(__animated_).md>) — Sets the highlighted state of the cell, optionally animating the transition between states.
