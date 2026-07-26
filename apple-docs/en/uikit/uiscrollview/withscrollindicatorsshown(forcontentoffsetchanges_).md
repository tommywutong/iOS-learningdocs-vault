---
title: 'withScrollIndicatorsShown(forContentOffsetChanges:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollview/withscrollindicatorsshown(forcontentoffsetchanges:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/withscrollindicatorsshown(forcontentoffsetchanges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/withscrollindicatorsshown%28forcontentoffsetchanges%3A%29.json'
content_hash: 'sha256:7afd7205046d1218'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# withScrollIndicatorsShown(forContentOffsetChanges:)

<sub>Instance Method</sub>

Displays the scroll indicators during updates to the scroll view’s content offset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func withScrollIndicatorsShown(forContentOffsetChanges changes: () -> Void)
```

## Parameters

- `changes` — A block that changes the scroll view’s content offset.

## Discussion

The scroll view displays the scroll indicator for an axis if the content offset changes along that axis; otherwise, the scroll indicator for that axis remains hidden. For example, if you update the content offset horizontally in the `changes` block, the scroll view shows the horizontal scroll indicator but not the vertical scroll indicator.

If you animate changes to the content offset in the `changes` block, the scroll view displays its scroll indicators in their original locations, animates them to the destination locations, then fades them out. Otherwise, the scroll view displays its scroll indicators in the destination locations, then fades them out.

## See Also

### Managing the scroll indicator and refresh control

- [indicatorStyle](indicatorstyle-swift.property.md) — The style of the scroll indicators.
- [IndicatorStyle](indicatorstyle-swift.enum.md) — Defines constants that represent the styles of the scroll indicators.
- [showsHorizontalScrollIndicator](showshorizontalscrollindicator.md) — A Boolean value that controls whether the horizontal scroll indicator is visible.
- [showsVerticalScrollIndicator](showsverticalscrollindicator.md) — A Boolean value that controls whether the vertical scroll indicator is visible.
- [horizontalScrollIndicatorInsets](horizontalscrollindicatorinsets.md) — The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [verticalScrollIndicatorInsets](verticalscrollindicatorinsets.md) — The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [automaticallyAdjustsScrollIndicatorInsets](automaticallyadjustsscrollindicatorinsets.md) — A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [- flashScrollIndicators](<flashscrollindicators().md>) — Displays the scroll indicators momentarily.
- [refreshControl](refreshcontrol.md) — The refresh control associated with the scroll view.
- [UIRefreshControl](../uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
