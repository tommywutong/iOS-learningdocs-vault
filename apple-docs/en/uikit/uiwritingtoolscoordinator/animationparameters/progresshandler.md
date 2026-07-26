---
title: progressHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/animationparameters/progresshandler
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/animationparameters/progresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/animationparameters/progresshandler.json'
content_hash: 'sha256:215a1572eaa4c243'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [AnimationParameters](../animationparameters.md)

# progressHandler

<sub>Instance Property</sub>

A custom block that runs at the same time as the system animations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var progressHandler: ((Float) -> Void)? { get set }
```

## Discussion

If you have animations you want to run at the same time as the system animations, assign a block to this property and use it to run your animations. The block you provide must have no return value and take a floating-point value as a parameter. The parameter indicates the current progress of the animations as a percentage value between `0.0` to `1.0`. The system executes your block multiple times during the course of the animations, providing an updated completion value each time.

## See Also

### Creating custom animations

- [completionHandler](completionhandler.md) — A custom block to run when the system animations finish.
