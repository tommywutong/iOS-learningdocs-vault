---
title: forceTouchCapability
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/forcetouchcapability
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/forcetouchcapability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/forcetouchcapability.json'
content_hash: 'sha256:398ee7952148d1d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# forceTouchCapability

<sub>Instance Property</sub>

The force touch capability value of the trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var forceTouchCapability: UIForceTouchCapability { get }
```

## Discussion

3D Touch is available only on certain devices. On those devices, availability is determined by the user’s associated accessibility setting in the Settings app. Check this property’s value on app launch, and in your implementation of the [- traitCollectionDidChange:](<../uitraitenvironment/traitcollectiondidchange(__).md>) method.

If this property does not contain a value, the meaning is equivalent to the value [UIForceTouchCapabilityUnknown](../uiforcetouchcapability/unknown.md).

## See Also

### Retrieving the force touch capability traits

- [UIForceTouchCapability](../uiforcetouchcapability.md) — Keys that indicate the availability of 3D Touch on a device.
