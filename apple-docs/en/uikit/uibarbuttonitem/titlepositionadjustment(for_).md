---
title: 'titlePositionAdjustment(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/titlepositionadjustment(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/titlepositionadjustment(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/titlepositionadjustment%28for%3A%29.json'
content_hash: 'sha256:64ac280aac131a33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# titlePositionAdjustment(for:)

<sub>Instance Method</sub>

Returns the title offset for specified bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func titlePositionAdjustment(for barMetrics: UIBarMetrics) -> UIOffset
```

## Parameters

- `barMetrics` — Bar metrics.

## Return Value

The title offset for `barMetrics`.

## Discussion

This offset is used to adjust the position of a title (if any) within a bordered bar button.

## See Also

### Customizing the title placement

- [- setTitlePositionAdjustment:forBarMetrics:](<settitlepositionadjustment(__for_).md>) — Sets the title offset for specified bar metrics.
