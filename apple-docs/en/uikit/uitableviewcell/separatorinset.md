---
title: separatorInset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/separatorinset
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/separatorinset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/separatorinset.json'
content_hash: 'sha256:d626c22ba4febaa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# separatorInset

<sub>Instance Property</sub>

The inset values for the separator line drawn beneath the cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var separatorInset: UIEdgeInsets { get set }
```

## Discussion

Use this property to indent the left and right edges of the separator line drawn beneath the cell. Positive inset values move the separator inward and away from edges of the cell. Negative values are treated as if the inset is set to 0.

The table view uses only the left and right inset values; it ignores the top and bottom inset values. The value assigned to this property takes precedence over any default separator insets set on the table view.

## See Also

### Managing content indentation

- [indentationLevel](indentationlevel.md) — The indentation level of the cell’s content.
- [indentationWidth](indentationwidth.md) — The width for each level of indentation of a cell’s content.
- [shouldIndentWhileEditing](shouldindentwhileediting.md) — A Boolean value that controls whether the cell background is indented when the table view is in editing mode.
- [SeparatorStyle](separatorstyle.md) — The style for cells to use as separators.
