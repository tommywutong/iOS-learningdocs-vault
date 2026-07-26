---
title: 'addAction(target:selector:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiupdatelink/addaction(target:selector:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(target:selector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/addaction%28target%3Aselector%3A%29.json'
content_hash: 'sha256:860bcb96f1719883'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# addAction(target:selector:)

<sub>Instance Method</sub>

Adds an action with the specified target and selector to the UI update link.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addAction(target: Any, selector: Selector)
```

## Discussion

This method adds the action to the [beforeCADisplayLinkDispatch](../uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [- addActionToPhase:target:selector:](<addaction(to_target_selector_).md>) instead.

## See Also

### Adding actions

- [- addActionWithHandler:](<addaction(handler_).md>) — Adds an action with the specified handler to the UI update link.
- [- addActionToPhase:handler:](<addaction(to_handler_).md>) — Adds an action with the specified handler to the UI update link for a particular UI update phase.
- [- addActionToPhase:target:selector:](<addaction(to_target_selector_).md>) — Adds an action with the specified target and selector to the UI update link for a particular UI update phase.
- [UIUpdateActionPhase](../uiupdateactionphase.md) — An object that defines specific phases of the UI update process.
