---
title: endUpdates()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/endupdates()
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/endupdates()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/endupdates%28%29.json'
content_hash: 'sha256:c444acb84b7cc5ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# endUpdates()

<sub>Instance Method</sub>

Concludes a series of method calls that insert, delete, select, or reload rows and sections of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func endUpdates()
```

## Discussion

Use the [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) method instead of this one whenever possible.

You call this method to bracket a series of method calls that begins with [- beginUpdates](<beginupdates().md>) and that consists of operations to insert, delete, select, and reload rows and sections of the table view. When you call `endUpdates`, `UITableView` animates the operations simultaneously. Invocations of [- beginUpdates](<beginupdates().md>) and `endUpdates` can be nested. If you don’t make the insertion, deletion, and selection calls inside this block, table attributes such as row count can become invalid.

## See Also

### Performing batch updates to rows and sections

- [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) — Animates multiple insert, delete, reload, and move operations as a group.
- [- beginUpdates](<beginupdates().md>) — Begins a series of method calls that insert, delete, or select rows and sections of the table view.
