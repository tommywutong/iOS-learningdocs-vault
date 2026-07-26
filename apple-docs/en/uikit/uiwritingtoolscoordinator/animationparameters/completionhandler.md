---
title: completionHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/animationparameters/completionhandler
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/animationparameters/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/animationparameters/completionhandler.json'
content_hash: 'sha256:938011704552f9be'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [AnimationParameters](../animationparameters.md)

# completionHandler

<sub>Instance Property</sub>

A custom block to run when the system animations finish.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var completionHandler: (() -> Void)? { get set }
```

## Discussion

Set this property to a block that you want the system to run when any animations finish. The block you provide must have no return value and no parameters. The system executes this block once when the current animation finish.

## See Also

### Creating custom animations

- [progressHandler](progresshandler.md) — A custom block that runs at the same time as the system animations.
