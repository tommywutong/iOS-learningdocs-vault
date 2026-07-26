---
title: scrollIndicatorInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscrollview/scrollindicatorinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/scrollindicatorinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/scrollindicatorinsets.json'
content_hash: 'sha256:6c69f0ecd439a735'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# scrollIndicatorInsets

<sub>Instance Property</sub>

The distance the scroll indicators are inset from the edge of the scroll view.

> [!warning] Deprecated
> Use [horizontalScrollIndicatorInsets](horizontalscrollindicatorinsets.md) and [verticalScrollIndicatorInsets](verticalscrollindicatorinsets.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var scrollIndicatorInsets: UIEdgeInsets { get set }
```

## Discussion

The default value is [UIEdgeInsetsZero](../uiedgeinsets/zero.md).
