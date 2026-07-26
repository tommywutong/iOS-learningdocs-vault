---
title: UIScrollView.ContentInsetAdjustmentBehavior.scrollableAxes
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/scrollableaxes
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/scrollableaxes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/scrollableaxes.json'
content_hash: 'sha256:0f64d056a59e82b3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScrollView](../../uiscrollview.md) · [ContentInsetAdjustmentBehavior](../contentinsetadjustmentbehavior-swift.enum.md)

# UIScrollView.ContentInsetAdjustmentBehavior.scrollableAxes

<sub>Case</sub>

Adjust the insets only in the scrollable directions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case scrollableAxes
```

## Discussion

The top and bottom insets include the safe area inset values when the vertical content size is greater than the height of the scroll view itself. The top and bottom insets are also adjusted when the [alwaysBounceVertical](../alwaysbouncevertical.md) property is [true](../../../swift/true.md). Similarly, the left and right insets include the safe area insets when the horizontal content size is greater than the width of the scroll view.
