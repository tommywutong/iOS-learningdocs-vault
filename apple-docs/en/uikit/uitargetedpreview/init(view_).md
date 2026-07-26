---
title: 'init(view:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitargetedpreview/init(view:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitargetedpreview/init(view:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitargetedpreview/init%28view%3A%29.json'
content_hash: 'sha256:42a047848b993635'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITargetedPreview](../uitargetedpreview.md)

# init(view:)

<sub>Initializer</sub>

Creates a targeted preview for a view in the current window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(view: UIView)
```

## Parameters

- `view` — The view to animate. This view must be in a window.

## Return Value

A new targeted preview object.

## See Also

### Creating a targeted preview object

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- initWithView:parameters:target:](<init(view_parameters_target_).md>) — Creates a targeted preview with the specified view, parameters, and target container.
- [- initWithView:parameters:](<init(view_parameters_).md>) — Creates a targeted preview for a view in the current window and including the specified parameters.
