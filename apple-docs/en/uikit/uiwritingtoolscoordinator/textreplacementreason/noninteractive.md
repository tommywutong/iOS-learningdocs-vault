---
title: UIWritingToolsCoordinator.TextReplacementReason.noninteractive
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/noninteractive
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/noninteractive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/noninteractive.json'
content_hash: 'sha256:09f7b05e2ccda57d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextReplacementReason](../textreplacementreason.md)

# UIWritingToolsCoordinator.TextReplacementReason.noninteractive

<sub>Case</sub>

An option to replace the text in your view without animating the change.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case noninteractive
```

## Discussion

When Writing Tools requests a noninteractive change in your delegate’s `UIWritingToolsCoordinator/Delegate/writingToolsCoordinator(_:replaceRange:inContext:proposedText:reason:animationParameters:completion:)` method, update your view’s text storage without animating the change.

## See Also

### Getting the reasons

- [UIWritingToolsCoordinatorTextReplacementReasonInteractive](interactive.md) — An option to animate the replacement of text in your view.
