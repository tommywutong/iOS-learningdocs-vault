---
title: makeKey()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/makekey()
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/makekey()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/makekey%28%29.json'
content_hash: 'sha256:daf50612cf067f2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# makeKey()

<sub>Instance Method</sub>

Makes the window the key window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func makeKey()
```

## Discussion

Use this method to make the window key without changing its visibility. The key window receives keyboard and other non-touch related events. This method causes the previous key window to resign the key status.

## See Also

### Making windows key

- [keyWindow](iskeywindow.md) — A Boolean value that indicates whether the window is the key window.
- [canBecomeKeyWindow](canbecomekey.md) — A Boolean value that indicates whether the window can become the key window.
- [- makeKeyAndVisible](<makekeyandvisible().md>) — Shows the window and makes it the key window.
- [- becomeKeyWindow](<becomekey().md>) — Tells the window that it’s the key window.
- [- resignKeyWindow](<resignkey().md>) — Tells the window that it’s no longer the key window.
