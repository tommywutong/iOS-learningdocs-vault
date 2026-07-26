---
title: verticalScrollIndicatorInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 13.1+, tvOS 11.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/verticalscrollindicatorinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/verticalscrollindicatorinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/verticalscrollindicatorinsets.json'
content_hash: 'sha256:fe849f9c05339ace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# verticalScrollIndicatorInsets

<sub>Instance Property</sub>

The vertical distance the scroll indicators are inset from the edge of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var verticalScrollIndicatorInsets: UIEdgeInsets { get set }
```

## Discussion

The default value is [UIEdgeInsetsZero](../uiedgeinsets/zero.md).

## See Also

### Managing the scroll indicator and refresh control

- [indicatorStyle](indicatorstyle-swift.property.md) — The style of the scroll indicators.
- [IndicatorStyle](indicatorstyle-swift.enum.md) — Defines constants that represent the styles of the scroll indicators.
- [showsHorizontalScrollIndicator](showshorizontalscrollindicator.md) — A Boolean value that controls whether the horizontal scroll indicator is visible.
- [showsVerticalScrollIndicator](showsverticalscrollindicator.md) — A Boolean value that controls whether the vertical scroll indicator is visible.
- [horizontalScrollIndicatorInsets](horizontalscrollindicatorinsets.md) — The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [automaticallyAdjustsScrollIndicatorInsets](automaticallyadjustsscrollindicatorinsets.md) — A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [- flashScrollIndicators](<flashscrollindicators().md>) — Displays the scroll indicators momentarily.
- [- withScrollIndicatorsShownForContentOffsetChanges:](<withscrollindicatorsshown(forcontentoffsetchanges_).md>) — Displays the scroll indicators during updates to the scroll view’s content offset.
- [refreshControl](refreshcontrol.md) — The refresh control associated with the scroll view.
- [UIRefreshControl](../uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
