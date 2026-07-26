---
title: UIWritingToolsCoordinator.TextReplacementReason.interactive
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/interactive
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/interactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/interactive.json'
content_hash: 'sha256:fe1ab8c61cb5d692'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextReplacementReason](../textreplacementreason.md)

# UIWritingToolsCoordinator.TextReplacementReason.interactive

<sub>Case</sub>

An option to animate the replacement of text in your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case interactive
```

## Discussion

When Writing Tools requests an interactive change in your delegate’s `UIWritingToolsCoordinator/Delegate/writingToolsCoordinator(_:replaceRange:inContext:proposedText:reason:animationParameters:completion:)` method, it passes a valid set of animation parameters to that method. Update your view’s text storage and use the provided [AnimationParameters](../animationparameters.md) type to create any view-specific animations you need to support the animated replacement of the text.

## See Also

### Getting the reasons

- [UIWritingToolsCoordinatorTextReplacementReasonNoninteractive](noninteractive.md) — An option to replace the text in your view without animating the change.
