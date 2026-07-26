---
title: allowsFocus
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/allowsfocus
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/allowsfocus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/allowsfocus.json'
content_hash: 'sha256:5bafc8b210ecef4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# allowsFocus

<sub>Instance Property</sub>

A Boolean value that determines whether the table view allows its cells to become focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsFocus: Bool { get set }
```

## Discussion

If you implement [- tableView:canFocusRowAtIndexPath:](<../uitableviewdelegate/tableview(__canfocusrowat_).md>), its return value takes precedence over the value of this property.

The system determines the default value of this property according to the platform and other properties of the table view.

## See Also

### Working with focus

- [allowsFocusDuringEditing](allowsfocusduringediting.md) — A Boolean value that determines whether the table view allows its cells to become focused in edit mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
- [remembersLastFocusedIndexPath](rememberslastfocusedindexpath.md) — A Boolean value that indicates whether the table view automatically returns the focus to the cell at the last focused index path.
