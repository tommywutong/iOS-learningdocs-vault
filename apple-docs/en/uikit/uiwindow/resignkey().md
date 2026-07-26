---
title: resignKey()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/resignkey()
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/resignkey()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/resignkey%28%29.json'
content_hash: 'sha256:b1ae36bd2762781a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# resignKey()

<sub>Instance Method</sub>

Tells the window that it’s no longer the key window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resignKey()
```

## Discussion

Never call this method directly. The system calls this method and posts [UIWindowDidResignKeyNotification](didresignkeynotification.md) to let the window know when it’s no longer the key window. The default implementation of this method does nothing, but subclasses can override it and use it to perform tasks related to resigning the key window status.

In iOS 15 and later, the system calls this method when the window is no longer the key window in its scene. In iOS 14 and earlier, the system calls this method when the window is no longer the key window in the app.

## See Also

### Making windows key

- [keyWindow](iskeywindow.md) — A Boolean value that indicates whether the window is the key window.
- [canBecomeKeyWindow](canbecomekey.md) — A Boolean value that indicates whether the window can become the key window.
- [- makeKeyAndVisible](<makekeyandvisible().md>) — Shows the window and makes it the key window.
- [- makeKeyWindow](<makekey().md>) — Makes the window the key window.
- [- becomeKeyWindow](<becomekey().md>) — Tells the window that it’s the key window.
