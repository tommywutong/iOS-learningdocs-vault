---
title: makeKeyAndVisible()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/makekeyandvisible()
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/makekeyandvisible()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/makekeyandvisible%28%29.json'
content_hash: 'sha256:1733dedb5d9644d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# makeKeyAndVisible()

<sub>Instance Method</sub>

Shows the window and makes it the key window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func makeKeyAndVisible()
```

## Discussion

This is a convenience method to show the current window and position it in front of all other windows at the same level or lower. If you only want to show the window, change its [hidden](../uiview/ishidden.md) property to [false](../../swift/false.md).

## See Also

### Making windows key

- [keyWindow](iskeywindow.md) — A Boolean value that indicates whether the window is the key window.
- [canBecomeKeyWindow](canbecomekey.md) — A Boolean value that indicates whether the window can become the key window.
- [- makeKeyWindow](<makekey().md>) — Makes the window the key window.
- [- becomeKeyWindow](<becomekey().md>) — Tells the window that it’s the key window.
- [- resignKeyWindow](<resignkey().md>) — Tells the window that it’s no longer the key window.
