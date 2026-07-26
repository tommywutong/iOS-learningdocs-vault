---
title: motionEffects
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimotioneffectgroup/motioneffects
source_url: 'https://developer.apple.com/documentation/uikit/uimotioneffectgroup/motioneffects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimotioneffectgroup/motioneffects.json'
content_hash: 'sha256:619d1f870f876160'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMotionEffectGroup](../uimotioneffectgroup.md)

# motionEffects

<sub>Instance Property</sub>

An array of motion effect objects to apply as a group to the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var motionEffects: [UIMotionEffect]? { get set }
```

## Discussion

The array contains one or more [UIMotionEffect](../uimotioneffect.md) objects. When the viewer offset changes, each object in the group is asked for its key paths and updated values. Those values are then applied simultaneously.
