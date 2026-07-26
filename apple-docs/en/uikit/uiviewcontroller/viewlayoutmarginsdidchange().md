---
title: viewLayoutMarginsDidChange()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/viewlayoutmarginsdidchange()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewlayoutmarginsdidchange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewlayoutmarginsdidchange%28%29.json'
content_hash: 'sha256:e7ff49c00de037de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# viewLayoutMarginsDidChange()

<sub>Instance Method</sub>

Called to notify the view controller that the layout margins of its root view changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewLayoutMarginsDidChange()
```

## Discussion

Use this method to update the position of content based on the new margin values.

## See Also

### Managing the view’s margins

- [Positioning content within layout margins](../positioning-content-within-layout-margins.md) — Position views so that they aren’t crowded by other content.
- [viewRespectsSystemMinimumLayoutMargins](viewrespectssystemminimumlayoutmargins.md) — A Boolean value indicating whether the view controller’s view uses the system-defined minimum layout margins.
- [systemMinimumLayoutMargins](systemminimumlayoutmargins.md) — The minimum layout margins for the view controller’s root view.
