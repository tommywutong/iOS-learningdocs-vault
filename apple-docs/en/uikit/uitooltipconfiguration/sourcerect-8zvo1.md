---
title: sourceRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitooltipconfiguration/sourcerect-8zvo1
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipconfiguration/sourcerect-8zvo1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipconfiguration/sourcerect-8zvo1.json'
content_hash: 'sha256:eb8b94b32a6e0893'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipConfiguration](../uitooltipconfiguration.md)

# sourceRect

<sub>Instance Property</sub>

The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency var sourceRect: CGRect? { get }
```

## Discussion

To set [sourceRect](../uiviewcontrollerpreviewing/sourcerect.md), create a tooltip configuration object using the [+ configurationWithToolTip:inRect:](<init(tooltip_in_).md>) method.

## See Also

### Accessing the configuration settings

- [toolTip](tooltip.md) — The text to display in the tooltip.
