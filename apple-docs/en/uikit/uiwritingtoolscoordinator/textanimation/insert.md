---
title: UIWritingToolsCoordinator.TextAnimation.insert
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textanimation/insert
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textanimation/insert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textanimation/insert.json'
content_hash: 'sha256:9b8f4ef2447f1899'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextAnimation](../textanimation.md)

# UIWritingToolsCoordinator.TextAnimation.insert

<sub>Case</sub>

The animation that Writing Tools performs when inserting text into your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case insert
```

## Discussion

This type of animation shows the insertion of text to your view. When preparing for this animation, hide the text in the provided range if you haven’t already. If you support animating the reflow of your view’s text, you can also prepare any other animations you need. Writing Tools uses a preview object you provide to animate the insertion of the text.

## See Also

### Getting the animation types

- [UIWritingToolsCoordinatorTextAnimationAnticipate](anticipate.md) — The animation that Writing Tools performs when waiting to receive results from the large language model.
- [UIWritingToolsCoordinatorTextAnimationRemove](remove.md) — The animation that Writing Tools performs when removing text from your view.
