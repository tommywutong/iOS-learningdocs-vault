---
title: 'targetOffsetFromCenter(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipushbehavior/targetoffsetfromcenter(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/targetoffsetfromcenter(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/targetoffsetfromcenter%28for%3A%29.json'
content_hash: 'sha256:772f76d4f7ce9e3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# targetOffsetFromCenter(for:)

<sub>Instance Method</sub>

Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func targetOffsetFromCenter(for item: any UIDynamicItem) -> UIOffset
```

## Parameters

- `item` — The dynamic item for which you’re retrieving the target offset.

## Return Value

The offset, from the center of the dynamic item, at which the push behavior’s force vector is applied. If you haven’t set a target offset, returns the center of the dynamic item.

## See Also

### Configuring a push behavior

- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the force vector for the behavior.
- [angle](angle.md) — The angle, in radians, of the force vector for the behavior.
- [magnitude](magnitude.md) — The magnitude of the force vector for the push behavior.
- [mode](mode-swift.property.md) — Returns the force mode for the push behavior.
- [- setTargetOffsetFromCenter:forItem:](<settargetoffsetfromcenter(__for_).md>) — Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [pushDirection](pushdirection.md) — The direction of the force vector for the behavior, expressed as _x_ and _y_ components and using standard UIKit geometry.
