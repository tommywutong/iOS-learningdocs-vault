---
title: mode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipushbehavior/mode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/mode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/mode-swift.property.json'
content_hash: 'sha256:2e8043cfbecd79d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# mode

<sub>Instance Property</sub>

Returns the force mode for the push behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var mode: UIPushBehavior.Mode { get }
```

## Discussion

The mode is one of the values available in the [Mode](mode-swift.enum.md) enumeration. Set the mode when you call the [- initWithItems:mode:](<init(items_mode_).md>) method.

## See Also

### Configuring a push behavior

- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the force vector for the behavior.
- [angle](angle.md) — The angle, in radians, of the force vector for the behavior.
- [magnitude](magnitude.md) — The magnitude of the force vector for the push behavior.
- [- setTargetOffsetFromCenter:forItem:](<settargetoffsetfromcenter(__for_).md>) — Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [- targetOffsetFromCenterForItem:](<targetoffsetfromcenter(for_).md>) — Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [pushDirection](pushdirection.md) — The direction of the force vector for the behavior, expressed as _x_ and _y_ components and using standard UIKit geometry.
