---
title: 'textDraggableView(_:willAnimateLiftWith:session:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdragdelegate/textdraggableview(_:willanimateliftwith:session:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragdelegate/textdraggableview(_:willanimateliftwith:session:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragdelegate/textdraggableview%28_%3Awillanimateliftwith%3Asession%3A%29.json'
content_hash: 'sha256:1ab31b7e1a70c9cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragDelegate](../uitextdragdelegate.md)

# textDraggableView(_:willAnimateLiftWith:session:)

<sub>Instance Method</sub>

Tells the delegate when the lift animation is about to begin, and gives you a chance to animate additional changes alongside the system animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func textDraggableView(_ textDraggableView: any UIView & UITextDraggable, willAnimateLiftWith animator: any UIDragAnimating, session: any UIDragSession)
```

## Parameters

- `textDraggableView` — The text view where the drag activity was started.

- `animator` — The animator that you use when adding animations.

- `session` — The drag session of the current drag activity.

## Discussion

You implement this delegate method when you want to add animations that happen alongside the system animation during the lift activity. To add such an animation, use the animator’s [- addAnimations:](<../uidraganimating/addanimations(__).md>) method. To add an animation that happens after the system animation has ended, use the animator’s [- addCompletion:](<../uidraganimating/addcompletion(__).md>) method.
