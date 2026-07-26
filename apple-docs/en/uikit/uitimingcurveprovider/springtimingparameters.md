---
title: springTimingParameters
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitimingcurveprovider/springtimingparameters
source_url: 'https://developer.apple.com/documentation/uikit/uitimingcurveprovider/springtimingparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitimingcurveprovider/springtimingparameters.json'
content_hash: 'sha256:3584a0c1a7fcd732'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITimingCurveProvider](../uitimingcurveprovider.md)

# springTimingParameters

<sub>Instance Property</sub>

The spring-based timing parameters to use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var springTimingParameters: UISpringTimingParameters? { get }
```

## Discussion

Implement this property and use it to provide spring-based timing information. If the value of the [timingCurveType](timingcurvetype.md) property is [UITimingCurveTypeSpring](../uitimingcurvetype/spring.md) or [UITimingCurveTypeComposed](../uitimingcurvetype/composed.md), you must return an object from this property.

For more information about configuring spring-based timing parameters, see [UISpringTimingParameters](../uispringtimingparameters.md).

## See Also

### Getting the timing information

- [timingCurveType](timingcurvetype.md) — The type of timing information to use.
- [cubicTimingParameters](cubictimingparameters.md) — The cubic timing parameters to use.
