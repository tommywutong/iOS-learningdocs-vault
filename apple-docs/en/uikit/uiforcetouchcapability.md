---
title: UIForceTouchCapability
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiforcetouchcapability
source_url: 'https://developer.apple.com/documentation/uikit/uiforcetouchcapability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiforcetouchcapability.json'
content_hash: 'sha256:dbde444a250f5075'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIForceTouchCapability

<sub>Enumeration</sub>

Keys that indicate the availability of 3D Touch on a device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIForceTouchCapability
```

## Overview

Only certain devices support 3D Touch. On those that do, the user can disable 3D Touch in the Accessibility area in Settings.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Availability options

- [UIForceTouchCapabilityUnknown](uiforcetouchcapability/unknown.md) — The availability of 3D Touch is unknown.
- [UIForceTouchCapabilityAvailable](uiforcetouchcapability/available.md) — 3D Touch is available on the device.
- [UIForceTouchCapabilityUnavailable](uiforcetouchcapability/unavailable.md) — 3D Touch isn’t available on the device.

### Initializers

- [init(rawValue:)](<uiforcetouchcapability/init(rawvalue_).md>)

## See Also

### Retrieving the force touch capability traits

- [forceTouchCapability](uitraitcollection/forcetouchcapability.md) — The force touch capability value of the trait collection.
