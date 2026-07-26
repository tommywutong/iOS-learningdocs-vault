---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uialertview/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/delegate.json'
content_hash: 'sha256:6a10e12b3ba04a45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# delegate

<sub>Instance Property</sub>

The receiver’s delegate or `nil` if it doesn’t have a delegate.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
weak var delegate: AnyObject? { get set }
```

## Discussion

See [UIAlertViewDelegate](../uialertviewdelegate.md) for the methods this delegate should implement.

## See Also

### Setting properties

- [alertViewStyle](alertviewstyle.md) — The kind of alert displayed to the user. _(deprecated)_
- [title](title.md) — The string that appears in the receiver’s title bar. _(deprecated)_
- [message](message.md) — Descriptive text that provides more details than the title. _(deprecated)_
- [visible](isvisible.md) — A Boolean value that indicates whether the receiver is displayed. _(deprecated)_
