---
title: showsHorizontalScrollIndicator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/showshorizontalscrollindicator
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/showshorizontalscrollindicator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/showshorizontalscrollindicator.json'
content_hash: 'sha256:8133970b96f499b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# showsHorizontalScrollIndicator

<sub>Instance Property</sub>

A Boolean value that controls whether the horizontal scroll indicator is visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var showsHorizontalScrollIndicator: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md). The indicator is visible while tracking is underway and fades out after tracking.

## See Also

### Managing the scroll indicator and refresh control

- [indicatorStyle](indicatorstyle-swift.property.md) — The style of the scroll indicators.
- [IndicatorStyle](indicatorstyle-swift.enum.md) — Defines constants that represent the styles of the scroll indicators.
- [showsVerticalScrollIndicator](showsverticalscrollindicator.md) — A Boolean value that controls whether the vertical scroll indicator is visible.
- [horizontalScrollIndicatorInsets](horizontalscrollindicatorinsets.md) — The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [verticalScrollIndicatorInsets](verticalscrollindicatorinsets.md) — The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [automaticallyAdjustsScrollIndicatorInsets](automaticallyadjustsscrollindicatorinsets.md) — A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [- flashScrollIndicators](<flashscrollindicators().md>) — Displays the scroll indicators momentarily.
- [- withScrollIndicatorsShownForContentOffsetChanges:](<withscrollindicatorsshown(forcontentoffsetchanges_).md>) — Displays the scroll indicators during updates to the scroll view’s content offset.
- [refreshControl](refreshcontrol.md) — The refresh control associated with the scroll view.
- [UIRefreshControl](../uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
