---
title: UITableView.Style
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/style-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/style-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/style-swift.enum.json'
content_hash: 'sha256:0be4ac10bdcec8d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# UITableView.Style

<sub>Enumeration</sub>

Constants for the table view styles.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Style
```

## Overview

You set the table style when you initialize the table view (see [- initWithFrame:style:](<init(frame_style_).md>)). You can’t modify the style thereafter.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Styles

- [UITableViewStylePlain](style-swift.enum/plain.md) — A plain table view.
- [UITableViewStyleGrouped](style-swift.enum/grouped.md) — A table view where sections have distinct groups of rows.
- [UITableViewStyleInsetGrouped](style-swift.enum/insetgrouped.md) — A table view where the grouped sections are inset with rounded corners.

### Initializers

- [init(rawValue:)](<style-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the table’s appearance

- [style](style-swift.property.md) — The style of the table view.
- [tableHeaderView](tableheaderview.md) — The view that displays above the table’s content.
- [tableFooterView](tablefooterview.md) — The view that displays below the table’s content.
- [backgroundView](backgroundview.md) — The background view of the table view.
