---
title: localizedModel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/localizedmodel
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/localizedmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/localizedmodel.json'
content_hash: 'sha256:8de46324ba2b1088'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# localizedModel

<sub>Instance Property</sub>

The model of the device as a localized string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var localizedModel: String { get }
```

## Discussion

The value of this property is a string that contains a localized version of the string returned from [model](model.md).

## See Also

### Identifying the device and operating system

- [name](name.md) — The name of the device.
- [systemName](systemname.md) — The name of the operating system running on the device.
- [systemVersion](systemversion.md) — The current version of the operating system.
- [model](model.md) — The model of the device.
- [userInterfaceIdiom](userinterfaceidiom.md) — The style of interface to use on the current device.
- [identifierForVendor](identifierforvendor.md) — An alphanumeric string that uniquely identifies a device to the app’s vendor.
