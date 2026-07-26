---
title: isKeyWindow
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/iskeywindow
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/iskeywindow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/iskeywindow.json'
content_hash: 'sha256:f79d8fcd40574e81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# isKeyWindow

<sub>Instance Property</sub>

A Boolean value that indicates whether the window is the key window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isKeyWindow: Bool { get }
```

## Discussion

In iOS 15 and later, the value of this property is [true](../../swift/true.md) when the window is the key window of its scene. In iOS 14 and earlier, the value of this property is [true](../../swift/true.md) when the window is the key window in the app.

The key window receives keyboard and other non-touch-related events. Only one window at a time may be the key window.

## See Also

### Making windows key

- [canBecomeKeyWindow](canbecomekey.md) — A Boolean value that indicates whether the window can become the key window.
- [- makeKeyAndVisible](<makekeyandvisible().md>) — Shows the window and makes it the key window.
- [- makeKeyWindow](<makekey().md>) — Makes the window the key window.
- [- becomeKeyWindow](<becomekey().md>) — Tells the window that it’s the key window.
- [- resignKeyWindow](<resignkey().md>) — Tells the window that it’s no longer the key window.
