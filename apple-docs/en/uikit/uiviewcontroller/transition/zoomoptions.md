---
title: UIViewController.Transition.ZoomOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transition/zoomoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition/zoomoptions.json'
content_hash: 'sha256:ab25fa261d487dc1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIViewController](../../uiviewcontroller.md) · [Transition](../transition.md)

# UIViewController.Transition.ZoomOptions

<sub>Class</sub>

Options for a zoom transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class ZoomOptions
```

## Relationships

- **Inherits From**: [NSObject](../../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../../swift/cvararg.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [NSCopying](../../../foundation/nscopying.md), [NSObjectProtocol](../../../objectivec/nsobjectprotocol.md)

## Topics

### Setting options

- [alignmentRectProvider](zoomoptions/alignmentrectprovider.md) — A closure that returns the alignment rectangle for the starting and ending views.
- [AlignmentRectContext](zoomoptions/alignmentrectcontext.md) — An object that contains a zoom transition’s starting and ending views.
- [dimmingColor](zoomoptions/dimmingcolor.md) — The dimming color.
- [dimmingVisualEffect](zoomoptions/dimmingvisualeffect.md) — The dimming visual effect.

### Accessing the animation state

- [interactiveDismissShouldBegin](zoomoptions/interactivedismissshouldbegin.md) — A closure that determines whether an interactive dismissal can begin.
- [InteractionContext](zoomoptions/interactioncontext.md) — Data you can use to determine whether an interactive dismissal can begin.

## See Also

### Creating zoom transitions

- [zoom(options:sourceViewProvider:)](<zoom(options_sourceviewprovider_).md>) — Creates a zoom transition from the view that the source provider specifies.
- [ZoomSourceViewProviderContext](zoomsourceviewprovidercontext.md) — A context object that contains references to the view controllers from a zoom transition.
