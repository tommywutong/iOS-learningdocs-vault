---
title: UITimingCurveProvider
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitimingcurveprovider
source_url: 'https://developer.apple.com/documentation/uikit/uitimingcurveprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitimingcurveprovider.json'
content_hash: 'sha256:b6397d8ba12b8a5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITimingCurveProvider

<sub>Protocol</sub>

An interface for providing the timing information needed to perform animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITimingCurveProvider : NSCoding, NSCopying
```

## Overview

An object that adopts the [UITimingCurveProvider](uitimingcurveprovider.md) protocol provides the timing information needed to perform animations with a [UIViewPropertyAnimator](uiviewpropertyanimator.md) object. A timing curve defines the velocity at which animated properties change to their new values over the duration of the animation. A custom timing curve provider can specify timing using the built-in UIKit curves, a cubic Bézier curve, a spring-based timing function, or a combination of timing information.

When implementing this protocol in a custom object, you must provide implementations for all of the properties. Use the [timingCurveType](uitimingcurveprovider/timingcurvetype.md) property to specify which timing information your object provides. Configure the other properties with the actual timing curve values.

## Relationships

- **Inherits From**: [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md)

- **Conforming Types**: [UICubicTimingParameters](uicubictimingparameters.md), [UISpringTimingParameters](uispringtimingparameters.md)

## Topics

### Getting the timing information

- [timingCurveType](uitimingcurveprovider/timingcurvetype.md) — The type of timing information to use.
- [cubicTimingParameters](uitimingcurveprovider/cubictimingparameters.md) — The cubic timing parameters to use.
- [springTimingParameters](uitimingcurveprovider/springtimingparameters.md) — The spring-based timing parameters to use.

### Constants

- [UITimingCurveType](uitimingcurvetype.md) — Constants indicating the type of timing information to use.

## See Also

### Timing curves

- [UISpringTimingParameters](uispringtimingparameters.md) — The timing information for animations that mimics the behavior of a spring.
- [UICubicTimingParameters](uicubictimingparameters.md) — The timing information for animations in the form of a cubic Bézier curve.
