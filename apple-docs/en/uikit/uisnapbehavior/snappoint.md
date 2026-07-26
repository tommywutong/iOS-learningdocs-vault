---
title: snapPoint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisnapbehavior/snappoint
source_url: 'https://developer.apple.com/documentation/uikit/uisnapbehavior/snappoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisnapbehavior/snappoint.json'
content_hash: 'sha256:2b54f24edf89c589'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISnapBehavior](../uisnapbehavior.md)

# snapPoint

<sub>Instance Property</sub>

The point to which to snap.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var snapPoint: CGPoint { get set }
```

## Discussion

The initial value of this property is the value you passed in to the [- initWithItem:snapToPoint:](<init(item_snapto_).md>) method. Changing this value updates the dynamic item and potentially puts it in motion again.

The coordinate system of the point depends on how you initialized the underlying dynamic animator, as described in the overview of [UIDynamicAnimator](../uidynamicanimator.md).

## See Also

### Configuring a snap behavior

- [damping](damping.md) — The amount of oscillation of a dynamic item during the conclusion of a snap.
