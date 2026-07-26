---
title: parameters
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimutableusernotificationaction/parameters
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/parameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationaction/parameters.json'
content_hash: 'sha256:31ad8a8c512eeff9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableUserNotificationAction](../uimutableusernotificationaction.md)

# parameters

<sub>Instance Property</sub>

A dictionary of additional parameters to include with the action.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var parameters: [AnyHashable : Any] { get set }
```

## Discussion

Use this dictionary to specify any behavior-specific data for the action. For example, the `UIUserNotificationActionBehaviorTextInput` behavior supports the `UIUserNotificationTextInputActionButtonTitleKey` key, which lets you customize the title of the button displayed by the text input interface.

## See Also

### Configuring the action’s behavior

- [activationMode](activationmode.md) — The mode in which to run the app when the action is performed. _(deprecated)_
- [authenticationRequired](isauthenticationrequired.md) — A Boolean value indicating whether the user must unlock the device before the action is performed. _(deprecated)_
- [destructive](isdestructive.md) — A Boolean value indicating whether the action is destructive. _(deprecated)_
- [behavior](behavior.md) — The custom behavior (if any) that the action supports. _(deprecated)_
