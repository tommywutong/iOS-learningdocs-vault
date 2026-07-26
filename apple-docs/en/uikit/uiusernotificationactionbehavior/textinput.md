---
title: UIUserNotificationActionBehavior.textInput
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationactionbehavior/textinput
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationactionbehavior/textinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationactionbehavior/textinput.json'
content_hash: 'sha256:5ec0daca3cb9f5a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationActionBehavior](../uiusernotificationactionbehavior.md)

# UIUserNotificationActionBehavior.textInput

<sub>Case</sub>

The text input behavior.

> [!warning] Deprecated
> For more information, see [UIUserNotificationAction](../uiusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case textInput
```

## Discussion

When specified, the system provides a way for the user to enter a text response to be included with the notification. The text response is assigned to the [UIUserNotificationActionResponseTypedTextKey](../uiusernotificationactionresponsetypedtextkey.md) of the response information dictionary when the notification is delivered to your app.

## See Also

### Constants

- [UIUserNotificationActionBehaviorDefault](default.md) — The default action behavior. When specified, the action supports no additional behaviors. _(deprecated)_
