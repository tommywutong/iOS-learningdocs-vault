---
title: 'alertViewCancel(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertviewdelegate/alertviewcancel(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertviewcancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertviewdelegate/alertviewcancel%28_%3A%29.json'
content_hash: 'sha256:da7e15d324ab49bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertViewDelegate](../uialertviewdelegate.md)

# alertViewCancel(_:)

<sub>Instance Method</sub>

Sent to the delegate before an alert view is canceled.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func alertViewCancel(_ alertView: UIAlertView)
```

## Parameters

- `alertView` — The alert view that will be canceled.

## Discussion

If the alert view’s delegate does not implement this method, clicking the cancel button is simulated and the alert view is dismissed. Implement this method if you need to perform some actions before an alert view is canceled. An alert view can be canceled at any time by the system—for example, when the user taps the Home button. The [- alertView:willDismissWithButtonIndex:](<alertview(__willdismisswithbuttonindex_).md>) and [- alertView:didDismissWithButtonIndex:](<alertview(__diddismisswithbuttonindex_).md>) methods are invoked after this method.
