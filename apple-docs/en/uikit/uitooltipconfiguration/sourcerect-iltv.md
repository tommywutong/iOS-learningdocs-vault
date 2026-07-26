---
title: sourceRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitooltipconfiguration/sourcerect-iltv
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipconfiguration/sourcerect-iltv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipconfiguration/sourcerect-iltv.json'
content_hash: 'sha256:7d0f4b692a98aeba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipConfiguration](../uitooltipconfiguration.md)

# sourceRect

<sub>Instance Property</sub>

The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) CGRect sourceRect;
```

## Discussion

To set [sourceRect](sourcerect-iltv.md), create a tooltip configuration object using the [+ configurationWithToolTip:inRect:](<init(tooltip_in_).md>) method.

## See Also

### Accessing the configuration settings

- [toolTip](tooltip.md) — The text to display in the tooltip.
