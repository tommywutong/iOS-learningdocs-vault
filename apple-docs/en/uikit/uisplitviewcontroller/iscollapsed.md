---
title: isCollapsed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/iscollapsed
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/iscollapsed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/iscollapsed.json'
content_hash: 'sha256:c9e1630f16d7289f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# isCollapsed

<sub>Instance Property</sub>

A Boolean value that indicates whether only one of the child view controllers displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isCollapsed: Bool { get }
```

## Discussion

This property is set to [true](../../swift/true.md) when the split view controller content is semantically collapsed into a single container. Collapsing happens when the split view controller transitions from a horizontally regular to a horizontally compact environment. After it has been collapsed, the split view controller reports having only one child view controller in its [viewControllers](viewcontrollers.md) property. When collapsed, the [displayMode](displaymode-swift.property.md) property has no impact on the appearance of the split view interface.

In a column-style split view interface, if this property is [true](../../swift/true.md) and the split view controller has a view controller set for its [UISplitViewControllerColumnCompact](column/compact.md) column, the interface displays that view controller.

The value of this property is [false](../../swift/false.md) when the split view controller is capable of displaying more than one of its child view controllers at the same time, even if it’s not showing more than one at the moment. In this expanded mode, the split view controller’s configuration of its child view controllers is determined by the [displayMode](displaymode-swift.property.md) property.

During a transition from an expanded to a collapsed interface, the value of this property is [false](../../swift/false.md) until after the collapse transition finishes and all of the relevant delegate methods have been called. Similarly, when transitioning back to an expanded interface, the value is [true](../../swift/true.md) until the transition finishes.

## See Also

### Managing column dimensions

- [preferredPrimaryColumnWidthFraction](preferredprimarycolumnwidthfraction.md) — The relative width of the primary view controller’s content.
- [preferredPrimaryColumnWidth](preferredprimarycolumnwidth.md) — The preferred width, in points, of the primary view controller’s content.
- [primaryColumnWidth](primarycolumnwidth.md) — The width, in points, of the primary view controller’s content.
- [minimumPrimaryColumnWidth](minimumprimarycolumnwidth.md) — The minimum width, in points, for the primary view controller’s content.
- [maximumPrimaryColumnWidth](maximumprimarycolumnwidth.md) — The maximum width, in points, for the primary view controller’s content.
- [preferredSupplementaryColumnWidthFraction](preferredsupplementarycolumnwidthfraction.md) — The relative width of the supplementary view controller’s content.
- [preferredSupplementaryColumnWidth](preferredsupplementarycolumnwidth.md) — The preferred width, in points, of the supplementary view controller’s content.
- [supplementaryColumnWidth](supplementarycolumnwidth.md) — The width, in points, of the supplementary view controller’s content.
- [minimumSupplementaryColumnWidth](minimumsupplementarycolumnwidth.md) — The minimum width, in points, for the supplementary view controller’s content.
- [maximumSupplementaryColumnWidth](maximumsupplementarycolumnwidth.md) — The maximum width, in points, for the supplementary view controller’s content.
- [preferredSecondaryColumnWidth](preferredsecondarycolumnwidth.md) — The preferred width, in points, for the secondary view controller’s content.
- [preferredSecondaryColumnWidthFraction](preferredsecondarycolumnwidthfraction.md) — The relative width of the secondary view controller’s content.
- [minimumSecondaryColumnWidth](minimumsecondarycolumnwidth.md) — The minimum width, in points, for the secondary view controller’s content.
- [preferredInspectorColumnWidth](preferredinspectorcolumnwidth.md) — The preferred width, in points, for the inspector view controller’s content.
- [preferredInspectorColumnWidthFraction](preferredinspectorcolumnwidthfraction.md) — The relative width of the inspector view controller’s content.
