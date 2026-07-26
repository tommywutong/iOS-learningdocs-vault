---
title: 'init(view:parameters:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitargetedpreview/init(view:parameters:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitargetedpreview/init(view:parameters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitargetedpreview/init%28view%3Aparameters%3A%29.json'
content_hash: 'sha256:59ea4ef5dca70562'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITargetedPreview](../uitargetedpreview.md)

# init(view:parameters:)

<sub>Initializer</sub>

Creates a targeted preview for a view in the current window and including the specified parameters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(view: UIView, parameters: UIPreviewParameters)
```

## Parameters

- `view` — The view to animate. This view must be in a window.

- `parameters` — The animation parameters.

## Return Value

A new targeted preview object.

## See Also

### Creating a targeted preview object

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- initWithView:parameters:target:](<init(view_parameters_target_).md>) — Creates a targeted preview with the specified view, parameters, and target container.
- [- initWithView:](<init(view_).md>) — Creates a targeted preview for a view in the current window.
