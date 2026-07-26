---
title: name
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/name
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/name.json'
content_hash: 'sha256:4ae2333d425ac998'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# name

<sub>Instance Property</sub>

The name of the device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var name: String { get }
```

## Discussion

The default value of this property varies according to the device’s operating system version number:

| OS | Default value | Example |
|---|---|---|
| iOS 15 and earlier | User-assigned device name | `"Ravi’s iPhone 13 Pro"` |
| iOS 16 and later | Generic device name | `"iPhone"` |

In iOS, the _user-assigned device name_ is available in the Settings app under General \> About \> Name. To access the user-assigned device name through this property in iOS 16 and later, your app must meet certain criteria and be assigned an entitlement. For information, see [com.apple.developer.device-information.user-assigned-device-name](../../bundleresources/entitlements/com.apple.developer.device-information.user-assigned-device-name.md).

> [!note] Related Sessions from WWDC22
> Session 10096: [What’s new in privacy](https://developer.apple.com/videos/play/wwdc2022/10096)
>
> Session 10068: [What’s new in UIKit](https://developer.apple.com/videos/play/wwdc2022/10068)

## See Also

### Identifying the device and operating system

- [systemName](systemname.md) — The name of the operating system running on the device.
- [systemVersion](systemversion.md) — The current version of the operating system.
- [model](model.md) — The model of the device.
- [localizedModel](localizedmodel.md) — The model of the device as a localized string.
- [userInterfaceIdiom](userinterfaceidiom.md) — The style of interface to use on the current device.
- [identifierForVendor](identifierforvendor.md) — An alphanumeric string that uniquely identifies a device to the app’s vendor.
