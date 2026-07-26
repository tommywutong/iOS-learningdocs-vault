---
title: 'addMotionEffect(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/addmotioneffect(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/addmotioneffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/addmotioneffect%28_%3A%29.json'
content_hash: 'sha256:c067301d7ff76a14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# addMotionEffect(_:)

<sub>Instance Method</sub>

Begins applying a motion effect to the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addMotionEffect(_ effect: UIMotionEffect)
```

## Parameters

- `effect` — The motion effect.

## Discussion

The system animates the transition to the motion effect’s values using the present [UIView](../uiview.md) animation context. The motion effect’s keyPath/value pairs are applied to the view’s presentation layer.

## See Also

### Using motion effects

- [motionEffects](motioneffects.md) — The array of motion effects for the view.
- [- removeMotionEffect:](<removemotioneffect(__).md>) — Stops applying a motion effect to the view.
