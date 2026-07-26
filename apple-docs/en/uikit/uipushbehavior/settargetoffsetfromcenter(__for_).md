---
title: 'setTargetOffsetFromCenter(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipushbehavior/settargetoffsetfromcenter(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/settargetoffsetfromcenter(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/settargetoffsetfromcenter%28_%3Afor%3A%29.json'
content_hash: 'sha256:72f492daa0715b44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# setTargetOffsetFromCenter(_:for:)

<sub>Instance Method</sub>

Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTargetOffsetFromCenter(_ o: UIOffset, for item: any UIDynamicItem)
```

## Parameters

- `o` — The offset, from the center of the dynamic item, at which to apply the push behavior’s force vector.

- `item` — The dynamic item for which you’re setting a target offset.

## Discussion

If you don’t set a target offset for a dynamic item, a push behavior’s force vector is applied at the item center.

## See Also

### Configuring a push behavior

- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the force vector for the behavior.
- [angle](angle.md) — The angle, in radians, of the force vector for the behavior.
- [magnitude](magnitude.md) — The magnitude of the force vector for the push behavior.
- [mode](mode-swift.property.md) — Returns the force mode for the push behavior.
- [- targetOffsetFromCenterForItem:](<targetoffsetfromcenter(for_).md>) — Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [pushDirection](pushdirection.md) — The direction of the force vector for the behavior, expressed as _x_ and _y_ components and using standard UIKit geometry.
