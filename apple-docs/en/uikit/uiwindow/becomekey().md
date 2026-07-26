---
title: becomeKey()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/becomekey()
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/becomekey()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/becomekey%28%29.json'
content_hash: 'sha256:5b56817e77df3a83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# becomeKey()

<sub>Instance Method</sub>

Tells the window that it’s the key window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func becomeKey()
```

## Discussion

Never call this method directly. The system calls this method and posts [UIWindowDidBecomeKeyNotification](didbecomekeynotification.md) to let the window know that it’s the key window. The default implementation of this method does nothing, but subclasses can override it and use it to perform tasks related to becoming the key window.

In iOS 15 and later, the system calls this method when the window becomes the key window in its scene. In iOS 14 and earlier, the system calls this method when the window becomes the key window in the app.

## See Also

### Making windows key

- [keyWindow](iskeywindow.md) — A Boolean value that indicates whether the window is the key window.
- [canBecomeKeyWindow](canbecomekey.md) — A Boolean value that indicates whether the window can become the key window.
- [- makeKeyAndVisible](<makekeyandvisible().md>) — Shows the window and makes it the key window.
- [- makeKeyWindow](<makekey().md>) — Makes the window the key window.
- [- resignKeyWindow](<resignkey().md>) — Tells the window that it’s no longer the key window.
