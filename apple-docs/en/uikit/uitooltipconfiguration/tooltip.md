---
title: toolTip
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitooltipconfiguration/tooltip
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipconfiguration/tooltip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipconfiguration/tooltip.json'
content_hash: 'sha256:2a61b633419210ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipConfiguration](../uitooltipconfiguration.md)

# toolTip

<sub>Instance Property</sub>

The text to display in the tooltip.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var toolTip: String { get }
```

## Discussion

To set the tooltip text, create a tooltip configuration object using either the [+ configurationWithToolTip:](<init(tooltip_).md>) or [+ configurationWithToolTip:inRect:](<init(tooltip_in_).md>) methods.

## See Also

### Accessing the configuration settings

- [sourceRect](sourcerect-8zvo1.md) — The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.
