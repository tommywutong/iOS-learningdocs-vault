---
title: 'position(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarpositioningdelegate/position(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarpositioningdelegate/position(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarpositioningdelegate/position%28for%3A%29.json'
content_hash: 'sha256:39087993f4c48784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarPositioningDelegate](../uibarpositioningdelegate.md)

# position(for:)

<sub>Instance Method</sub>

Asks the delegate for the position of the specified bar in its new window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func position(for bar: any UIBarPositioning) -> UIBarPosition
```

## Parameters

- `bar` — The bar that was added to the window.

## Return Value

The position of the bar.

## Discussion

If your interface has a custom bar with a delegate, that delegate can implement this method and use it to specify the position of the bar that has been added to a window.

Delegates for the [UINavigationBar](../uinavigationbar.md) and [UISearchBar](../uisearchbar.md) classes return the value [UIBarPositionTop](../uibarposition/top.md) by default. The delegate of the [UIToolbar](../uitoolbar.md) class returns the value [UIBarPositionBottom](../uibarposition/bottom.md) by default.

## See Also

### Related Documentation

- [UIBarPositioning](../uibarpositioning.md) — A set of methods for defining the positioning of bars in iOS apps.
