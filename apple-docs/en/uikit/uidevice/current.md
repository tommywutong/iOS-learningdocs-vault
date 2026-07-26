---
title: current
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/current
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/current.json'
content_hash: 'sha256:3176631655055d02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# current

<sub>Type Property</sub>

An object that represents the current device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var current: UIDevice { get }
```

## Return Value

A singleton object that represents the current device.

## Discussion

You access the properties of the returned [UIDevice](../uidevice.md) instance to obtain information about the device. You must instantiate the [UIDevice](../uidevice.md) instance before registering to receive device notifications.
