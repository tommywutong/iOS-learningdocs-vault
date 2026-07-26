---
title: viewSafeAreaInsetsDidChange()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/viewsafeareainsetsdidchange()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewsafeareainsetsdidchange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewsafeareainsetsdidchange%28%29.json'
content_hash: 'sha256:48db6028cc876713'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# viewSafeAreaInsetsDidChange()

<sub>Instance Method</sub>

Called to notify the view controller that the safe area insets of its root view changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewSafeAreaInsetsDidChange()
```

## Discussion

Use this method to update your interface to accommodate the new safe area. UIKit updates the safe area in response to size changes to system bars or when you modify the additional safe area insets of your view controller. UIKit also calls this method immediately before your view appears onscreen.

## See Also

### Extending the view’s safe area

- [Positioning content relative to the safe area](../positioning-content-relative-to-the-safe-area.md) — Position views so that they aren’t obstructed by other content.
- [additionalSafeAreaInsets](additionalsafeareainsets.md) — Custom insets that you specify to modify the view controller’s safe area.
