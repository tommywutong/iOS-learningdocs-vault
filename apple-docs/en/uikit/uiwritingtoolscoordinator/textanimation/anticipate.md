---
title: UIWritingToolsCoordinator.TextAnimation.anticipate
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textanimation/anticipate
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textanimation/anticipate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textanimation/anticipate.json'
content_hash: 'sha256:348131516f37b57a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [TextAnimation](../textanimation.md)

# UIWritingToolsCoordinator.TextAnimation.anticipate

<sub>Case</sub>

The animation that Writing Tools performs when waiting to receive results from the large language model.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case anticipate
```

## Discussion

This type of animation applies a visual effect to the text that Writing Tools is evaluating. When preparing for this animation, hide the text that Writing Tools is about to evaluate. In the same space where that text appears, Writing Tools displays a preview image that you provide and animates changes to that image.

## See Also

### Getting the animation types

- [UIWritingToolsCoordinatorTextAnimationInsert](insert.md) — The animation that Writing Tools performs when inserting text into your view.
- [UIWritingToolsCoordinatorTextAnimationRemove](remove.md) — The animation that Writing Tools performs when removing text from your view.
