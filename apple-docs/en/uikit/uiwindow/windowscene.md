---
title: windowScene
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/windowscene
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/windowscene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/windowscene.json'
content_hash: 'sha256:041f0917ab805252'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# windowScene

<sub>Instance Property</sub>

The scene containing the window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var windowScene: UIWindowScene? { get set }
```

## Discussion

Changing the value of this property moves the window to the newly specified scene. Setting the property to `nil` removes the window from its current scene.

## See Also

### Getting related objects

- [avDisplayManager](avdisplaymanager.md) — The display manager that handles requests for screen resolution, refresh rate, and HDR mode information.
