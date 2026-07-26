---
title: isAuthenticationRequired
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimutableusernotificationaction/isauthenticationrequired
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/isauthenticationrequired'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationaction/isauthenticationrequired.json'
content_hash: 'sha256:ab17f38e97bca5ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableUserNotificationAction](../uimutableusernotificationaction.md)

# isAuthenticationRequired

<sub>Instance Property</sub>

A Boolean value indicating whether the user must unlock the device before the action is performed.

> [!warning] Deprecated
> For more information, see [UIMutableUserNotificationAction](../uimutableusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isAuthenticationRequired: Bool { get set }
```

## Discussion

The value of this property is ignored and treated as a value of [true](../../swift/true.md) when the value of the [activationMode](activationmode.md) property is set to [UIMutableUserNotificationAction](../uimutableusernotificationaction.md).

If your app uses data protection to encrypt data on disk, consider the data needs of the corresponding action before setting this property to [false](../../swift/false.md). For many data protection classes, data remains encrypted and unavailable while the device is locked. If your app needs to access encrypted data to perform a task, you likely need to set this property to [true](../../swift/true.md) to ensure that the data is accessible.

## See Also

### Configuring the action’s behavior

- [activationMode](activationmode.md) — The mode in which to run the app when the action is performed. _(deprecated)_
- [destructive](isdestructive.md) — A Boolean value indicating whether the action is destructive. _(deprecated)_
- [behavior](behavior.md) — The custom behavior (if any) that the action supports. _(deprecated)_
- [parameters](parameters.md) — A dictionary of additional parameters to include with the action. _(deprecated)_
