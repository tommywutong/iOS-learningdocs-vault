---
title: handoffUserActivityType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/handoffuseractivitytype
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/handoffuseractivitytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/handoffuseractivitytype.json'
content_hash: 'sha256:4f50a503185ed2a9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# handoffUserActivityType

<sub>Instance Property</sub>

The type of the pending Handoff activity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var handoffUserActivityType: String? { get }
```

## Discussion

When a Handoff activity is pending at scene-connection time, UIKit puts the type of that activity in this property. Use this information at connection time to prepare your scene to receive the actual activity object. After your scene connects, UIKit calls the appropriate delegate methods to deliver the [NSUserActivity](../../../foundation/nsuseractivity.md) object.

If the value of this property is `nil`, no Handoff activity is pending.
