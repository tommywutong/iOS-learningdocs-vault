---
title: 'alertView(_:clickedButtonAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertviewdelegate/alertview(_:clickedbuttonat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertview(_:clickedbuttonat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertviewdelegate/alertview%28_%3Aclickedbuttonat%3A%29.json'
content_hash: 'sha256:dd3207dcd1950239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertViewDelegate](../uialertviewdelegate.md)

# alertView(_:clickedButtonAt:)

<sub>Instance Method</sub>

Sent to the delegate when the user clicks a button on an alert view.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func alertView(_ alertView: UIAlertView, clickedButtonAt buttonIndex: Int)
```

## Parameters

- `alertView` — The alert view containing the button.

- `buttonIndex` — The index of the button that was clicked. The button indices start at `0`.

## Discussion

The receiver is automatically dismissed after this method is invoked.
