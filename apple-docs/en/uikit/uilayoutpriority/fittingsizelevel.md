---
title: fittingSizeLevel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutpriority/fittingsizelevel
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutpriority/fittingsizelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutpriority/fittingsizelevel.json'
content_hash: 'sha256:621445005baab629'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutPriority](../uilayoutpriority.md)

# fittingSizeLevel

<sub>Type Property</sub>

The priority level with which the view wants to conform to the target size in that computation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var fittingSizeLevel: UILayoutPriority { get }
```

## Discussion

When you send a [- systemLayoutSizeFittingSize:](<../uiview/systemlayoutsizefitting(__).md>) message to a view, the size fitting most closely to the target size is computed. This priority is quite low. It’s generally not appropriate to make a constraint at exactly this priority. You want to be higher or lower.

## See Also

### Constants

- [UILayoutPriorityRequired](required.md) — A required constraint.
- [UILayoutPriorityDefaultHigh](defaulthigh.md) — The priority level with which a button resists compressing its content.
- [UILayoutPriorityDragThatCanResizeScene](dragthatcanresizescene.md) — The priority level for a drag that may end up resizing the window’s scene.
- [UILayoutPrioritySceneSizeStayPut](scenesizestayput.md) — The priority level at which the window’s scene prefers to stay the same size.
- [UILayoutPriorityDragThatCannotResizeScene](dragthatcannotresizescene.md) — The priority level for a drag that won’t resize the window’s scene.
- [UILayoutPriorityDefaultLow](defaultlow.md) — The priority level at which a button hugs its contents horizontally.
