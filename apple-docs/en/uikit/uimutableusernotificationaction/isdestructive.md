---
title: isDestructive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimutableusernotificationaction/isdestructive
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/isdestructive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationaction/isdestructive.json'
content_hash: 'sha256:be938d92e0107279'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableUserNotificationAction](../uimutableusernotificationaction.md)

# isDestructive

<sub>Instance Property</sub>

A Boolean value indicating whether the action is destructive.

> [!warning] Deprecated
> For more information, see [UIMutableUserNotificationAction](../uimutableusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isDestructive: Bool { get set }
```

## Discussion

Use this property to signal to the user whether the action causes destructive behavior to the user’s data or the app. When the value of this property is [true](../../swift/true.md), the system displays the corresponding button differently to indicate that the action is destructive.

The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring the action’s behavior

- [activationMode](activationmode.md) — The mode in which to run the app when the action is performed. _(deprecated)_
- [authenticationRequired](isauthenticationrequired.md) — A Boolean value indicating whether the user must unlock the device before the action is performed. _(deprecated)_
- [behavior](behavior.md) — The custom behavior (if any) that the action supports. _(deprecated)_
- [parameters](parameters.md) — A dictionary of additional parameters to include with the action. _(deprecated)_
