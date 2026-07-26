---
title: indentationWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/indentationwidth
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/indentationwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/indentationwidth.json'
content_hash: 'sha256:93e57d087109302a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# indentationWidth

<sub>Instance Property</sub>

The width for each level of indentation of a cell’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indentationWidth: CGFloat { get set }
```

## Discussion

The default indentation width is `10.0` points.

## See Also

### Managing content indentation

- [indentationLevel](indentationlevel.md) — The indentation level of the cell’s content.
- [shouldIndentWhileEditing](shouldindentwhileediting.md) — A Boolean value that controls whether the cell background is indented when the table view is in editing mode.
- [separatorInset](separatorinset.md) — The inset values for the separator line drawn beneath the cell.
- [SeparatorStyle](separatorstyle.md) — The style for cells to use as separators.
