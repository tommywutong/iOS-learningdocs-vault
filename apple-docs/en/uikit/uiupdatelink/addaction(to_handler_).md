---
title: 'addAction(to:handler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiupdatelink/addaction(to:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(to:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/addaction%28to%3Ahandler%3A%29.json'
content_hash: 'sha256:b41cd68ba236ac26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# addAction(to:handler:)

<sub>Instance Method</sub>

Adds an action with the specified handler to the UI update link for a particular UI update phase.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addAction(to phase: UIUpdateActionPhase, handler: @escaping (UIUpdateLink, UIUpdateInfo) -> Void)
```

## See Also

### Adding actions

- [- addActionWithHandler:](<addaction(handler_).md>) — Adds an action with the specified handler to the UI update link.
- [- addActionWithTarget:selector:](<addaction(target_selector_).md>) — Adds an action with the specified target and selector to the UI update link.
- [- addActionToPhase:target:selector:](<addaction(to_target_selector_).md>) — Adds an action with the specified target and selector to the UI update link for a particular UI update phase.
- [UIUpdateActionPhase](../uiupdateactionphase.md) — An object that defines specific phases of the UI update process.
