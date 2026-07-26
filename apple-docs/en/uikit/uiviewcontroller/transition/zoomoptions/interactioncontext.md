---
title: UIViewController.Transition.ZoomOptions.InteractionContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transition/zoomoptions/interactioncontext
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/interactioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition/zoomoptions/interactioncontext.json'
content_hash: 'sha256:ba29e25bea9a590c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIViewController](../../../uiviewcontroller.md) · [Transition](../../transition.md) · [ZoomOptions](../zoomoptions.md)

# UIViewController.Transition.ZoomOptions.InteractionContext

<sub>Class</sub>

Data you can use to determine whether an interactive dismissal can begin.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class InteractionContext
```

## Relationships

- **Inherits From**: [NSObject](../../../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../../../swift/cvararg.md), [CustomDebugStringConvertible](../../../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../../../swift/customstringconvertible.md), [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [NSObjectProtocol](../../../../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the context

- [location](interactioncontext/location.md) — The touch’s location.
- [velocity](interactioncontext/velocity.md) — The touch’s velocity.
- [willBegin](interactioncontext/willbegin.md) — A Boolean value that indicates whether the transition is beginning.

## See Also

### Accessing the animation state

- [interactiveDismissShouldBegin](interactivedismissshouldbegin.md) — A closure that determines whether an interactive dismissal can begin.
