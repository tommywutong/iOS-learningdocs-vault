---
title: keyWindow
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/keywindow
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/keywindow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/keywindow.json'
content_hash: 'sha256:f04c79df2fc644b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# keyWindow

<sub>Instance Property</sub>

The key window associated with the scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var keyWindow: UIWindow? { get }
```

## Discussion

The key window receives keyboard and other non-touch-related events. Of a scene’s associated [windows](windows.md), only one window at a time may be the key window.

## See Also

### Getting the active windows

- [windows](windows.md) — The windows associated with the scene.
- [screen](screen.md) — The screen that displays the contents of the scene.
