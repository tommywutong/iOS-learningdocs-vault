---
title: systemVersion
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/systemversion
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/systemversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/systemversion.json'
content_hash: 'sha256:2d48f518bef4f9a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# systemVersion

<sub>Instance Property</sub>

The current version of the operating system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var systemVersion: String { get }
```

## Discussion

An example of the system version is @“1.2”.

## See Also

### Identifying the device and operating system

- [name](name.md) — The name of the device.
- [systemName](systemname.md) — The name of the operating system running on the device.
- [model](model.md) — The model of the device.
- [localizedModel](localizedmodel.md) — The model of the device as a localized string.
- [userInterfaceIdiom](userinterfaceidiom.md) — The style of interface to use on the current device.
- [identifierForVendor](identifierforvendor.md) — An alphanumeric string that uniquely identifies a device to the app’s vendor.
