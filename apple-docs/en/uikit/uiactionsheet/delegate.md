---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactionsheet/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/delegate.json'
content_hash: 'sha256:1c7b8504e8cbaa24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# delegate

<sub>Instance Property</sub>

The receiver’s delegate or `nil` if it doesn’t have a delegate.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
weak var delegate: (any UIActionSheetDelegate)? { get set }
```

## Discussion

For a list of methods your delegate object can implement, see [UIActionSheetDelegate](../uiactionsheetdelegate.md).

## See Also

### Setting properties

- [title](title.md) — The string that appears in the receiver’s title bar. _(deprecated)_
- [visible](isvisible.md) — A Boolean value that indicates whether the receiver is displayed. _(deprecated)_
- [actionSheetStyle](actionsheetstyle.md) — The receiver’s presentation style. _(deprecated)_
