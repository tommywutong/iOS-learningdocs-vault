---
title: canBecomeKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/canbecomekey
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/canbecomekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/canbecomekey.json'
content_hash: 'sha256:0ec63c6b977f52c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# canBecomeKey

<sub>Instance Property</sub>

A Boolean value that indicates whether the window can become the key window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var canBecomeKey: Bool { get }
```

## Discussion

The default value is [true](../../swift/true.md). To indicate that the window can’t become the key window, override [canBecomeKeyWindow](canbecomekey.md) and return [false](../../swift/false.md).

## See Also

### Making windows key

- [keyWindow](iskeywindow.md) — A Boolean value that indicates whether the window is the key window.
- [- makeKeyAndVisible](<makekeyandvisible().md>) — Shows the window and makes it the key window.
- [- makeKeyWindow](<makekey().md>) — Makes the window the key window.
- [- becomeKeyWindow](<becomekey().md>) — Tells the window that it’s the key window.
- [- resignKeyWindow](<resignkey().md>) — Tells the window that it’s no longer the key window.
