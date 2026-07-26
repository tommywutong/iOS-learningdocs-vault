---
title: preferredPrimaryColumnWidthFraction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/preferredprimarycolumnwidthfraction
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferredprimarycolumnwidthfraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/preferredprimarycolumnwidthfraction.json'
content_hash: 'sha256:be7a5efe3cdb7729'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# preferredPrimaryColumnWidthFraction

<sub>Instance Property</sub>

The relative width of the primary view controller’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredPrimaryColumnWidthFraction: CGFloat { get set }
```

## Discussion

Use this property to specify your preferred width for the primary view controller’s view. The value of this property is a floating-point number between `0.0` and `1.0` that represents the percentage of the overall width of the split view controller. For example, the value `0.4` represents 40% of the current width. The default value of this property is [UISplitViewControllerAutomaticDimension](automaticdimension.md), which results in an appropriate width for the primary view controller.

The values in the [minimumPrimaryColumnWidth](minimumprimarycolumnwidth.md) and [maximumPrimaryColumnWidth](maximumprimarycolumnwidth.md) properties constrain the actual width of the primary view controller. The split view controller attempts to use the width you specify, but may change this value to accommodate the available space. You can get the actual width for the primary view controller’s view from the [primaryColumnWidth](primarycolumnwidth.md) property.

## See Also

### Managing column dimensions

- [collapsed](iscollapsed.md) — A Boolean value that indicates whether only one of the child view controllers displays.
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
