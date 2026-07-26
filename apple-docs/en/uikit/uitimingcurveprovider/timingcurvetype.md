---
title: timingCurveType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitimingcurveprovider/timingcurvetype
source_url: 'https://developer.apple.com/documentation/uikit/uitimingcurveprovider/timingcurvetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitimingcurveprovider/timingcurvetype.json'
content_hash: 'sha256:fa71df0470ffb3ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITimingCurveProvider](../uitimingcurveprovider.md)

# timingCurveType

<sub>Instance Property</sub>

The type of timing information to use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var timingCurveType: UITimingCurveType { get }
```

## Discussion

Use this property to specify the type of timing information your timing curve object supplies. The value of this property determines whether the view property animator uses the object in the [cubicTimingParameters](cubictimingparameters.md) or [springTimingParameters](springtimingparameters.md) property for timing information.

## See Also

### Getting the timing information

- [cubicTimingParameters](cubictimingparameters.md) — The cubic timing parameters to use.
- [springTimingParameters](springtimingparameters.md) — The spring-based timing parameters to use.
