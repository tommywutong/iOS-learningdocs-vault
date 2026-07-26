---
title: 'addAction(handler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiupdatelink/addaction(handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/addaction%28handler%3A%29.json'
content_hash: 'sha256:54cd95ac8a01dd81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# addAction(handler:)

<sub>Instance Method</sub>

Adds an action with the specified handler to the UI update link.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addAction(handler: @escaping (UIUpdateLink, UIUpdateInfo) -> Void)
```

## Discussion

This method adds the action to the [beforeCADisplayLinkDispatch](../uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [- addActionToPhase:handler:](<addaction(to_handler_).md>) instead.

## See Also

### Adding actions

- [- addActionToPhase:handler:](<addaction(to_handler_).md>) — Adds an action with the specified handler to the UI update link for a particular UI update phase.
- [- addActionWithTarget:selector:](<addaction(target_selector_).md>) — Adds an action with the specified target and selector to the UI update link.
- [- addActionToPhase:target:selector:](<addaction(to_target_selector_).md>) — Adds an action with the specified target and selector to the UI update link for a particular UI update phase.
- [UIUpdateActionPhase](../uiupdateactionphase.md) — An object that defines specific phases of the UI update process.
