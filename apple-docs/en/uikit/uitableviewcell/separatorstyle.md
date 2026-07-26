---
title: UITableViewCell.SeparatorStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/separatorstyle
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/separatorstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/separatorstyle.json'
content_hash: 'sha256:1b2bed068369da29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# UITableViewCell.SeparatorStyle

<sub>Enumeration</sub>

The style for cells to use as separators.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum SeparatorStyle
```

## Overview

You use these constants to set the value of the [separatorStyle](../uitableview/separatorstyle.md) property defined by [UITableView](../uitableview.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITableViewCellSeparatorStyleNone](separatorstyle/none.md) — The separator cell has no distinct style.
- [UITableViewCellSeparatorStyleSingleLine](separatorstyle/singleline.md) — The separator cell has a single line running across its width.
- [UITableViewCellSeparatorStyleSingleLineEtched](separatorstyle/singlelineetched.md) — The separator cell has double lines running across its width, giving it an etched look. _(deprecated)_

### Initializers

- [init(rawValue:)](<separatorstyle/init(rawvalue_).md>)

## See Also

### Customizing the separator appearance

- [separatorStyle](../uitableview/separatorstyle.md) — The style for table cells to use as separators.
- [separatorColor](../uitableview/separatorcolor.md) — The color of separator rows in the table view.
- [separatorEffect](../uitableview/separatoreffect.md) — The effect to apply to table separators.
- [separatorInset](../uitableview/separatorinset.md) — The default inset of cell separators.
- [separatorInsetReference](../uitableview/separatorinsetreference-swift.property.md) — An indicator of how to interpret the separator inset value.
- [SeparatorInsetReference](../uitableview/separatorinsetreference-swift.enum.md) — Constants that indicate how to interpret the separator inset value of a table view.
