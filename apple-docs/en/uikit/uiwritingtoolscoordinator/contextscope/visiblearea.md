---
title: UIWritingToolsCoordinator.ContextScope.visibleArea
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/contextscope/visiblearea
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/contextscope/visiblearea'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/contextscope/visiblearea.json'
content_hash: 'sha256:90649fdb6018080e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [ContextScope](../contextscope.md)

# UIWritingToolsCoordinator.ContextScope.visibleArea

<sub>Case</sub>

An option to provide only the text in the currently visible portion of your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case visibleArea
```

## Discussion

With this option, include only the currently visible text, along with some additional text before and after the visible text.

## See Also

### Getting the scope

- [UIWritingToolsCoordinatorContextScopeUserSelection](userselection.md) — An option to provide only the view’s currently selected text.
- [UIWritingToolsCoordinatorContextScopeFullDocument](fulldocument.md) — An option to provide all of your view’s text.
