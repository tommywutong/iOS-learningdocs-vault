---
title: 'removeMotionEffect(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/removemotioneffect(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/removemotioneffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/removemotioneffect%28_%3A%29.json'
content_hash: 'sha256:5f018b6a2ee361ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# removeMotionEffect(_:)

<sub>Instance Method</sub>

Stops applying a motion effect to the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeMotionEffect(_ effect: UIMotionEffect)
```

## Parameters

- `effect` — The motion effect.

## Discussion

Any affected presentation values animate to their post-removal values using the present [UIView](../uiview.md) animation context.

## See Also

### Using motion effects

- [- addMotionEffect:](<addmotioneffect(__).md>) — Begins applying a motion effect to the view.
- [motionEffects](motioneffects.md) — The array of motion effects for the view.
