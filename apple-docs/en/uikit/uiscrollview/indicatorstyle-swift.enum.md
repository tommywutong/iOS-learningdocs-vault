---
title: UIScrollView.IndicatorStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/indicatorstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/indicatorstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/indicatorstyle-swift.enum.json'
content_hash: 'sha256:260654a5b2af57c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# UIScrollView.IndicatorStyle

<sub>Enumeration</sub>

Defines constants that represent the styles of the scroll indicators.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum IndicatorStyle
```

## Overview

You use these constants to set the value of the [indicatorStyle](indicatorstyle-swift.property.md) style.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIScrollViewIndicatorStyleDefault](indicatorstyle-swift.enum/default.md) — The default style of scroll indicator, which is black with a white border.
- [UIScrollViewIndicatorStyleBlack](indicatorstyle-swift.enum/black.md) — A style of indicator which is black and smaller than the default style.
- [UIScrollViewIndicatorStyleWhite](indicatorstyle-swift.enum/white.md) — A style of indicator is white and smaller than the default style.

### Initializers

- [init(rawValue:)](<indicatorstyle-swift.enum/init(rawvalue_).md>)

## See Also

### Managing the scroll indicator and refresh control

- [indicatorStyle](indicatorstyle-swift.property.md) — The style of the scroll indicators.
- [showsHorizontalScrollIndicator](showshorizontalscrollindicator.md) — A Boolean value that controls whether the horizontal scroll indicator is visible.
- [showsVerticalScrollIndicator](showsverticalscrollindicator.md) — A Boolean value that controls whether the vertical scroll indicator is visible.
- [horizontalScrollIndicatorInsets](horizontalscrollindicatorinsets.md) — The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [verticalScrollIndicatorInsets](verticalscrollindicatorinsets.md) — The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [automaticallyAdjustsScrollIndicatorInsets](automaticallyadjustsscrollindicatorinsets.md) — A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [- flashScrollIndicators](<flashscrollindicators().md>) — Displays the scroll indicators momentarily.
- [- withScrollIndicatorsShownForContentOffsetChanges:](<withscrollindicatorsshown(forcontentoffsetchanges_).md>) — Displays the scroll indicators during updates to the scroll view’s content offset.
- [refreshControl](refreshcontrol.md) — The refresh control associated with the scroll view.
- [UIRefreshControl](../uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
