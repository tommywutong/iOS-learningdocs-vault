---
title: UIWritingToolsCoordinator.TextAnimation.remove
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textanimation/remove
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textanimation/remove'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textanimation/remove.json'
content_hash: 'sha256:08b2e8d7aebf4745'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextAnimation](../textanimation.md)

# UIWritingToolsCoordinator.TextAnimation.remove

<sub>Case</sub>

The animation that Writing Tools performs when removing text from your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case remove
```

## Discussion

This type of animation shows the removal of text from your view. When preparing for this animation, hide the text in the provided range if you haven’t already. If you support animating the reflow of your view’s text, you can also prepare any other animations you need. Writing Tools uses a preview object you provide to animate the removal of the text.

## See Also

### Getting the animation types

- [UIWritingToolsCoordinatorTextAnimationAnticipate](anticipate.md) — The animation that Writing Tools performs when waiting to receive results from the large language model.
- [UIWritingToolsCoordinatorTextAnimationInsert](insert.md) — The animation that Writing Tools performs when inserting text into your view.
