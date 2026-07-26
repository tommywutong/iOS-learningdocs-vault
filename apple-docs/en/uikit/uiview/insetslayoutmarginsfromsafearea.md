---
title: insetsLayoutMarginsFromSafeArea
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/insetslayoutmarginsfromsafearea
source_url: 'https://developer.apple.com/documentation/uikit/uiview/insetslayoutmarginsfromsafearea'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/insetslayoutmarginsfromsafearea.json'
content_hash: 'sha256:1c10e696198b8e53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# insetsLayoutMarginsFromSafeArea

<sub>Instance Property</sub>

A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var insetsLayoutMarginsFromSafeArea: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), any margins that are outside the safe area are automatically modified to fall within the safe area boundary. The default value of this property is [true](../../swift/true.md). Changing the value to [false](../../swift/false.md) allows your margins to remain at their original locations, even when they are outside the safe area.

## See Also

### Getting the safe area

- [Positioning content relative to the safe area](../positioning-content-relative-to-the-safe-area.md) — Position views so that they aren’t obstructed by other content.
- [safeAreaInsets](safeareainsets.md) — The insets that you use to determine the safe area for this view.
- [safeAreaLayoutGuide](safearealayoutguide.md) — The layout guide representing the portion of your view that is unobscured by bars and other content.
- [- safeAreaInsetsDidChange](<safeareainsetsdidchange().md>) — Called when the safe area of the view changes.
