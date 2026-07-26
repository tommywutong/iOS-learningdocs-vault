---
title: minimumPrimaryColumnWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/minimumprimarycolumnwidth
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/minimumprimarycolumnwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/minimumprimarycolumnwidth.json'
content_hash: 'sha256:6b2abf376f505bc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# minimumPrimaryColumnWidth

<sub>Instance Property</sub>

The minimum width, in points, for the primary view controller’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumPrimaryColumnWidth: CGFloat { get set }
```

## Discussion

Use this property in conjunction with the [maximumPrimaryColumnWidth](maximumprimarycolumnwidth.md) property to ensure the width of the primary view controller’s content is set to an acceptable value. The preliminary width is specified by the [preferredPrimaryColumnWidthFraction](preferredprimarycolumnwidthfraction.md) property, which is applied to the split view controller’s width and checked against these bounds. If the resulting width is less than the minimum value specified by this property, the width is set to the value in this property.

The default value of this property is [UISplitViewControllerAutomaticDimension](automaticdimension.md), which corresponds to a minimum width of 0 points.

## See Also

### Managing column dimensions

- [collapsed](iscollapsed.md) — A Boolean value that indicates whether only one of the child view controllers displays.
- [preferredPrimaryColumnWidthFraction](preferredprimarycolumnwidthfraction.md) — The relative width of the primary view controller’s content.
- [preferredPrimaryColumnWidth](preferredprimarycolumnwidth.md) — The preferred width, in points, of the primary view controller’s content.
- [primaryColumnWidth](primarycolumnwidth.md) — The width, in points, of the primary view controller’s content.
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
