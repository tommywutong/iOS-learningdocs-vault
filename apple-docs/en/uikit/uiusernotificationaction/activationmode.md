---
title: activationMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationaction/activationmode
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationaction/activationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationaction/activationmode.json'
content_hash: 'sha256:1d8ad4311bd137c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationAction](../uiusernotificationaction.md)

# activationMode

<sub>Instance Property</sub>

The mode in which to run the app when the action is performed.

> [!warning] Deprecated
> For more information, see [UIUserNotificationAction](../uiusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var activationMode: UIUserNotificationActivationMode { get }
```

## Discussion

If the value in this property is [UIUserNotificationActivationModeForeground](../uiusernotificationactivationmode/foreground.md), the value of the [authenticationRequired](isauthenticationrequired.md) property is assumed to be [true](../../swift/true.md) regardless of its actual value.

## See Also

### Getting the action’s configuration

- [authenticationRequired](isauthenticationrequired.md) — A Boolean value indicating whether the user must unlock the device before the action is performed. _(deprecated)_
- [destructive](isdestructive.md) — A Boolean value indicating whether the action is destructive. _(deprecated)_
- [behavior](behavior.md) — The custom behavior (if any) that the action supports. _(deprecated)_
- [parameters](parameters.md) — A dictionary of additional parameters to include with the action. _(deprecated)_
