---
title: 'willPresent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertviewdelegate/willpresent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertviewdelegate/willpresent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertviewdelegate/willpresent%28_%3A%29.json'
content_hash: 'sha256:86b086fe80967f4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertViewDelegate](../uialertviewdelegate.md)

# willPresent(_:)

<sub>Instance Method</sub>

Sent to the delegate before a model view is presented to the user.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func willPresent(_ alertView: UIAlertView)
```

## Parameters

- `alertView` — The alert view that is about to be displayed.

## See Also

### Customizing behavior

- [- alertViewShouldEnableFirstOtherButton:](<alertviewshouldenablefirstotherbutton(__).md>) — Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled. _(deprecated)_
- [- didPresentAlertView:](<didpresent(__).md>) — Sent to the delegate after an alert view is presented to the user. _(deprecated)_
- [- alertView:willDismissWithButtonIndex:](<alertview(__willdismisswithbuttonindex_).md>) — Sent to the delegate before an alert view is dismissed. _(deprecated)_
- [- alertView:didDismissWithButtonIndex:](<alertview(__diddismisswithbuttonindex_).md>) — Sent to the delegate after an alert view is dismissed from the screen. _(deprecated)_
