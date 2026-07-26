---
title: actionSheetStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactionsheet/actionsheetstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/actionsheetstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/actionsheetstyle.json'
content_hash: 'sha256:d392b60199d68e90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# actionSheetStyle

<sub>Instance Property</sub>

The receiver’s presentation style.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var actionSheetStyle: UIActionSheetStyle { get set }
```

## Discussion

This property determines how the action sheet looks when it is presented. For a list of possible values, see the [UIActionSheetStyle](../uiactionsheetstyle.md) constants.

## See Also

### Setting properties

- [delegate](delegate.md) — The receiver’s delegate or `nil` if it doesn’t have a delegate. _(deprecated)_
- [title](title.md) — The string that appears in the receiver’s title bar. _(deprecated)_
- [visible](isvisible.md) — A Boolean value that indicates whether the receiver is displayed. _(deprecated)_
