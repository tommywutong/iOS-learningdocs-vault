---
title: UIWritingToolsCoordinator.TextReplacementReason.rejected
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/rejected
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/rejected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/rejected.json'
content_hash: 'sha256:bb7c466e8eaa9586'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextReplacementReason](../textreplacementreason.md)

# UIWritingToolsCoordinator.TextReplacementReason.rejected

<sub>Case</sub>

An option to replace the text in your view when a grammar suggestion is rejected.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case rejected
```

## Discussion

When the user interacts with a grammar issue and the UI is shown, and the option to ignore a suggestion is chosen, this reason will be used. Update your view’s text storage without animating the change. In addition, use `ignoreGrammarRange` on [UITextChecker](../../uitextchecker.md) to make sure that the suggestion will continue to be ignored.
