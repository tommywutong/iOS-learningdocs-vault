---
title: beginUpdates()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/beginupdates()
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/beginupdates()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/beginupdates%28%29.json'
content_hash: 'sha256:e120a2ad69cd8e24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# beginUpdates()

<sub>Instance Method</sub>

Begins a series of method calls that insert, delete, or select rows and sections of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func beginUpdates()
```

## Discussion

Use the [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) method instead of this one whenever possible.

Call this method if you want subsequent insertions, deletion, and selection operations (for example, [- cellForRowAtIndexPath:](<cellforrow(at_).md>) and [indexPathsForVisibleRows](indexpathsforvisiblerows.md)) to be animated simultaneously. You can also use this method followed by the [- endUpdates](<endupdates().md>) method to animate the change in the row heights without reloading the cell. This group of methods must conclude with an invocation of [- endUpdates](<endupdates().md>). These method pairs can be nested. If you don’t make the insertion, deletion, and selection calls inside this block, table attributes such as row count might become invalid. You shouldn’t call [- reloadData](<reloaddata().md>) within the group; if you call this method within the group, you must perform any animations yourself.

## See Also

### Performing batch updates to rows and sections

- [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) — Animates multiple insert, delete, reload, and move operations as a group.
- [- endUpdates](<endupdates().md>) — Concludes a series of method calls that insert, delete, select, or reload rows and sections of the table view.
