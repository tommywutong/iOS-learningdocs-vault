---
title: model
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/model
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/model'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/model.json'
content_hash: 'sha256:f813befee709695d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# model

<sub>Instance Property</sub>

The model of the device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var model: String { get }
```

## Discussion

Possible examples of model strings are “iPhone” and “iPod touch”.

## See Also

### Identifying the device and operating system

- [name](name.md) — The name of the device.
- [systemName](systemname.md) — The name of the operating system running on the device.
- [systemVersion](systemversion.md) — The current version of the operating system.
- [localizedModel](localizedmodel.md) — The model of the device as a localized string.
- [userInterfaceIdiom](userinterfaceidiom.md) — The style of interface to use on the current device.
- [identifierForVendor](identifierforvendor.md) — An alphanumeric string that uniquely identifies a device to the app’s vendor.
