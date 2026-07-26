---
title: UITableView.SeparatorInsetReference.fromCellEdges
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/separatorinsetreference-swift.enum/fromcelledges
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/separatorinsetreference-swift.enum/fromcelledges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/separatorinsetreference-swift.enum/fromcelledges.json'
content_hash: 'sha256:83f531b5eb9c9635'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITableView](../../uitableview.md) · [SeparatorInsetReference](../separatorinsetreference-swift.enum.md)

# UITableView.SeparatorInsetReference.fromCellEdges

<sub>Case</sub>

An inset value that’s relative to the edge of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case fromCellEdges
```

## Discussion

When this style is active, setting the left and right insets to `0.0` would result in a separator to extend from the entire distance between the left and right edges of the cell. Setting the insets to other values would inset the separator by the specified amount.

## See Also

### Constants

- [UITableViewSeparatorInsetFromAutomaticInsets](fromautomaticinsets.md) — An inset value that indicates the starting position is based on the default separator insets.
