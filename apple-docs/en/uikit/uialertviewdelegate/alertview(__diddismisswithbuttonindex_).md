---
title: 'alertView(_:didDismissWithButtonIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertviewdelegate/alertview(_:diddismisswithbuttonindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertview(_:diddismisswithbuttonindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertviewdelegate/alertview%28_%3Adiddismisswithbuttonindex%3A%29.json'
content_hash: 'sha256:d6cb7ed4cd0a382c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertViewDelegate](../uialertviewdelegate.md)

# alertView(_:didDismissWithButtonIndex:)

<sub>Instance Method</sub>

Sent to the delegate after an alert view is dismissed from the screen.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func alertView(_ alertView: UIAlertView, didDismissWithButtonIndex buttonIndex: Int)
```

## Parameters

- `alertView` — The alert view that was dismissed.

- `buttonIndex` — The index of the button that was clicked. The button indices start at `0`. If this is the cancel button index, the alert view is canceling. If `-1`, the cancel button index is not set.

## Discussion

This method is invoked after the animation ends and the view is hidden.

## See Also

### Customizing behavior

- [- alertViewShouldEnableFirstOtherButton:](<alertviewshouldenablefirstotherbutton(__).md>) — Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled. _(deprecated)_
- [- willPresentAlertView:](<willpresent(__).md>) — Sent to the delegate before a model view is presented to the user. _(deprecated)_
- [- didPresentAlertView:](<didpresent(__).md>) — Sent to the delegate after an alert view is presented to the user. _(deprecated)_
- [- alertView:willDismissWithButtonIndex:](<alertview(__willdismisswithbuttonindex_).md>) — Sent to the delegate before an alert view is dismissed. _(deprecated)_
