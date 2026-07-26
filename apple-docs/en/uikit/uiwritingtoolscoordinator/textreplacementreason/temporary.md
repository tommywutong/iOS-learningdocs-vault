---
title: UIWritingToolsCoordinator.TextReplacementReason.temporary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/temporary
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/temporary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/temporary.json'
content_hash: 'sha256:1ad13484e5734400'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextReplacementReason](../textreplacementreason.md)

# UIWritingToolsCoordinator.TextReplacementReason.temporary

<sub>Case</sub>

An option to replace the text in your view when a grammar suggestion is temporarily shown to preview the proposed change in the text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case temporary
```

## Discussion

When the user interacts with a grammar issue and the UI is shown, in some cases the suggestion needs to be shown temporarily. Update your view’s text storage without animating the change.
