---
title: UIWritingToolsCoordinator.ContextScope.fullDocument
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/contextscope/fulldocument
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/contextscope/fulldocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/contextscope/fulldocument.json'
content_hash: 'sha256:bc0e3ceb0047fab3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [ContextScope](../contextscope.md)

# UIWritingToolsCoordinator.ContextScope.fullDocument

<sub>Case</sub>

An option to provide all of your view’s text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case fullDocument
```

## Discussion

With this option, include all of the text your view manages. If your view has multiple text storage objects, create a separate context object for each one.

## See Also

### Getting the scope

- [UIWritingToolsCoordinatorContextScopeUserSelection](userselection.md) — An option to provide only the view’s currently selected text.
- [UIWritingToolsCoordinatorContextScopeVisibleArea](visiblearea.md) — An option to provide only the text in the currently visible portion of your view.
