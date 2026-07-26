---
title: isVisible
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uialertview/isvisible
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/isvisible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/isvisible.json'
content_hash: 'sha256:b3b488d6b66eb33e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# isVisible

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is displayed.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isVisible: Bool { get }
```

## Discussion

If [true](../../swift/true.md), the receiver is displayed; otherwise, [false](../../swift/false.md).

## See Also

### Setting properties

- [delegate](delegate.md) — The receiver’s delegate or `nil` if it doesn’t have a delegate. _(deprecated)_
- [alertViewStyle](alertviewstyle.md) — The kind of alert displayed to the user. _(deprecated)_
- [title](title.md) — The string that appears in the receiver’s title bar. _(deprecated)_
- [message](message.md) — Descriptive text that provides more details than the title. _(deprecated)_
