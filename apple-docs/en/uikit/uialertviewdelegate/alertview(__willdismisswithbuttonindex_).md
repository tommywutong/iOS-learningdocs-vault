---
title: 'alertView(_:willDismissWithButtonIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertviewdelegate/alertview(_:willdismisswithbuttonindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertview(_:willdismisswithbuttonindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertviewdelegate/alertview%28_%3Awilldismisswithbuttonindex%3A%29.json'
content_hash: 'sha256:9c067e7305ac6d6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertViewDelegate](../uialertviewdelegate.md)

# alertView(_:willDismissWithButtonIndex:)

<sub>Instance Method</sub>

Sent to the delegate before an alert view is dismissed.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func alertView(_ alertView: UIAlertView, willDismissWithButtonIndex buttonIndex: Int)
```

## Parameters

- `alertView` — The alert view that is about to be dismissed.

- `buttonIndex` — The index of the button that was clicked. The button indices start at `0`. If this is the cancel button index, the alert view is canceling. If `-1`, the cancel button index is not set.

## Discussion

This method is invoked before the animation begins and the view is hidden.

## See Also

### Customizing behavior

- [- alertViewShouldEnableFirstOtherButton:](<alertviewshouldenablefirstotherbutton(__).md>) — Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled. _(deprecated)_
- [- willPresentAlertView:](<willpresent(__).md>) — Sent to the delegate before a model view is presented to the user. _(deprecated)_
- [- didPresentAlertView:](<didpresent(__).md>) — Sent to the delegate after an alert view is presented to the user. _(deprecated)_
- [- alertView:didDismissWithButtonIndex:](<alertview(__diddismisswithbuttonindex_).md>) — Sent to the delegate after an alert view is dismissed from the screen. _(deprecated)_
