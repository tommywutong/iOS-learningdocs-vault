---
title: identifierForVendor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/identifierforvendor
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/identifierforvendor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/identifierforvendor.json'
content_hash: 'sha256:d4f92530850bdee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# identifierForVendor

<sub>Instance Property</sub>

An alphanumeric string that uniquely identifies a device to the app’s vendor.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var identifierForVendor: UUID? { get }
```

## Discussion

The value of this property is the same for apps that come from the same vendor running on the same device. A different value is returned for apps on the same device that come from different vendors, and for apps on different devices regardless of vendor.

Normally, the vendor is determined by data provided by the App Store. If the app wasn’t installed from the app store (such as enterprise apps and apps still in development), then a vendor identifier is calculated based on the app’s bundle ID. The bundle ID is assumed to be in reverse-DNS format.

- In iOS 6, the first two components of the bundle ID are used to generate the vendor ID. If the bundle ID only has a single component, then the entire bundle ID is used.
- In IOS 7, all components of the bundle except for the last component are used to generate the vendor ID. If the bundle ID only has a single component, then the entire bundle ID is used.

The following table shows a collection of bundle IDs and which portions of the bundle ID the system uses to calculate the vendor ID.

| Bundle ID | iOS 6.x | iOS 7.x |
|---|---|---|
| Com.example.app1 | **Com.example**.app1 | **Com.example**.app1 |
| Com.example.app2 | **Com.example**.app2 | **Com.example**.app2 |
| Com.example.app.app1 | **Com.example**.app.app1 | **Com.example.app**.app1 |
| Com.example.app.app2 | **Com.example**.app.app2 | **Com.example.app**.app2 |
| Example | **Example** | **Example** |

For example, `com.example.app1` and `com.example.app2` would appear to have the same vendor ID.

If the value is `nil`, wait and get the value again later. This happens, for example, after the device has been restarted but before the user has unlocked the device.

The value in this property remains the same while the app (or another app from the same vendor) is installed on the iOS device. The value changes when the user deletes all of that vendor’s apps from the device and subsequently reinstalls one or more of them. The value can also change when installing test builds using Xcode or when installing an app on a device using ad-hoc distribution. Therefore, if your app stores the value of this property anywhere, you should gracefully handle situations where the identifier changes.

## See Also

### Identifying the device and operating system

- [name](name.md) — The name of the device.
- [systemName](systemname.md) — The name of the operating system running on the device.
- [systemVersion](systemversion.md) — The current version of the operating system.
- [model](model.md) — The model of the device.
- [localizedModel](localizedmodel.md) — The model of the device as a localized string.
- [userInterfaceIdiom](userinterfaceidiom.md) — The style of interface to use on the current device.
