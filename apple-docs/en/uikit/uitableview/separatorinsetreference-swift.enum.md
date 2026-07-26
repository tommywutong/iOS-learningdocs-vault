---
title: UITableView.SeparatorInsetReference
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/separatorinsetreference-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/separatorinsetreference-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/separatorinsetreference-swift.enum.json'
content_hash: 'sha256:1bf5f95d7448afe7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# UITableView.SeparatorInsetReference

<sub>Enumeration</sub>

Constants that indicate how to interpret the separator inset value of a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum SeparatorInsetReference
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITableViewSeparatorInsetFromCellEdges](separatorinsetreference-swift.enum/fromcelledges.md) — An inset value that’s relative to the edge of the cell.
- [UITableViewSeparatorInsetFromAutomaticInsets](separatorinsetreference-swift.enum/fromautomaticinsets.md) — An inset value that indicates the starting position is based on the default separator insets.

### Initializers

- [init(rawValue:)](<separatorinsetreference-swift.enum/init(rawvalue_).md>)

## See Also

### Customizing the separator appearance

- [separatorStyle](separatorstyle.md) — The style for table cells to use as separators.
- [SeparatorStyle](../uitableviewcell/separatorstyle.md) — The style for cells to use as separators.
- [separatorColor](separatorcolor.md) — The color of separator rows in the table view.
- [separatorEffect](separatoreffect.md) — The effect to apply to table separators.
- [separatorInset](separatorinset.md) — The default inset of cell separators.
- [separatorInsetReference](separatorinsetreference-swift.property.md) — An indicator of how to interpret the separator inset value.
