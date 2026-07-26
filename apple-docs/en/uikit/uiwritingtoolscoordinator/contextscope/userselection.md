---
title: UIWritingToolsCoordinator.ContextScope.userSelection
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/contextscope/userselection
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/contextscope/userselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/contextscope/userselection.json'
content_hash: 'sha256:182f455eacf3c0f3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [ContextScope](../contextscope.md)

# UIWritingToolsCoordinator.ContextScope.userSelection

<sub>Case</sub>

An option to provide only the view’s currently selected text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case userSelection
```

## Discussion

With this option, include the selected text in your context object, along with some additional text before and after the selection. When performing changes inline with your view’s content, Writing Tools applies animations only to the selected text.

## See Also

### Getting the scope

- [UIWritingToolsCoordinatorContextScopeFullDocument](fulldocument.md) — An option to provide all of your view’s text.
- [UIWritingToolsCoordinatorContextScopeVisibleArea](visiblearea.md) — An option to provide only the text in the currently visible portion of your view.
