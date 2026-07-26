---
title: UIScrollView.ContentInsetAdjustmentBehavior.automatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/automatic
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/automatic.json'
content_hash: 'sha256:73d46eb1dfef3a2e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScrollView](../../uiscrollview.md) · [ContentInsetAdjustmentBehavior](../contentinsetadjustmentbehavior-swift.enum.md)

# UIScrollView.ContentInsetAdjustmentBehavior.automatic

<sub>Case</sub>

Automatically adjust the scroll view insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

Content is always adjusted vertically when the scroll view is the content view of a view controller that is currently displayed by a navigation or tab bar controller. If the scroll view is horizontally scrollable, the horizontal content offset is also adjusted when there are nonzero safe area insets.
