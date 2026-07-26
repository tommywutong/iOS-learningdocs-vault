---
title: 'scaledValue(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontmetrics/scaledvalue(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontmetrics/scaledvalue(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontmetrics/scaledvalue%28for%3A%29.json'
content_hash: 'sha256:ed936b9eff4c7aa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontMetrics](../uifontmetrics.md)

# scaledValue(for:)

<sub>Instance Method</sub>

Scales an arbitrary layout value based on the current Dynamic Type settings.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func scaledValue(for value: CGFloat) -> CGFloat
```

## Parameters

- `value` — The height value that you want to scale. Specify the height of the object that contains the text (at the standard Dynamic Type size) that you want to display.

## Return Value

A layout height that is scaled appropriately to accommodate the text that you want to display.

## Discussion

Use this method to scale the height of visual elements containing text. For example, if you define a button with text that can scale based on Dynamic Type, you would use this method to obtain an appropriately scaled height for your button’s background content.

## See Also

### Scaling Layout Values

- [- scaledValueForValue:compatibleWithTraitCollection:](<scaledvalue(for_compatiblewith_).md>) — Scales an arbitrary layout value based on the current Dynamic Type settings and the specified traits.
