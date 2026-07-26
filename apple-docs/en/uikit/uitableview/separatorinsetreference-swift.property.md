---
title: separatorInsetReference
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/separatorinsetreference-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/separatorinsetreference-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/separatorinsetreference-swift.property.json'
content_hash: 'sha256:7efe9abdfb0f53ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# separatorInsetReference

<sub>Instance Property</sub>

An indicator of how to interpret the separator inset value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var separatorInsetReference: UITableView.SeparatorInsetReference { get set }
```

## Discussion

Use the value of this property to determine how the value in the separatorInset property is interpreted for cells. The default value of this property is [UITableViewSeparatorInsetFromCellEdges](separatorinsetreference-swift.enum/fromcelledges.md).

## See Also

### Customizing the separator appearance

- [separatorStyle](separatorstyle.md) — The style for table cells to use as separators.
- [SeparatorStyle](../uitableviewcell/separatorstyle.md) — The style for cells to use as separators.
- [separatorColor](separatorcolor.md) — The color of separator rows in the table view.
- [separatorEffect](separatoreffect.md) — The effect to apply to table separators.
- [separatorInset](separatorinset.md) — The default inset of cell separators.
- [SeparatorInsetReference](separatorinsetreference-swift.enum.md) — Constants that indicate how to interpret the separator inset value of a table view.
