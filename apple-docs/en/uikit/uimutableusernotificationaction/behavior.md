---
title: behavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimutableusernotificationaction/behavior
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/behavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationaction/behavior.json'
content_hash: 'sha256:572763384f3787b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableUserNotificationAction](../uimutableusernotificationaction.md)

# behavior

<sub>Instance Property</sub>

The custom behavior (if any) that the action supports.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var behavior: UIUserNotificationActionBehavior { get set }
```

## Discussion

The default value of this property is `UIUserNotificationActionBehaviorDefault`.

## See Also

### Configuring the action’s behavior

- [activationMode](activationmode.md) — The mode in which to run the app when the action is performed. _(deprecated)_
- [authenticationRequired](isauthenticationrequired.md) — A Boolean value indicating whether the user must unlock the device before the action is performed. _(deprecated)_
- [destructive](isdestructive.md) — A Boolean value indicating whether the action is destructive. _(deprecated)_
- [parameters](parameters.md) — A dictionary of additional parameters to include with the action. _(deprecated)_
