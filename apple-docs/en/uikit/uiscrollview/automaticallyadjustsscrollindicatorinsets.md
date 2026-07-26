---
title: automaticallyAdjustsScrollIndicatorInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/automaticallyadjustsscrollindicatorinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/automaticallyadjustsscrollindicatorinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/automaticallyadjustsscrollindicatorinsets.json'
content_hash: 'sha256:2458b3de7a26c282'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# automaticallyAdjustsScrollIndicatorInsets

<sub>Instance Property</sub>

A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyAdjustsScrollIndicatorInsets: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md).

## See Also

### Managing the scroll indicator and refresh control

- [indicatorStyle](indicatorstyle-swift.property.md) — The style of the scroll indicators.
- [IndicatorStyle](indicatorstyle-swift.enum.md) — Defines constants that represent the styles of the scroll indicators.
- [showsHorizontalScrollIndicator](showshorizontalscrollindicator.md) — A Boolean value that controls whether the horizontal scroll indicator is visible.
- [showsVerticalScrollIndicator](showsverticalscrollindicator.md) — A Boolean value that controls whether the vertical scroll indicator is visible.
- [horizontalScrollIndicatorInsets](horizontalscrollindicatorinsets.md) — The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [verticalScrollIndicatorInsets](verticalscrollindicatorinsets.md) — The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [- flashScrollIndicators](<flashscrollindicators().md>) — Displays the scroll indicators momentarily.
- [- withScrollIndicatorsShownForContentOffsetChanges:](<withscrollindicatorsshown(forcontentoffsetchanges_).md>) — Displays the scroll indicators during updates to the scroll view’s content offset.
- [refreshControl](refreshcontrol.md) — The refresh control associated with the scroll view.
- [UIRefreshControl](../uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
