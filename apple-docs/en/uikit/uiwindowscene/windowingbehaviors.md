---
title: windowingBehaviors
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/windowingbehaviors
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/windowingbehaviors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/windowingbehaviors.json'
content_hash: 'sha256:46521ebd7c52a214'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# windowingBehaviors

<sub>Instance Property</sub>

An object that specifies the behaviors of the window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var windowingBehaviors: UISceneWindowingBehaviors? { get }
```

## Discussion

For Mac apps built with Mac Catalyst, use this property to specify whether the scene’s window displays minimize and close buttons. This property is `nil` on unsupported platforms.

## See Also

### Determining window behaviors

- [fullScreen](isfullscreen.md) — A Boolean value that indicates whether the window scene is full screen or windowed.
- [UISceneWindowingBehaviors](../uiscenewindowingbehaviors.md) — An object with properties that determine the behavior of a window.
