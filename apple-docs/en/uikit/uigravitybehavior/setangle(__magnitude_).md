---
title: 'setAngle(_:magnitude:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigravitybehavior/setangle(_:magnitude:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigravitybehavior/setangle(_:magnitude:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigravitybehavior/setangle%28_%3Amagnitude%3A%29.json'
content_hash: 'sha256:e09c663e05c0dd07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGravityBehavior](../uigravitybehavior.md)

# setAngle(_:magnitude:)

<sub>Instance Method</sub>

Sets the angle and magnitude of the gravity vector for the behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setAngle(_ angle: CGFloat, magnitude: CGFloat)
```

## Parameters

- `angle` — The radian angle for the gravity vector, using standard UIKit geometry. Specify the value `pi / 2` to create a force that pulls items downward toward the bottom of the reference view.

- `magnitude` — The magnitude of the gravitational force. Specify `1.0` to get the standard UIKit gravity, which has an acceleration value of 1000 points / second².

## See Also

### Configuring a gravity behavior

- [gravityDirection](gravitydirection.md) — The direction and magnitude of the gravitational force, expressed as a vector.
- [angle](angle.md) — The direction of the gravity vector, expressed in radians in the reference coordinate system.
- [magnitude](magnitude.md) — The magnitude of the gravity vector.
