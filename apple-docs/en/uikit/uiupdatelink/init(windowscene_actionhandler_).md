---
title: 'init(windowScene:actionHandler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiupdatelink/init(windowscene:actionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/init(windowscene:actionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/init%28windowscene%3Aactionhandler%3A%29.json'
content_hash: 'sha256:ebdd26f958bfac79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# init(windowScene:actionHandler:)

<sub>Initializer</sub>

Creates a UI update link for the specified window using the specified action handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(windowScene: UIWindowScene, actionHandler handler: @escaping (UIUpdateLink, UIUpdateInfo) -> Void)
```

## Discussion

This initializer adds the action to the [beforeCADisplayLinkDispatch](../uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [- addActionToPhase:handler:](<addaction(to_handler_).md>) or [- addActionToPhase:target:selector:](<addaction(to_target_selector_).md>) instead.

## See Also

### Creating a UI update link

- [+ updateLinkForView:](<init(view_).md>) — Creates a UI update link for the specified view.
- [+ updateLinkForView:actionHandler:](<init(view_actionhandler_).md>) — Creates a UI update link for the specified view using the specified action handler.
- [+ updateLinkForView:actionTarget:selector:](<init(view_actiontarget_selector_).md>) — Creates a UI update link for the specified view using the specified target and action.
- [+ updateLinkForWindowScene:](<init(windowscene_).md>) — Creates a UI update link for the specified window.
- [+ updateLinkForWindowScene:actionTarget:selector:](<init(windowscene_actiontarget_selector_).md>) — Creates a UI update link for the specified window using the specified target and action.
