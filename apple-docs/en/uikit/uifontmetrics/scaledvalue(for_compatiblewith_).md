---
title: 'scaledValue(for:compatibleWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontmetrics/scaledvalue(for:compatiblewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontmetrics/scaledvalue(for:compatiblewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontmetrics/scaledvalue%28for%3Acompatiblewith%3A%29.json'
content_hash: 'sha256:dbb0b4c3b2100957'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontMetrics](../uifontmetrics.md)

# scaledValue(for:compatibleWith:)

<sub>Instance Method</sub>

Scales an arbitrary layout value based on the current Dynamic Type settings and the specified traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func scaledValue(for value: CGFloat, compatibleWith traitCollection: UITraitCollection?) -> CGFloat
```

## Parameters

- `value` — The height value that you want to scale. Specify the height of the object that contains the text (at the standard Dynamic Type size) that you want to display.

- `traitCollection` — The trait collection to use when determining compatibility. The returned value is appropriate for use in an interface that adopts the specified traits.

## Return Value

A layout height that is scaled appropriately to accommodate the text that you want to display.

## Discussion

Use this method to scale the height of visual elements containing text. For example, if you define a button with text that can scale based on Dynamic Type, you would use this method to obtain an appropriately scaled height for your button’s background content.

## See Also

### Scaling Layout Values

- [- scaledValueForValue:](<scaledvalue(for_).md>) — Scales an arbitrary layout value based on the current Dynamic Type settings.
