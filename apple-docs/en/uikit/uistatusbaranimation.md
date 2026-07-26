---
title: UIStatusBarAnimation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistatusbaranimation
source_url: 'https://developer.apple.com/documentation/uikit/uistatusbaranimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistatusbaranimation.json'
content_hash: 'sha256:54abe992d478615b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStatusBarAnimation

<sub>Enumeration</sub>

Constants that specify the animation of the status bar as it’s hidden or made visible.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIStatusBarAnimation
```

## Overview

Constants of the [UIStatusBarAnimation](uistatusbaranimation.md) type are arguments of the [- setStatusBarHidden:withAnimation:](<uiapplication/setstatusbarhidden(__with_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIStatusBarAnimationNone](uistatusbaranimation/none.md) — No animation is applied to the status bar as it is shown or hidden.
- [UIStatusBarAnimationFade](uistatusbaranimation/fade.md) — The status bar fades in and out as it is shown or hidden, respectively.
- [UIStatusBarAnimationSlide](uistatusbaranimation/slide.md) — The status bar slides in or out as it is shown or hidden, respectively.

### Initializers

- [init(rawValue:)](<uistatusbaranimation/init(rawvalue_).md>)

## See Also

### Deprecated enumerations

- [UIDirectionalRectEdge](uidirectionalrectedge.md) — Constants that specify an edge or a set of edges, taking the user interface layout direction into account. _(deprecated)_
