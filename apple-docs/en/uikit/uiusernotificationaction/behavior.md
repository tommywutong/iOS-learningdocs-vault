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
doc_path: /documentation/uikit/uiusernotificationaction/behavior
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationaction/behavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationaction/behavior.json'
content_hash: 'sha256:259a34699372e57f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationAction](../uiusernotificationaction.md)

# behavior

<sub>Instance Property</sub>

The custom behavior (if any) that the action supports.

> [!warning] Deprecated
> For more information, see [UIUserNotificationAction](../uiusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var behavior: UIUserNotificationActionBehavior { get }
```

## Discussion

The default value of this property is [UIUserNotificationActionBehaviorDefault](../uiusernotificationactionbehavior/default.md).

## See Also

### Getting the action’s configuration

- [activationMode](activationmode.md) — The mode in which to run the app when the action is performed. _(deprecated)_
- [authenticationRequired](isauthenticationrequired.md) — A Boolean value indicating whether the user must unlock the device before the action is performed. _(deprecated)_
- [destructive](isdestructive.md) — A Boolean value indicating whether the action is destructive. _(deprecated)_
- [parameters](parameters.md) — A dictionary of additional parameters to include with the action. _(deprecated)_
