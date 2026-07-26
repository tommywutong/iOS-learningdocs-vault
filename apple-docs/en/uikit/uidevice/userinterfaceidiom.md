---
title: userInterfaceIdiom
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/userinterfaceidiom
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/userinterfaceidiom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/userinterfaceidiom.json'
content_hash: 'sha256:b05928b347b39645'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# userInterfaceIdiom

<sub>Instance Property</sub>

The style of interface to use on the current device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var userInterfaceIdiom: UIUserInterfaceIdiom { get }
```

## Discussion

For universal applications, you can use this property to tailor the behavior of your application for a specific type of device. For example, iPhone and iPad devices have different screen sizes, so you might want to create different views and controls based on the type of the current device.

## See Also

### Identifying the device and operating system

- [name](name.md) — The name of the device.
- [systemName](systemname.md) — The name of the operating system running on the device.
- [systemVersion](systemversion.md) — The current version of the operating system.
- [model](model.md) — The model of the device.
- [localizedModel](localizedmodel.md) — The model of the device as a localized string.
- [identifierForVendor](identifierforvendor.md) — An alphanumeric string that uniquely identifies a device to the app’s vendor.
