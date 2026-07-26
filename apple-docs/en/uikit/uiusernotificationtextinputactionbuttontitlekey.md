---
title: UIUserNotificationTextInputActionButtonTitleKey
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationtextinputactionbuttontitlekey
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationtextinputactionbuttontitlekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationtextinputactionbuttontitlekey.json'
content_hash: 'sha256:82847a6b4a7390ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserNotificationTextInputActionButtonTitleKey

<sub>Global Variable</sub>

The key for specifying the title of the text input button.

> [!warning] Deprecated
> For more information, see [UIUserNotificationAction](uiusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
let UIUserNotificationTextInputActionButtonTitleKey: String
```

## Description

The value of this key is an [NSString](../foundation/nsstring.md) object. When the user chooses to provide a text response to a notification, UIKit displays an interface for entering that response. The value of this key is used on the button that the user taps to accept that text and attach it to the notification.
