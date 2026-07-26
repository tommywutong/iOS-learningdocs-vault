---
title: additionalSafeAreaInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/additionalsafeareainsets
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/additionalsafeareainsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/additionalsafeareainsets.json'
content_hash: 'sha256:37b31f6eac8b8e33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# additionalSafeAreaInsets

<sub>Instance Property</sub>

Custom insets that you specify to modify the view controller’s safe area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var additionalSafeAreaInsets: UIEdgeInsets { get set }
```

## Discussion

Use this property to adjust the safe area insets of this view controller’s views by the specified amount. The safe area defines the portion of your view controller’s visible area that is guaranteed to be unobscured by the system status bar or by an ancestor-provided view such as the navigation bar.

You might use this property to extend the safe area to include custom content in your interface. For example, a drawing app might use this property to avoid displaying content underneath tool palettes.

## See Also

### Extending the view’s safe area

- [Positioning content relative to the safe area](../positioning-content-relative-to-the-safe-area.md) — Position views so that they aren’t obstructed by other content.
- [- viewSafeAreaInsetsDidChange](<viewsafeareainsetsdidchange().md>) — Called to notify the view controller that the safe area insets of its root view changed.
