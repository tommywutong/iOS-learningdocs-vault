---
title: 'alertViewShouldEnableFirstOtherButton(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertviewdelegate/alertviewshouldenablefirstotherbutton(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertviewshouldenablefirstotherbutton(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertviewdelegate/alertviewshouldenablefirstotherbutton%28_%3A%29.json'
content_hash: 'sha256:1bb73c85de760fb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertViewDelegate](../uialertviewdelegate.md)

# alertViewShouldEnableFirstOtherButton(_:)

<sub>Instance Method</sub>

Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func alertViewShouldEnableFirstOtherButton(_ alertView: UIAlertView) -> Bool
```

## Parameters

- `alertView` — The alert view that is being configured.

## Return Value

[true](../../swift/true.md) if the button should be enabled, no if the button should be disabled.

## See Also

### Customizing behavior

- [- willPresentAlertView:](<willpresent(__).md>) — Sent to the delegate before a model view is presented to the user. _(deprecated)_
- [- didPresentAlertView:](<didpresent(__).md>) — Sent to the delegate after an alert view is presented to the user. _(deprecated)_
- [- alertView:willDismissWithButtonIndex:](<alertview(__willdismisswithbuttonindex_).md>) — Sent to the delegate before an alert view is dismissed. _(deprecated)_
- [- alertView:didDismissWithButtonIndex:](<alertview(__diddismisswithbuttonindex_).md>) — Sent to the delegate after an alert view is dismissed from the screen. _(deprecated)_
