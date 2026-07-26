---
title: UITableViewCell.SelectionStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/selectionstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/selectionstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/selectionstyle-swift.enum.json'
content_hash: 'sha256:928c0af5e9abf693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# UITableViewCell.SelectionStyle

<sub>Enumeration</sub>

The style of selected cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum SelectionStyle
```

## Overview

You use these constants to set the value of the [selectionStyle](selectionstyle-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITableViewCellSelectionStyleNone](selectionstyle-swift.enum/none.md) — The cell has no distinct style for when it’s selected.
- [UITableViewCellSelectionStyleBlue](selectionstyle-swift.enum/blue.md) — The cell has a default background color when it’s selected.
- [UITableViewCellSelectionStyleGray](selectionstyle-swift.enum/gray.md) — The cell has a gray background when it’s selected.
- [UITableViewCellSelectionStyleDefault](selectionstyle-swift.enum/default.md) — The cell selection style to use for tables.

### Initializers

- [init(rawValue:)](<selectionstyle-swift.enum/init(rawvalue_).md>)

## See Also

### Managing cell selection and highlighting

- [selectionStyle](selectionstyle-swift.property.md) — The style of selection for a cell.
- [selected](isselected.md) — A Boolean value that indicates whether the cell is selected.
- [- setSelected:animated:](<setselected(__animated_).md>) — Sets the selected state of the cell, optionally animating the transition between states.
- [highlighted](ishighlighted.md) — A Boolean value that indicates whether the cell is highlighted.
- [- setHighlighted:animated:](<sethighlighted(__animated_).md>) — Sets the highlighted state of the cell, optionally animating the transition between states.
