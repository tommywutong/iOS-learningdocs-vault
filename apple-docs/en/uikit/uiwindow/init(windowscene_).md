---
title: 'init(windowScene:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindow/init(windowscene:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/init(windowscene:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/init%28windowscene%3A%29.json'
content_hash: 'sha256:9b5f69eaf6781b66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# init(windowScene:)

<sub>Initializer</sub>

Creates a window and associates it with the specified scene object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(windowScene: UIWindowScene)
```

## Parameters

- `windowScene` — The scene object in which to display the window.

## Return Value

A new window object associated with the specified scene.

## Discussion

This method creates the new window and automatically associates it with the specified scene. You can access this window later from the scene’s [windows](../uiwindowscene/windows.md) property.
