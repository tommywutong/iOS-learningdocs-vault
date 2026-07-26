---
title: indentationLevel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/indentationlevel
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/indentationlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/indentationlevel.json'
content_hash: 'sha256:943a8c672cbf42f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# indentationLevel

<sub>Instance Property</sub>

The indentation level of the cell’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indentationLevel: Int { get set }
```

## Discussion

The default value of the property is zero (no indentation). Assigning a positive value to this property indents the cell’s content from the left edge of the cell separator. The amount of indentation is equal to the indentation level multiplied by the value in the [indentationWidth](indentationwidth.md) property.

## See Also

### Managing content indentation

- [indentationWidth](indentationwidth.md) — The width for each level of indentation of a cell’s content.
- [shouldIndentWhileEditing](shouldindentwhileediting.md) — A Boolean value that controls whether the cell background is indented when the table view is in editing mode.
- [separatorInset](separatorinset.md) — The inset values for the separator line drawn beneath the cell.
- [SeparatorStyle](separatorstyle.md) — The style for cells to use as separators.
