---
title: UIWritingToolsCoordinator.TextAnimation.indicateGrammar
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textanimation/indicategrammar
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textanimation/indicategrammar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textanimation/indicategrammar.json'
content_hash: 'sha256:100182aca0ca7007'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextAnimation](../textanimation.md)

# UIWritingToolsCoordinator.TextAnimation.indicateGrammar

<sub>Case</sub>

The animation effect that Writing Tools performs on grammar issues when they are first indicated.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case indicateGrammar
```

## Discussion

When preparing for this animation, hide the portion of the text for which the grammar issue is going to be indicated. When finishing the animation, show the text again.
