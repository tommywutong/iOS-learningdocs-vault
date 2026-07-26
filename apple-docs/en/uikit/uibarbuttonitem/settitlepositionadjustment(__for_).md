---
title: 'setTitlePositionAdjustment(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/settitlepositionadjustment(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/settitlepositionadjustment(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/settitlepositionadjustment%28_%3Afor%3A%29.json'
content_hash: 'sha256:924f35e057d47b6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# setTitlePositionAdjustment(_:for:)

<sub>Instance Method</sub>

Sets the title offset for specified bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTitlePositionAdjustment(_ adjustment: UIOffset, for barMetrics: UIBarMetrics)
```

## Parameters

- `adjustment` — The title offset for `barMetrics`.

- `barMetrics` — Bar metrics.

## Discussion

This offset is used to adjust the position of a title (if any) within a bordered bar button.

## See Also

### Customizing the title placement

- [- titlePositionAdjustmentForBarMetrics:](<titlepositionadjustment(for_).md>) — Returns the title offset for specified bar metrics.
