---
title: 'addAction(to:target:selector:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiupdatelink/addaction(to:target:selector:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(to:target:selector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/addaction%28to%3Atarget%3Aselector%3A%29.json'
content_hash: 'sha256:4cdae1a77891f633'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# addAction(to:target:selector:)

<sub>Instance Method</sub>

Adds an action with the specified target and selector to the UI update link for a particular UI update phase.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addAction(to phase: UIUpdateActionPhase, target: Any, selector: Selector)
```

## See Also

### Adding actions

- [- addActionWithHandler:](<addaction(handler_).md>) — Adds an action with the specified handler to the UI update link.
- [- addActionToPhase:handler:](<addaction(to_handler_).md>) — Adds an action with the specified handler to the UI update link for a particular UI update phase.
- [- addActionWithTarget:selector:](<addaction(target_selector_).md>) — Adds an action with the specified target and selector to the UI update link.
- [UIUpdateActionPhase](../uiupdateactionphase.md) — An object that defines specific phases of the UI update process.
