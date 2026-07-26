---
title: windows
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/windows
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/windows'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/windows.json'
content_hash: 'sha256:55bc1263a1ea4a92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# windows

<sub>Instance Property</sub>

The windows associated with the scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var windows: [UIWindow] { get }
```

## Discussion

Use this property to retrieve the windows associated with the scene. To remove the window from the current scene, or move it to a different scene, change the value of the window’s [windowScene](../uiwindow/windowscene.md) property.

## See Also

### Getting the active windows

- [keyWindow](keywindow.md) — The key window associated with the scene.
- [screen](screen.md) — The screen that displays the contents of the scene.
